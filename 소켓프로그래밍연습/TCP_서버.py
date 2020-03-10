#라이브러리임포트(socket)
import socket

#소켓생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binding
server_socket.bind(('127.0.0.1', 9999))

#클라이언트접속대기
server_socket.listen()

#클라이언트접속시,해당클라이언트를위한소켓생성
client_socket, addr = server_socket.accept()
client_socket
addr

#클라이언트로부터데이터수신 / recv(한번에수신할수있는최대데이터사이즈)
data = client_socket.recv(1024)
data
data.decode('utf-8')

#클라이언트에데이터송신
client_socket.sendall(data)

print(data)
#소켓닫기
client_socket.close()
server_socket.close()
