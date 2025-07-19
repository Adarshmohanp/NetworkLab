import socket

def start_client(host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server {host}:{port}")

    try:
        while True:
            msg = input("You: ")
            if msg.lower() == 'exit':
                print("Closing connection.")
                break
            client_socket.sendall(msg.encode())

            data = client_socket.recv(1024).decode()
            if not data:
                print("Connection closed by server.")
                break
            print(f"Server: {data}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()