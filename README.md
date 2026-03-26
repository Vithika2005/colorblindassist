# Color Blindness Assistant

An intelligent, real-time accessibility system that helps colorblind users **see**, **understand**, and **interact** with the world more clearly using **Daltonization**, **perceptual simulation**, and **AI-powered scene understanding**.

---

## Problem

Over **300 million people worldwide** live with color vision deficiency.
They struggle with:
- Traffic signals
- Graphs & data visualizations
- UI/UX elements (buttons, alerts)
- Everyday object recognition
Color isn’t just aesthetic — it’s **Information**.
And for millions, that information is broken.

---

## Solution

We built a real-time assistive system that:

- Corrects colors LIVE using Daltonization
- Adapts to severity of color blindness
- Detects deficiency using Ishihara tests
- Explains the scene using AI (Vision-Language Model)

Not just “see better” — but understand better

---

## Tech Stack

- Python
- OpenCV (real-time image processing)
- Streamlit (interactive UI)
- Colorspacious (perceptual color modeling)
- BLIP (Vision-Language Model) (AI scene understanding) 

---

## Key Innovation

Unlike traditional filters, our system:

- Simulates how users perceive color
- Calculates lost color information
- Reinjects that information using Daltonization
- Enhances perception in real-time

---
## 🔬 How It Works

### Pipeline
Webcam Frame
     ↓
Convert BGR → RGB
     ↓
Normalize (0–1)
     ↓
Simulate Color Blindness (CVD)
     ↓
Compute Color Loss (Error)
     ↓
Apply Daltonization Correction
     ↓
Display Corrected Output
     ↓
AI Caption Generation (BLIP)


### Formula
error = original - simulated
corrected = original + 0.7 * error


---

## Features

- Protanopia / Deuteranopia / Tritanopia modes
- Severity slider (adaptive correction)
- Real-time webcam processing (FPS optimized)
- Image upload support
- Ishihara-based detection
- AI-generated scene descriptions 🧠
- Live assistive feedback

---

## Run Locally

```bash
git clone https://github.com/Vithika2005/colorblindassist.git 
cd colorblind-assistant
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

## Architecture

<img src="https://raw.githubusercontent.com/Vithika2005/colorblindassist/main/final_app/assets/architecture.png" width="800"/>

## Demo

<img src="https://raw.githubusercontent.com/Vithika2005/colorblindassist/main/final_app/assets/demo.gif" width="800"/>

Project Evolution
- Step 1: Basic Daltonization
Simple correction logic
Limited to single deficiency
- Step 2: Colorspacious Integration
Accurate perceptual simulation
Support for all CVD types
- Final System: Real-Time Assistant
Streamlit UI
Ishihara detection
Real-time processing
Severity tuning
- Final Upgrade: AI Vision (VLM)
BLIP model integration
Scene understanding
Assistive description for users


Impact
This tool can:
- Improve accessibility for colorblind users
- Help designers build inclusive interfaces
- Assist in education & awareness
- Support healthcare screening

Future Scope
- Mobile app (real-world deployment)
- Browser extension
- Object detection + highlighting
- Voice-based assistance
- Personalized adaptive models
