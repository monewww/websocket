import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.92.4"
port = 12345
server.bind((host, port))
server.listen(5)
print("Server is listening for connections...")
client, addr = server.accept()
print("Client connected from", addr)
data = client.recv(1024)
print("Client sent:", data.decode())
client.close()
server.close()
