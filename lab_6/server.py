import socket
# the address of the server
server_add=('localhost',9999)
# creating an instance of the server for UDP
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# binding the address to the server instance
server.bind(server_add)


while True:
    # data received from client and the add of the client
    data,add=server.recvfrom(1000)
    # printing the message recived from the client
    print("Message recieved from [Client] : ",str(data.decode()))
    # the message to be sent to the client
    message=input("Enter the message you want to send to the client: ")
    # sending message to the client
    server.sendto(bytes(message.encode()),add)
# finally closing the instance of the server
server.close()
