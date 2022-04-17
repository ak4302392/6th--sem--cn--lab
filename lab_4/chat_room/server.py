
import socket
import time
# the server address with port and localhost
server_addr=('localhost',9999)
# creating an instance of the server socket
server=socket.socket()
# binding the ip address and port number
server.bind(server_addr)

# taking input the name at the server side
name=input(str("Enter your name : "))
# time.sleep(1)
# listening for the client side
server.listen()

print("waiting for connection to be established ")
# connecting with the client and getting the address of client
client,client_add=server.accept()

print("Connection Established successfully..")
# sending the name of the server to the client
client.sendall(name.encode())
# getting the name of the client 
sender_name=client.recv(1000).decode()

print("Hi, ",name, ", Welcome to the chat room")


while True:
    # message recieved from the client
    message_recieved=client.recv(1000).decode()
    # exiting the chat room 
    if(str(message_recieved)=="exit"):
        print("Exiting the chat room....")
        # here if we get exit from the client side ,
        # server also send the 'exit' to client side
        client.sendall(bytes("exit".encode()))
        break
    # printing the message recieved
    print(sender_name," : ",message_recieved)
    # getting input the message to sent
    message_sent=input(str(f"You : " ))
    # sending the message to the client
    client.sendall(bytes(message_sent.encode()))
#finally closing the server
server.close()
