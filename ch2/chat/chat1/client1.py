import socket
import time

target_host = "127.0.0.1"
target_port = 2222

client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client1.connect((target_host, target_port))

while True:
    message = input('input: ')
    print(message)
    # confer str to byte
    client1.send(message.encode("utf-8"))
    time.sleep(1)
