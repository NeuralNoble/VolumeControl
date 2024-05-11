# Hand Gesture Volume Control

This Python project allows you to control the volume of your system using hand gestures captured from a webcam. It uses the OpenCV library for computer vision to detect hand landmarks and calculate the distance between two specific landmarks to determine the hand gesture.

## How It Works

1. **Hand Tracking:** The program uses the HandTrackingModule to detect and track landmarks (specific points) on your hand, such as the tips of your fingers.

2. **Volume Calculation:** It calculates the length between two landmarks (usually the tip of the thumb and the tip of the index finger) to determine the hand gesture. Moving your hand closer reduces the volume, while moving it further away increases the volume.

3. **Volume Adjustment:** Based on the calculated length, the program interpolates the hand gesture to a volume level between 0 and 100 and sets the system's output volume accordingly using AppleScript.

## How to Use

1. **Requirements:** Make sure you have Python 3.x installed on your system along with the required libraries: OpenCV and NumPy , Mediapipe , Osascript.

2. **Clone the Repository:** Clone this repository to your local machine:

   ```bash
   git clone https://github.com/NeuralNoble/VolumeControl
```
