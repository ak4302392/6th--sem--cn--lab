from email import message
from http import client
from pydoc import cli
import socket
# the address of the server socket
server_address = ('localhost', 9999)
# creating an instance of socket for client connection
client = socket.socket()
# connecting the client with server
client.connect(server_address)

while 1:
    # taking message as input to send to the server
    print("Enter the message you want to send to the server ")
    message = input()
    # exiting the loop
    if(str(message)=="exit"):
        client.sendall(bytes(message.encode()))
        break
    print('sending..........', message)
    # sending the message to the server
    client.sendall(bytes(message.encode()))
    # printing the original data
    print('Original Data: ', message)
    # receiving the data from the server
    data = client.recv(1000).decode()
    # printing the data recieved from the server as echo
    print('ECHO Data......  ', data)
# finally closing the client socket
client.close()



