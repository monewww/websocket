import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.92.4"
port = 12345
client.connect((host, port))
client.send("Hello Server!".encode())