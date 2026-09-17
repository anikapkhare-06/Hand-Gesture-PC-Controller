🖐️ HAND GESTURE BASED PC CONTROLLER

A Computer Vision based system for controlling PC functions using hand gestures

Detect • Track • Recognize • Control

"Python" "OpenCV" "MediaPipe" "Computer Vision" "Hand Tracking"

---

📌 Overview

The Hand Gesture Based PC Controller is a Computer Vision project that enables users to interact with and control a computer using hand gestures.

The system uses a webcam to capture real-time hand movements and detects hand landmarks using a hand-tracking model. The detected hand information is processed to recognize gestures and perform corresponding PC control actions.

The project provides a touchless and interactive approach to Human-Computer Interaction (HCI).

---

✨ Features

Feature| Description
📷 Real-Time Camera Input| Captures live video through the webcam
🖐️ Hand Detection| Detects the user's hand in the camera frame
📍 Hand Landmark Tracking| Tracks important points of the hand
🤏 Gesture Recognition| Identifies predefined hand gestures
🖥️ PC Control| Uses recognized gestures to control PC functions
⚡ Real-Time Processing| Processes hand movements continuously
🎯 Touchless Interaction| Enables computer interaction without physical input devices

---

🏗️ System Architecture

          ┌─────────────────────┐
          │      Webcam         │
          └──────────┬──────────┘
                     ▼
          ┌─────────────────────┐
          │   Video Capture     │
          └──────────┬──────────┘
                     ▼
          ┌─────────────────────┐
          │   Hand Detection    │
          └──────────┬──────────┘
                     ▼
          ┌─────────────────────┐
          │ Hand Landmark       │
          │ Tracking            │
          └──────────┬──────────┘
                     ▼
          ┌─────────────────────┐
          │ Gesture Recognition │
          └──────────┬──────────┘
                     ▼
          ┌─────────────────────┐
          │   PC Controller     │
          └──────────┬──────────┘
                     ▼
          ┌─────────────────────┐
          │ Computer Interaction│
          └─────────────────────┘

---

🛠️ Tech Stack

Programming Language: Python

Computer Vision: OpenCV

Hand Tracking: MediaPipe Hand Landmarker

Model: "hand_landmarker.task"

Version Control: Git & GitHub

---

📂 Project Structure

HAND-GESTURE-BASED-PC-CONTROLLER/
│
├── main.py
├── hand_landmarker.task
├── README.md
└── .gitignore

File Description

File| Purpose
"main.py"| Main application containing the hand gesture detection and PC control logic
"hand_landmarker.task"| Hand Landmarker model used for hand detection and landmark tracking
"README.md"| Project documentation
".gitignore"| Specifies files ignored by Git

---

⚙️ Installation & Setup

1. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd HAND-GESTURE-BASED-PC-CONTROLLER

2. Install Required Libraries

Install the required Python packages:

pip install opencv-python mediapipe numpy

3. Check the Model File

Make sure the following file is present in the project directory:

hand_landmarker.task

---

▶️ Run the Project

Make sure your webcam is connected and accessible.

Run:

python main.py

The application will start the webcam and process hand movements in real time.

Perform the supported hand gestures in front of the camera to interact with the PC.

---

🖐️ How It Works

The system follows these basic steps:

1. The webcam captures live video frames.
2. OpenCV processes the camera input.
3. The Hand Landmarker model detects the hand.
4. Hand landmarks are extracted from the detected hand.
5. The program analyzes the landmark positions.
6. Predefined gestures are recognized.
7. The corresponding PC control action is triggered.

---

🎯 Applications

- 🖥️ Touchless PC control
- ♿ Accessibility and assistive interfaces
- 🎮 Human-Computer Interaction
- 🤖 Computer Vision applications
- 🏠 Smart interface systems
- 📚 Educational Computer Vision projects

---

🎯 Project Objectives

- Implement real-time hand detection using Computer Vision.
- Track hand landmarks using a hand-tracking model.
- Recognize predefined hand gestures.
- Use gestures for computer interaction.
- Develop a practical Human-Computer Interaction system.
- Explore touchless interaction technologies.

---

🚀 Future Improvements

- Add more hand gestures and PC commands.
- Improve gesture recognition accuracy.
- Add support for two-hand gestures.
- Add customizable user-defined gestures.
- Improve performance under different lighting conditions.
- Add voice and gesture control together.
- Develop a graphical interface for gesture configuration.

---

📸 Demo / Output

The system uses the webcam to detect the user's hand and recognize gestures in real time.

Screenshots and demonstration videos can be added here after testing the project.

---

👨‍💻 Author

[Anika Khare]

B.Tech — Computer Science & Engineering (AI & ML) 
VIT Bhopal University

---

🔗 Repository

View the project on GitHub.

Built as a Computer Vision project for learning, experimentation, and practical Human-Computer Interaction.

---

⭐ Project Highlights

Real-Time • Touchless • Computer Vision • Hand Tracking • Gesture Control
