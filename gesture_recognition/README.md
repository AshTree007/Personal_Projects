# Gesture Recognition System

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-00FF00?style=for-the-badge&logo=mediapipe&logoColor=white)

This project implements a real-time hand gesture recognition system utilizing `mediapipe` for hand tracking and a `PyTorch` neural network for gesture classification.

---

## Features

*   **Real-time Gesture Recognition:** Detects and classifies hand gestures from a live webcam feed.
*   **Hand Tracking:** Leverages `mediapipe` to accurately detect and track 3D hand landmarks.
*   **PyTorch Model:** Employs a custom-built sequential neural network in PyTorch for robust gesture classification.
*   **Model Training:** Includes a dedicated script (`model_trainer.py`) for training the gesture recognition model with custom datasets.

---

## Getting Started

### Prerequisites

*   Python 3.x
*   Webcam

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/Personal_projects.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd Personal_projects/gesture_recognition
    ```
3.  Install the required Python libraries:
    ```bash
    pip install -r reqs.txt
    ```

### Usage

To operate the real-time gesture recognition system, execute the main application file:

1.  **Run the Application:** From the `gesture_recognition` directory, execute the `video_stream.py` script:
    ```bash
    python video_stream.py
    ```
2.  **Observe Output:** A window displaying your webcam feed will open. The system will continuously analyze your hand movements. Recognized gestures will be printed to the console in real-time.
3.  **Perform Gestures:** Position your hand clearly in front of the webcam and perform the gestures that the model has been trained to recognize. The console output will indicate the detected gesture.

---

## How it Works

1.  **Hand Detection:** The `hand_detection.py` module processes video frames using the `mediapipe` library to extract 3D coordinates of hand landmarks.
2.  **Gesture Prediction:** The extracted landmark data is fed into the pre-trained PyTorch model within `gesture_detection.py`, which then predicts the corresponding gesture.
3.  **Video Stream:** The `video_stream.py` script orchestrates the capture of webcam input, passes frames to the hand detection and gesture prediction modules, and visualizes the output.

---

## Training a Custom Model

To train the model with your own gesture data:

1.  **Data Preparation:** Create a `training_data.csv` file. This file should contain landmark data for each gesture you wish to train. Each row should represent a single gesture instance with its corresponding landmark coordinates and a label.
2.  **Model Training Execution:** From the `gesture_recognition` directory, execute the `model_trainer.py` script:
    ```bash
    python model_trainer.py
    ```
3.  **Output:** The script will save the trained model as `model.pth` and the label encoder as `label_encoder.pth` in the project directory.

---

## Project Structure

```
gesture_recognition/
├───README.md
├───gesture_detection.py
├───hand_detection.py
├───model_trainer.py
├───reqs.txt
├───training_data.csv
└───video_stream.py
```

---

## Technologies Used

*   Python
*   PyTorch
*   MediaPipe
*   OpenCV
*   Scikit-learn

---