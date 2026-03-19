# 🚀 Color Blindness Assistant

A real-time accessibility tool that helps colorblind users perceive colors more accurately using **Daltonization** and **color vision deficiency simulation**.

---

## 🎯 Problem

Over **300 million people worldwide** suffer from color vision deficiency.

They struggle with:

- UI design (buttons, alerts)
- Traffic signals
- Graphs and charts
- Everyday visual perception

---

## 💡 Solution

This project provides:

- 🎥 Real-time webcam color correction  
- 🎚 Severity adjustment  
- 👁 Ishihara-based detection  
- 🧠 Adaptive correction based on deficiency  

---

## ⚙️ Tech Stack

- Python  
- OpenCV  
- Streamlit  
- Colorspacious  

---

## 🔬 How It Works

### Pipeline
Frame → Simulate CVD → Compute Error → Apply Daltonization → Output


### Formula
error = original - simulated
corrected = original + 0.7 * error


---

## 🧪 Features

- ✅ Protanopia / Deuteranopia / Tritanopia modes  
- ✅ Severity slider  
- ✅ Image upload support  
- ✅ Ishihara test integration  
- ✅ Real-time correction  

---

## ▶️ Run Locally

```bash
git clone <repo>
cd colorblind-assistant
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

---
1. Add your architecture image:
```markdown
## 🏗 Architecture

![Architecture](assets/architecture.png)

2. Demo 
![Demo](assets/demo.gif)

## 🔄 Project Evolution

### 🥉 Step 1: Basic Daltonization
- Initial implementation using simple correction
- Limited accuracy

### 🥈 Step 2: Colorspacious Integration
- Introduced perceptual color modeling
- Improved simulation accuracy

### 🥇 Final: Real-Time Assistant
- Streamlit UI
- Ishihara-based detection
- Severity tuning
- Real-time image correction