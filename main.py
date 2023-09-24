import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_adress='192.168.0.205'
port=6666
server_socket.bind((ip_adress,port))
server_socket.setblocking(False)
server_socket.listen()
while True:
    try:
        text=server_socket.accept()
        print(text)
    except BlockingIOError:
        pass
