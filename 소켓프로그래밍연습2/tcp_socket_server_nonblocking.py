import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 9999))
server_socket.listen()
client_socket, addr = server_socket.accept()
print('Connected by', addr)
client_socket.setblocking(0)

while True:
    try:
        data = client_socket.recv(4096)
        print('test')
        if not data:
            break
        print(data.decode('utf-8'))
    except:
        break
client_socket.close()
server_socket.close()
