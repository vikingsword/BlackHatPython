import socket
import threading


def handle_client(client_socket):
    while True:
        # 接收客户端消息
        data = client_socket.recv(1024)
        if not data:
            break

        message = data.decode()
        print("收到客户端消息:", message)

        # 发送回复给客户端
        reply = "收到你的消息: " + message
        client_socket.send(reply.encode())

    # 关闭客户端连接
    client_socket.close()


def start_server():
    # 创建TCP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = "127.0.0.1"  # 服务端IP地址
    server_port = 8888  # 服务端端口号

    # 绑定地址和端口
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)  # 最大连接数

    print("服务端启动，等待客户端连接...")

    while True:
        # 接受客户端连接
        client_socket, client_address = server_socket.accept()
        print("客户端连接：", client_address)

        # 创建线程处理客户端
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


start_server()
