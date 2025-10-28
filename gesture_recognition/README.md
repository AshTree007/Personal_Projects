# Gesture Recognition

This project is a real-time hand gesture recognition system that uses `mediapipe` for hand tracking and a `PyTorch` neural network for gesture classification.

## Features

*   **Real-time Gesture Recognition:** Recognizes hand gestures from a live video stream from your webcam.
*   **Hand Tracking:** Uses `mediapipe` to detect and track hand landmarks.
*   **PyTorch Model:** A sequential neural network built with PyTorch is used to classify the gestures based on the hand landmark data.
*   **Model Training:** Includes a script (`model_trainer.py`) to train the gesture recognition model on your own custom data.

## Setup

1.  **Install Dependencies:** Install the required Python libraries using the `reqs.txt` file:
    ```bash
    pip install -r reqs.txt
    ```

2.  **Run the Application:** To start the gesture recognition, run the `video_stream.py` script:
    ```bash
    python video_stream.py
    ```
    This will open a window showing your webcam feed with the recognized gesture printed to the console.

## How it Works

1.  **Hand Detection:** The `hand_detection.py` script uses the `mediapipe` library to process the video frame and extract the 3D coordinates of the hand landmarks.

2.  **Gesture Prediction:** The extracted landmark data is passed to the pre-trained PyTorch model in `gesture_detection.py`, which then predicts the gesture.

3.  **Video Stream:** The `video_stream.py` script captures the video feed from the webcam, passes each frame to the hand detection and gesture prediction modules, and displays the output.

## Training a Custom Model

To train the model with your own gestures, you will need to create a `training_data.csv` file with the landmark data for each gesture. The `model_trainer.py` script can then be used to train a new model. The script will save the trained model as `model.pth` and the label encoder as `label_encoder.pth`.

## Files

*   `video_stream.py`: The main script to run the gesture recognition application.
*   `hand_detection.py`: Handles the hand tracking and landmark extraction.
*   `gesture_detection.py`: Contains the PyTorch model and the prediction logic.
*   `model_trainer.py`: Script for training the gesture recognition model.
*   `model.pth`: The pre-trained PyTorch model.
*   `label_encoder.pth`: The saved label encoder for the gesture classes.
*   `reqs.txt`: A list of the required Python libraries.
