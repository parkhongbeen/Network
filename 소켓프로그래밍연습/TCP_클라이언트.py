import socket
#socket생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#서버접속
client_socket.connect(('127.0.0.1', 9999))

#서버에데이터송신
data = 'hello!? This is TPC!'
client_socket.sendall(data.encode())

#서버로부터데이터수신
client_socket.recv(1024)

#소켓닫기
client_socket.close()

