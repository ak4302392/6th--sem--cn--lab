
import socket
# creating the server socket instance
server = socket.socket()
# the server address with the port number
server_address = ('localhost', 9999)
# binding the server ip with the port number
server.bind(server_address)
# listening for the client request 3 specify the number of connections
server.listen()
# waiting for the connection to be established
print('waiting for connection')

# accepting the client connection request
# and getting the client details
connection, client_address = server.accept()
# printing the client address
print('connection established', connection, client_address)
while 1:

    # getting the data sent by the client
    data = connection.recv(1000).decode()
    # exiting the loop
    if(str(data)=="exit"):
        break
    # printing the data recieved
    print('Recieved data: ', data)
    # sending the same data to the client
    connection.sendall(bytes(data.encode()))
# finally closing the connection
server.close()
