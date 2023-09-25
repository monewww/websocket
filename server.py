import socket
import pickle

from testclass import A

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.92.4"
port = 12345
server.bind((host, port))
server.listen(5)
print("Server is listening for connections...")
client, addr = server.accept()
print("Client connected from", addr)
data = client.recv(1024)
a = pickle.loads(data)
if not isinstance(a, A):
    raise TypeError("Received object is not of type A")
print("Client data was received successfully")
for t in a.b:
    print(t.a)
client.close()
server.close()
