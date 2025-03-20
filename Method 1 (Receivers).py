import socket
import os

PORT = 5001
SAVE_DIR = r"received_files"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(1)

print(f"Receiver is listening on port {PORT}...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    try:
        filename = conn.recv(1024).decode()
        if not filename:
            continue

        file_path = os.path.join(SAVE_DIR, filename)

        with open(file_path, "wb") as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)

        print(f"File '{filename}' received and saved at '{file_path}'")

    except Exception as e:
        print(f"Error: {e}")
        break

print("Receiver stopped listening.")
conn.close()
server_socket.close()
