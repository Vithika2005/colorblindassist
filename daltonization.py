import cv2
import numpy as np
from colorspacious import cspace_converter

# ----------------------------
# Initial Settings
# ----------------------------

severity = 50

cvd_types = [
    "protanomaly",
    "deuteranomaly",
    "tritanomaly"
]

current_cvd_index = 1


# ----------------------------
# Create Converter Function
# ----------------------------

def get_converter(severity, cvd_type):

    target_space = {
        "name": "sRGB1+CVD",
        "cvd_type": cvd_type,
        "severity": severity
    }

    converter = cspace_converter("sRGB1", target_space)

    return converter


# ----------------------------
# Daltonization Pipeline
# ----------------------------

def daltonize_frame(frame, converter):

    # Convert BGR → RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Normalize
    rgb = rgb / 255.0

    h, w, _ = rgb.shape

    # Flatten image
    flat_rgb = rgb.reshape(-1, 3)

    # Simulate color blindness
    simulated = converter(flat_rgb)

    simulated = simulated.reshape(h, w, 3)
    simulated = np.clip(simulated, 0, 1)

    # Compute color loss
    error = rgb - simulated

    # Daltonization correction
    corrected = rgb + 0.7 * error

    corrected = np.clip(corrected, 0, 1)

    corrected = (corrected * 255).astype(np.uint8)

    # Convert back to BGR
    corrected = cv2.cvtColor(corrected, cv2.COLOR_RGB2BGR)

    return corrected


# ----------------------------
# Open Webcam
# ----------------------------

cap = cv2.VideoCapture(0)

converter = get_converter(severity, cvd_types[current_cvd_index])


# ----------------------------
# Trackbar Function
# ----------------------------

def nothing(x):
    pass


# ----------------------------
# Create Window + Slider
# ----------------------------

cv2.namedWindow("Daltonization Assistant")

cv2.createTrackbar(
    "Severity",
    "Daltonization Assistant",
    severity,
    100,
    nothing
)


print("Controls:")
print("1 → Protanopia Mode")
print("2 → Deuteranopia Mode")
print("3 → Tritanopia Mode")
print("Q → Quit")


# ----------------------------
# Main Loop
# ----------------------------

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Get severity from slider
    severity = cv2.getTrackbarPos(
        "Severity",
        "Daltonization Assistant"
    )

    # Update converter
    converter = get_converter(
        severity,
        cvd_types[current_cvd_index]
    )

    # Apply daltonization
    corrected_frame = daltonize_frame(
        frame,
        converter
    )

    label = f"{cvd_types[current_cvd_index]} | Severity {severity}"

    cv2.putText(
        corrected_frame,
        label,
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,255,255),
        2
    )

    cv2.imshow(
        "Daltonization Assistant",
        corrected_frame
    )

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    elif key == ord('1'):
        current_cvd_index = 0

    elif key == ord('2'):
        current_cvd_index = 1

    elif key == ord('3'):
        current_cvd_index = 2


cap.release()
cv2.destroyAllWindows()