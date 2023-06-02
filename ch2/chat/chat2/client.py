import socket

def start_client():
    # 创建TCP套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = "127.0.0.1"  # 服务端IP地址
    server_port = 8888         # 服务端端口号

    # 连接到服务端
    client_socket.connect((server_host, server_port))

    while True:
        # 输入消息
        message = input("请输入消息：")

        # 发送消息给服务端
        client_socket.send(message.encode())

        # 接收服务端回复
        reply = client_socket.recv(1024)
        print("收到服务端回复：", reply.decode())

    # 关闭连接
    client_socket.close()

start_client()
