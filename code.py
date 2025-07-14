import streamlit as st
from PIL import Image
import numpy as np
import torch
from ultralytics import YOLO


# Load a pre-trained YOLOv8 model (optional custom hand detection model)
model = YOLO("yolov8n.pt")  # Use a model trained on hands if available

st.title("🖐️ Hand Finger Counter App")

uploaded_file = st.file_uploader("Upload an image of your left hand", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Analyzing the hand..."):
        # Convert image to numpy array
        img_array = np.array(image)

        # Run detection (NOTE: yolov8n.pt is not trained on hands, you need a custom model or openpose)
        results = model(img_array)

        # Show the result
        boxes = results[0].boxes
        count = len(boxes)  # Placeholder for "fingers"

        # Placeholder logic (real finger detection would need a hand landmark model)
        st.success(f"Estimated Fingers Raised: {count if count <= 5 else 'Unknown'}")

        st.write("⚠️ Note: This model isn't trained on fingers. For accurate results, integrate with a finger-counting model like Mediapipe or a YOLO custom model.")


