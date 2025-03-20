import cv2
import mediapipe as mp
import numpy as np
import socket
import os
import time

# ✅ Use the same file path
FILE_PATH = r"C:\Users\smrit\AppData\Local\Programs\Python\Python312\example.txt"
SERVER_IP = "192.168.90.144"  # Receiver's IP
PORT = 5001

# Swipe detection settings
SWIPE_THRESHOLD = 200  # Pixels moved to register a swipe
FRAME_HISTORY = 10  # Number of frames to track movement

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Function to send the file
def send_file():
    if not os.path.exists(FILE_PATH):
        print(f"File '{FILE_PATH}' not found! Please check the path.")
        return
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT))

    filename = os.path.basename(FILE_PATH)
    client_socket.send(filename.encode())

    with open(FILE_PATH, "rb") as f:
        data = f.read(1024)
        while data:
            client_socket.send(data)
            data = f.read(1024)

    print(f"File '{filename}' sent successfully!")
    client_socket.close()

# Hand swipe detection
def detect_swipe():
    cap = cv2.VideoCapture(0)
    x_positions = []  # Store X positions of the hand

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)  # Mirror the image
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Track index finger tip (landmark 8)
                index_x = int(hand_landmarks.landmark[8].x * frame.shape[1])

                # Store movement history
                x_positions.append(index_x)
                if len(x_positions) > FRAME_HISTORY:
                    x_positions.pop(0)

                # Draw landmarks on the hand
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Check for swipe
                if len(x_positions) >= FRAME_HISTORY:
                    start_x, end_x = x_positions[0], x_positions[-1]

                    if abs(end_x - start_x) > SWIPE_THRESHOLD:
                        direction = "Right" if end_x > start_x else "Left"
                        print(f"Swipe {direction} detected! Sending file...")
                        time.sleep(1)
                        cap.release()
                        cv2.destroyAllWindows()
                        send_file()
                        return

        cv2.imshow("Hand Swipe Detector", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run swipe detection
detect_swipe()

