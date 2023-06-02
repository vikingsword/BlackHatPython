import socket
import threading

ip = "127.0.0.1"
port = 1111
# todo bug

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print(f'[*] Listening on {ip},{port}')

    while True:
        client, addr = server.accept()
        print(f'[*] from {addr[0]}:{addr[1]}')
        client_handle = threading.Thread(target=handle_client, args=(client,))
        client_handle.start()


def handle_client(client_socket):
    # while True:
    #     with client_socket as sock:
    #         request = sock.recv(1024)
    #         print(f'[*]  {request.decode("utf-8")}')
    # client_socket.close()
    while True:
        # 接收客户端消息
        data = client_socket.recv(1024)
        if not data:
            break

        message = data.decode()
        print("received message: ", message)

        # 发送回复给客户端
        # reply = "收到你的消息: " + message
        # client_socket.send(reply.encode())
    # 关闭客户端连接
    # client_socket.close()

if __name__ == '__main__':
    main()
