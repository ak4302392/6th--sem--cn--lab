
import socket
# getting the server address
server_add=('localhost',9999)
# creating the socket instance for the client
client=socket.socket()
# connecting with the server
client.connect(server_add)
# getting the name at client side
name=input(str("Enter your name : "))

print("Connection established ")
# sending the name of the client to the server
client.sendall(name.encode())
# getting the name of the server
sender_name=client.recv(1000).decode()


print("Hi, ", name, ", Welcome to the chat room!")


while True:
    # message to be sent
    message_sent=input(str("You : "))
    # sending the message to the server
    client.sendall(bytes(message_sent.encode()))
    # message recieved from server
    message_received=client.recv(1000).decode()
    # exiting the chat room 
    if(str(message_received)=="exit"):
        print("Exiting the chat room....")
        # here if we get exit from the server side ,
        # client also send the 'exit' to server side
        client.sendall(bytes("exit".encode()))
        break
    # printing the message recieved
    print(sender_name," : ",message_received)
# closing the client instance
client.close()