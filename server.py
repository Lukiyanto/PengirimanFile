import socket
import os

def start_server(host='127.0.0.1', port=5001, save_path='received_file.txt'):
    # Membuat socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Server listening on {host}:{port}')

    while True:
        conn, addr = server_socket.accept()
        print(f'Connection from {addr}')
        
        with open(save_path, 'wb') as file:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                file.write(data)

        print(f'File received and saved as {save_path}')
        conn.close()

if __name__ == '__main__':
    start_server()
