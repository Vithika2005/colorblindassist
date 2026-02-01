import numpy as np
import cv2
import gradio as gr
from colorspacious import cspace_converter

def daltonize_frame(frame, severity):
    # Convert BGR to RGB and normalize
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) / 255.0

    # Flatten image
    h, w, _ = image_rgb.shape
    flat_rgb = image_rgb.reshape(-1, 3)

    # Colorspacious simulation config
    target_space = {
        "name": "sRGB1+CVD",
        "cvd_type": "deuteranomaly",
        "severity": severity
    }

    # Simulate colorblind vision
    converter = cspace_converter("sRGB1", target_space)
    simulated = converter(flat_rgb)
    simulated_img = simulated.reshape((h, w, 3))
    simulated_img = np.clip(simulated_img, 0, 1)

    # Daltonize
    error = image_rgb - simulated_img
    daltonized = np.clip(image_rgb + 0.7 * error, 0, 1)

    # Convert back to uint8 for display
    output = (daltonized * 255).astype(np.uint8)
    return output

def process_webcam(frame, severity):
    return daltonize_frame(frame, severity)

gr.Interface(
    fn=process_webcam,
    inputs=[
        gr.Image(source="webcam", streaming=True, label="📷 Webcam Feed"),
        gr.Slider(0, 100, step=25, value=50, label="🎚️ Severity")
    ],
    outputs="image",
    live=True,
    title="🎨 Real-Time Daltonization for Deuteranomaly"
).launch()
