import socket

# Network settings
HOST_IP = "127.0.0.1"
HOST_PORT = 32000

# create socket

s = socket.socket()

# allow socket reuse
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# using localhost
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Waiting connection on : {HOST_PORT}")
connection_socket, client_adress = s.accept()
print(f"Established connection from : {client_adress}, infos : {connection_socket}")

motd = "Hello ! (Connected to server xxx)"

connection_socket.sendall(motd.encode())

s.close()