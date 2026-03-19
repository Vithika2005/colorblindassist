import cv2
import numpy as np
from colorspacious import cspace_converter

# Initial settings
severity = 50
cvd_type = "deuteranomaly"

def get_converter(severity):
    target_space = {
        "name": "sRGB1+CVD",
        "cvd_type": cvd_type,
        "severity": severity
    }
    return cspace_converter("sRGB1", target_space)

def daltonize_frame(frame, converter):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) / 255.0
    h, w, _ = rgb.shape
    flat_rgb = rgb.reshape(-1, 3)

    simulated = converter(flat_rgb).reshape(h, w, 3)
    error = rgb - simulated
    daltonized = np.clip(rgb + 0.7 * error, 0, 1)

    return cv2.cvtColor((daltonized * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)

# Open webcam
cap = cv2.VideoCapture(0)
converter = get_converter(severity)

print("Press ↑ / ↓ arrows to increase or decrease severity. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    output = daltonize_frame(frame, converter)

    cv2.putText(output, f"Severity: {severity}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('Daltonized Live Feed', output)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == 82:  # Up arrow
        if severity < 100:
            severity += 25
            converter = get_converter(severity)
    elif key == 84:  # Down arrow
        if severity > 0:
            severity -= 25
            converter = get_converter(severity)

cap.release()
cv2.destroyAllWindows()
