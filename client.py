import socket
import os

def send_file(host='127.0.0.1', port=5001, file_path='file_to_send.txt'):
    if not os.path.isfile(file_path):
        print(f'File {file_path} does not exist')
        return
    
    # Membuat socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f'Connected to server at {host}:{port}')

    with open(file_path, 'rb') as file:
        while (chunk := file.read(1024)):
            client_socket.sendall(chunk)

    print(f'File {file_path} sent successfully')
    client_socket.close()

if __name__ == '__main__':
    send_file()
