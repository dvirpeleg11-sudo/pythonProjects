import socket
import random

# Using 'with' ensures sockets close automatically on exit or error
with socket.socket() as server_socket:
    # Allow instant restart of the server on the same port
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('0.0.0.0', 8820)
    server_name = "dvir server"

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

    with client_socket:

        while True:

            data = client_socket.recv(1024).decode()

            if not data:
                print("Client disconnected unexpectedly.")
                break

            data = data.strip().lower()
            print("Client sent: " + data)

            if data == "whoru":
                client_socket.send(server_name.encode())
            elif data == "rand":
                random_number = random.randint(1, 10)
                client_socket.send(str(random_number).encode())
            elif data == "exit":
                client_socket.send("exited".encode())
                break
            else:
                client_socket.send("your message is not in the right protocol. please try again.".encode())
