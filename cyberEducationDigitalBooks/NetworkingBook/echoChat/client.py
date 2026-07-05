import socket

SERVER_ADDRESS = ("127.0.0.1", 8081)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(SERVER_ADDRESS)
print(client_socket.recv(2).decode())

while True:

    print("enter the data you want to send to the server: ")
    data_to_send = input()
    client_socket.send(data_to_send.encode())
    data_received = client_socket.recv(2).decode()
    print("Server:", data_received)

    if data_received == "end of conversation.":
        break
client_socket.close()
