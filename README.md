# Daltonization Assistant

A real-time computer vision tool that helps color-blind users perceive 
colors more clearly.

This project captures live video from the webcam, simulates different 
types of color blindness, and applies daltonization algorithms to enhance 
color perception.

## Features

* Real-time webcam processing
* Color blindness simulation
* Daltonization correction
* Adjustable severity slider
* Multiple modes:

  * Protanopia
  * Deuteranopia
  * Tritanopia

## Tech Stack

* Python
* OpenCV
* NumPy
* Colorspacious

## Controls

| Key | Function          |
| --- | ----------------- |
| 1   | Protanopia Mode   |
| 2   | Deuteranopia Mode |
| 3   | Tritanopia Mode   |
| q   | Quit Application  |

## Installation

Clone the repository:

```
git clone https://github.com/Vithika2005/colorblindassist.git 
cd daltonization-assistant
```

Create virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the program:

```
python daltonization.py
```

## Project Structure

```
daltonization-assistant
│
├── daltonization.py
├── requirements.txt
├── README.md
└── venv/
```

## Future Improvements

* Three-panel visualization (Original | Simulated | Daltonized)
* Mobile camera support
* Streamlit web interface
* Real-time performance optimization

