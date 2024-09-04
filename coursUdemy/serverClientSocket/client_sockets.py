import socket
import time

# Network settings
HOST_IP = "127.0.0.1"
HOST_PORT = 32000
SLEEP_DELAY = 2
MAX_DATA_SIZE = 1024
connection_retry = 10


while connection_retry > 0:
    try:
        s = socket.socket() # Socket has to be recreated after each attempt
        print(f"Connecting to : {HOST_IP} on port {HOST_PORT}")
        s.connect((HOST_IP, HOST_PORT))
        
    except ConnectionRefusedError:
        print("Error : server is not responding")
        time.sleep(SLEEP_DELAY)
        connection_retry -= 1
    else:
        print("Ok, now connected\n")
        break

# Data receive
result = s.recv(MAX_DATA_SIZE)

if result:
    print("Data received :", result.decode())
else:
    print("No data sent by server")

s.close()
