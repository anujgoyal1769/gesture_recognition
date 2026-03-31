# 🖐 Hand Gesture Recognizer

A real-time hand gesture recognition system built using **Python**, **OpenCV**, and **MediaPipe**. The application uses your webcam to detect and classify hand gestures instantly — no external hardware needed.

---

## 📸 What It Does

- Detects your hand in real-time using your webcam
- Tracks 21 hand landmarks using Google's MediaPipe
- Recognizes 10 common gestures including:
  - ✊ Fist
  - 🖐 Open Hand
  - ☝ Point Up
  - ✌ Peace / Victory
  - 👍 Thumbs Up
  - 🤙 Call Me
  - and more...
- Displays the recognized gesture name on screen
- Shows live FPS counter and number of hands detected

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Core language |
| OpenCV | Webcam capture & image display |
| MediaPipe | Hand landmark detection |
| NumPy | Numerical operations |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/hand-gesture-recognizer.git
cd hand-gesture-recognizer
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Project
```bash
python gesture_recognition.py
```

---

## 🎮 How to Use

1. Run the script — your webcam will open automatically
2. Hold your hand up in front of the camera
3. The gesture name will appear on screen in real time
4. Try different hand positions to see different gestures recognized
5. Press **`Q`** to quit the application

---

## 📁 Project Structure

```
hand-gesture-recognizer/
│
├── gesture_recognition.py   # Main application script
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 💡 How It Works

1. **Capture** — OpenCV reads frames from the webcam
2. **Detect** — MediaPipe detects 21 landmarks on the hand
3. **Analyze** — Each finger's tip vs. joint position is compared to check if it's up or down
4. **Classify** — The combination of 5 finger states (each 0 or 1) is matched to a gesture dictionary
5. **Display** — The gesture name is overlaid on the video feed

---

## 🔮 Future Improvements

- Add support for dynamic gestures (waving, swiping)
- Control PC volume or media using gestures
- Train a custom ML model for more complex gestures
- Add a gesture history log / export feature

---

## 👤 Author

**[Your Name]**  
[Your College / Course Name]  
Computer Vision Project — BYOP Submission

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
