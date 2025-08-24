🖐️ Hand Finger Counter App

An AI-powered Streamlit web app that attempts to count the number of fingers raised from an uploaded hand image.
Built using YOLOv8 for object detection and Streamlit for an interactive UI.

⚠️ Note: The current YOLOv8 model (yolov8n.pt) is not trained on hands/fingers.
For accurate finger counting, you’ll need to integrate Mediapipe Hands or train a custom YOLO model specifically for hand landmarks.

🚀 Features

Upload an image of your left hand.

AI model analyzes the image and tries to estimate fingers raised.

Displays detection bounding boxes and a finger count result.

Simple, lightweight, and easy to deploy on Streamlit Cloud or locally.

🛠️ Tech Stack

Python 3.8+

Streamlit
 → Web app framework

Ultralytics YOLOv8
 → Object detection

Pillow (PIL)
 → Image processing

NumPy
 → Array operations

PyTorch
 → Deep learning backend
