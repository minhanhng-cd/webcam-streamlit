import cv2
import numpy as np
import streamlit as st

st.title("Show Webcam on Streamlit")

st.header("Parameters")

with st.echo():
    # Change frame size
    WIDTH = 600
    HEIGHT = 300

st.header("Webcam")
with st.echo():

    # Toggle Webcam
    if st.sidebar.checkbox("Open Webcam"):

        # Start webcam
        cap = cv2.VideoCapture(0)

        # Display on streamlit
        # Initialize display
        viewer = st.image(np.zeros((WIDTH, HEIGHT)))


        while True:
            
            # Read frame
            _, frame = cap.read()

            # Convert to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Resize
            frame = cv2.resize(frame, (WIDTH, HEIGHT))
            
            # Update display
            viewer.image(frame)