import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_adress='localhost'
port=6666
server_socket.bind((ip_adress,port))
server_socket.setblocking(False)
server_socket.listen()
while True:
    time.sleep(0.5)
    try:
        text=server_socket.accept()
        print(text)
    except BlockingIOError:
        print("waiting")
        pass
