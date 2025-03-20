import http.server
import socketserver
import os
import socket

PORT = 8000
FILE_PATH = r"C:\Users\smrit\AppData\Local\Programs\Python\Python312\example.txt"
DIRECTORY = os.path.dirname(FILE_PATH)

if not os.path.exists(FILE_PATH):
    print(f"Error: File '{FILE_PATH}' not found!")
    exit(1)

os.chdir(DIRECTORY)

# Get local IP dynamically
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

local_ip = get_local_ip()

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at http://{local_ip}:{PORT}")
    print(f"Download your file at: http://{local_ip}:{PORT}/{os.path.basename(FILE_PATH)}")
    httpd.serve_forever()
