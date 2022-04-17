
import socket
# creating an instance of client for UDP
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# the address of he server
server_add=('localhost',9999)
while True:
    # the message to send to the server
    message_to_send=input("Enter the message you want to send to the server: ")
    # sending message to the server
    client.sendto(bytes(message_to_send.encode()),server_add)
    # message recieved from server
    message_recieved,add=client.recvfrom(1000)
    # printing the message received from sever
    print("Message from Server : ",str(message_recieved.decode()))

#finally closing the client instance
client.close()
