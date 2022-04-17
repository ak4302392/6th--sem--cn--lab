import socket
server_add=('localhost',9999)

#  Staring a TCP socket. 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#  Connecting to the server. 
client.connect(server_add)

#  Opening and reading the file data. 
file = open("data/yt.txt", "r")
data = file.read()

#  Sending the filename to the server. 
client.send("yt.txt".encode())
msg = client.recv(1000).decode()
print(f"[SERVER]: {msg}")

#  Sending the file data to the server. 
client.send(data.encode())
msg = client.recv(1000).decode()
print(f"[SERVER]: {msg}")

#  Closing the file. 
file.close()

#  Closing the connection from the server. 
client.close()

