
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("10.62.0.213",8000))
sock.send("hi")
