import socket

with socket.socket() as client_socket:

    server_address = ('127.0.0.1', 8820)

    # this line will create the pipe, so I can communicate with the server.
    client_socket.connect(server_address)

    while True:

        print(
            "\nOptions: [RAND] random number | [WHORU] server name | [EXIT] disconnect"
        )
        data_to_send = input("Enter command: ")

        if not data_to_send.strip():
            continue

        client_socket.send(data_to_send.encode())

        # byte is 8 bits. with one byte you can represent a letter. this command will enable 1024 bytes, which is 1024 letters.
        data_received_from_server = client_socket.recv(1024).decode()
        if not data_received_from_server:
            print("connection failed.")
            break
        elif data_received_from_server != "exited":
            print(f"the data you got from the server is: {data_received_from_server}")
        else:
            print("exited successfully from the connection. have a nice day!")
            break
