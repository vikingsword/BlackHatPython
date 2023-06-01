import socket

target_host = "127.0.0.1"
target_port = 2233

client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client1.connect((target_host, target_port))

while True:
    message = input('input: ')
    # confer str to byte
    client1.send(message.encode("utf-8"))
