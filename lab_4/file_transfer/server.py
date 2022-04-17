
import socket

server_add=('localhost',9999)


print("[STARTING] Server is starting.")
#  Staring a TCP socket. 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#  Bind the IP and PORT to the server. 
server.bind(server_add)

#  Server is listening, i.e., server is now waiting for the client to connected. 
server.listen()
print("[LISTENING] Server is listening.")

# while True:
#  Server has accepted the connection from the client. 
conn, server_add = server.accept()
print(f"[NEW CONNECTION] {server_add} connected.")

#  Receiving the filename from the client. 
filename = conn.recv(1000).decode()
print(f"[RECV] Receiving the filename.")
file = open(filename, "w")
conn.send("Filename received.".encode())

#  Receiving the file data from the client. 
data = conn.recv(1000).decode()
print(f"[RECV] Receiving the file data.")
file.write(data)
conn.send("File data received".encode())

#  Closing the file. 
file.close()

#  Closing the connection from the client. 
conn.close()
print(f"[DISCONNECTED] {server_add} disconnected.")

