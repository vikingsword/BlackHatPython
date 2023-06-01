import socket
import threading

ip = "127.0.0.1"
port = 2233
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
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*]  {request.decode("utf-8")}')



if __name__ == '__main__':
    main()
