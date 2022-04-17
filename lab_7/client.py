import socket
# creating an instance of the client UDP
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# the server address 
server_add=('localhost',9999)
# taking input the name of the user
name=str(input("Enter your name: "))


while True:
    # message to send to the server
    message_to_send=input(name+ " : ")
    # sending message to the server
    client.sendto(bytes(message_to_send.encode()),server_add)
    # recieving message from server
    message_recieved,add=client.recvfrom(1000)
    # printing the message recieved from the server
    print(f"[Server] : {str(message_recieved.decode())}")

# finally closing the socket instance
client.close()
