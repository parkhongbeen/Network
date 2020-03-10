import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = ('127.0.0.1', 9999)
data = 'Hello!? This is UDP'
client_socket.sendto(data.encode(),dest)
client_socket.close()

