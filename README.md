![image](https://github.com/user-attachments/assets/b116bc63-7be6-4fba-98d3-8d50a4643b3c)


S.W.I.P.E (Seamless Wireless Interaction for Packet Exchange) is a Python-based application that enables users to send files over a network using hand swipe gestures detected via a webcam or through an HTTP file server. It leverages OpenCV, MediaPipe, and Socket Programming for gesture-based transfer and also provides an HTTP-based file-sharing option.

🔹 Features


✅ Detects hand swipe gestures using a webcam for file transfer

✅ Sends files to a predefined IP over a network

✅ Hosts a local HTTP server for easy file downloads

✅ Real-time tracking with OpenCV and MediaPipe

✅ Dynamic IP detection for HTTP file sharing

🔹 Technologies Used

Python 3.x

OpenCV (Computer Vision)

MediaPipe (Hand tracking)

Socket Programming (Network communication)

HTTP Server (For browser-based file access)

🔹 Installation

Clone the repository:

Navigate to the project directory:

Install dependencies:

🔹 Usage

📌 Method 1: Hand Swipe File Transfer

Run the script and swipe right to send the file:

Press 'q' to exit.

📌 Method 2: HTTP File Server

Start the HTTP server to allow file downloads:

The file will be accessible at:http://192.168.0.0:port/filename.extension
