# colorblindassist
Color Blindness Assistance System that performs CVD (Color Vision Deficiency) simulation and correction using Machado-style transformation matrices, Colorspacious perceptual color space modeling, Error-redistribution daltonization, Live webcam processing. This project helps color-blind users distinguish colors by simulating how world looks to them.

# 🎨 Color Blindness Assistant — Machado-Style Daltonization

This project implements a Computer Vision–based Color Blindness Assistant that performs **Color Vision Deficiency (CVD) simulation and daltonization correction** for both images and real-time webcam feeds. It enhances color distinguishability for users with color blindness by modeling how colors are perceived under CVD and then applying corrective color redistribution to improve visual contrast.

The system combines two approaches: **Machado-style transformation matrices** for physiologically inspired CVD simulation and **perceptual color space conversion using the Colorspacious library** for severity-controlled modeling. It supports Deuteranopia / Deuteranomaly simulation and adaptive daltonization with adjustable severity levels.

---

## 🚀 Features

- Machado matrix–based CVD simulation  
- Perceptual CVD modeling with adjustable severity (0–100%)  
- Daltonization using error redistribution  
- Static image processing and visualization  
- Real-time webcam daltonization  
- Multi-severity comparison grids  
- Interactive severity control via keyboard  
- Modular and extensible processing pipeline  

---

## 🧠 Method Overview

**CVD Simulation**
- Convert image to normalized RGB
- Apply Machado Deuteranopia matrix OR Colorspacious CVD transform
- Generate simulated color-blind perception

**Daltonization**
- Compute perceptual color error between original and simulated image
- Redistribute error into visible spectrum


This improves contrast between confusing color pairs while preserving scene structure.

---

## 📷 Modes

### Image Mode
- Loads static images
- Displays original, simulated, and daltonized outputs
- Supports multi-severity visualization panels

### Webcam Mode
- Real-time frame-by-frame daltonization
- On-screen severity indicator

---

## 🛠 Tech Stack

- Python  
- OpenCV  
- NumPy  
- Matplotlib  
- Colorspacious  

---

## ♿ Applications

- Accessibility vision filters  
- UI contrast enhancement  
- AR preprocessing layers  
- Educational visualization tools  
- Assistive vision systems  

---

## 🔮 Future Improvements

- Support for Protanopia and Tritanopia  
- Object + color name detection with audio output  
- Mobile and web deployment  
- AR overlay integration  
- Pattern-based color substitution  
- User evaluation studies  

---

