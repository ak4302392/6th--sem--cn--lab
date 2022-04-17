import socket
from time import time
# the server address
server_add=('localhost',9999)
# creating the UDP instance
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# binding the server with the address
server.bind(server_add)
# taking input the name of the server end
name=str(input("Enter your name : "))


while True:
    # data and add of the client
    data,add=server.recvfrom(1000)
    # printing the message of the client
    print("[Client] : ",str(data.decode()))
    # taking input of the message to send to the client
    message=input(name+" : ")
    # sending the message to the client
    server.sendto(bytes(message.encode()),add)

#finally closing the socket instance
server.close()