import socket

client_socket = socket.socket()

server_address = ('127.0.0.1', 8820)

# this line will create the pipe, so I can communicate with the server.
client_socket.connect(server_address)

client_socket.send("Dvir".encode())

# byte is 8 bits. with one byte you can represent a letter. this command will enable 1024 bytes, which is 1024 letters.
data_received_from_server = client_socket.recv(1024)

if data_received_from_server == "":
    print("connection failed.")
else:
    print(f"the data you got from the server is: {data_received_from_server.decode()}")

client_socket.close()
