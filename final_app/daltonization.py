import cv2
import numpy as np
from colorspacious import cspace_converter

def get_converter(severity, cvd_type):
    return cspace_converter("sRGB1", {
        "name": "sRGB1+CVD",
        "cvd_type": cvd_type,
        "severity": severity
    })

def daltonize_frame(frame, cvd_type="deuteranomaly", severity=50):
    
    converter = get_converter(severity, cvd_type)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) / 255.0

    h, w, _ = rgb.shape
    flat = rgb.reshape(-1, 3)

    simulated = converter(flat).reshape(h, w, 3)
    simulated = np.clip(simulated, 0, 1)

    error = rgb - simulated
    corrected = rgb + 0.7 * error
    corrected = np.clip(corrected, 0, 1)

    corrected = (corrected * 255).astype(np.uint8)
    corrected = cv2.cvtColor(corrected, cv2.COLOR_RGB2BGR)

    return corrected
