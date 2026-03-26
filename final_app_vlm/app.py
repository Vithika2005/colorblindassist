import streamlit as st
import cv2
import numpy as np
import time
from PIL import Image  # ✅ YOU FORGOT THIS (important)
from daltonization import daltonize_frame

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(layout="wide")

# ----------------------------
# VLM (BLIP) SETUP
# ----------------------------
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

@st.cache_resource
def load_vlm():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_vlm()

def generate_caption(image):
    pil_image = Image.fromarray(image)
    inputs = processor(pil_image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption


# ----------------------------
# SESSION STATE INIT
# ----------------------------
if "mode" not in st.session_state:
    st.session_state["mode"] = "deuteranomaly"

# ----------------------------
# TITLE
# ----------------------------
st.title("🎨 Color Blindness Assistant + AI Vision")

# ----------------------------
# SIDEBAR
# ----------------------------
mode = st.sidebar.selectbox(
    "Color Blindness Type",
    ["protanomaly", "deuteranomaly", "tritanomaly"],
    index=["protanomaly", "deuteranomaly", "tritanomaly"].index(
        st.session_state["mode"]
    )
)

severity = st.sidebar.slider("Severity", 0, 100, 50)

run_webcam = st.sidebar.checkbox("Start Webcam")
run_test = st.sidebar.checkbox("Take Ishihara Test")

# ----------------------------
# ISHIHARA TEST
# ----------------------------
def ishihara_test():
    st.subheader("Ishihara Test")

    plates = [
        ("plate1.jpeg", ["2", "Nothing"]),
        ("plate2.jpeg", ["35", "5", "3"]),
        ("plate3.jpeg", ["12"]),
        ("plate4.jpeg", ["8", "3"])
    ]

    results = []

    for i, (file, options) in enumerate(plates):
        st.image(f"ishihara/{file}", width=200)

        choice = st.radio(
            f"Plate {i+1}",
            options,
            key=f"plate_{i}"
        )

        results.append(choice)

    if st.button("Submit Test"):

        normal = 0
        protan = 0
        deutan = 0

        if results[0] == "2":
            normal += 1

        if results[1] == "35":
            normal += 1
        elif results[1] == "5":
            protan += 1
        elif results[1] == "3":
            deutan += 1

        if results[3] == "8":
            normal += 1

        if normal >= 3:
            st.success("Normal Vision")
            st.session_state["mode"] = "deuteranomaly"

        elif protan > deutan:
            st.warning("Protanomaly detected")
            st.session_state["mode"] = "protanomaly"

        elif deutan > protan:
            st.warning("Deuteranomaly detected")
            st.session_state["mode"] = "deuteranomaly"

        else:
            st.warning("General Red-Green Deficiency")

# CALL TEST
if run_test:
    ishihara_test()

# ----------------------------
# IMAGE UPLOAD
# ----------------------------
uploaded = st.file_uploader("Upload Image")

if uploaded:
    file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    corrected = daltonize_frame(img, mode, severity)

    col1, col2 = st.columns(2)

    with col1:
        st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Original")

    with col2:
        corrected_rgb = cv2.cvtColor(corrected, cv2.COLOR_BGR2RGB)
        st.image(corrected_rgb, caption="Corrected")

    # 🧠 AI DESCRIPTION
    st.subheader("🧠 AI Description")
    caption = generate_caption(corrected_rgb)
    st.write(caption)

# ----------------------------
# WEBCAM (REAL-TIME LOOP)
# ----------------------------
if run_webcam:

    cap = cv2.VideoCapture(0)
    stframe = st.empty()
    text_placeholder = st.empty()

    prev_time = time.time()

    while True:

        ret, frame = cap.read()
        if not ret:
            st.error("Camera not working")
            break

        frame = cv2.resize(frame, (640, 480))

        corrected = daltonize_frame(frame, mode, severity)

        # FPS
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        cv2.putText(corrected, f"FPS: {int(fps)}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

        cv2.putText(corrected,
                    f"{mode} | Severity {severity}",
                    (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 255, 255), 2)

        corrected_rgb = cv2.cvtColor(corrected, cv2.COLOR_BGR2RGB)

        stframe.image(corrected_rgb)

        # 🧠 AI CAPTION EVERY 3 SECONDS (NO LAG)
        if int(time.time()) % 3 == 0:
            caption = generate_caption(corrected_rgb)
            text_placeholder.markdown(f"**🧠 AI:** {caption}")

    cap.release()
