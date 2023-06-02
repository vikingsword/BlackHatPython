import socket

def start_client():
    target_host = "127.0.0.1"
    target_port = 2233

    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client1.connect((target_host, target_port))

    while True:
        message = input('input: ')
        # confer str to byte
        client1.send(message.encode())
        # reply = client1.recv(1024)
        # print("收到服务端回复：", reply.decode())


start_client()