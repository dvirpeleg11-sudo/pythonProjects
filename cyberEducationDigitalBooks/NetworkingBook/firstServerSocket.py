import socket

server_address = ('0.0.0.0', 8820)
server_socket = socket.socket()

# taking the port 8820. the ip shows who can connect to us.
server_socket.bind(server_address)

# listen to connection, so we can help our clients. the default parameter is 0.
# the parameter decide how many sockets can wait in the queue without being accepted by the server.
# this is not a blocking method.
server_socket.listen()

print("Server is up and running")

# this is a blocking method.
(client_socket, client_address) = server_socket.accept()
print("Client connected")

data = client_socket.recv(1024).decode()
print("Client sent: " + data)

reply = "Hello " + data
client_socket.send(reply.encode())

client_socket.close()
# here we could decide to start a new conversation with another client or close our socket as we did in the next line.
server_socket.close()
