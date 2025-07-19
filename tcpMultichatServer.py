import socket
import threading

clients = {}

def handle_client(client_socket, nickname):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg:
                print(f"[{nickname}] {msg}")
        except:
            print(f"{nickname} disconnected.")
            clients.pop(nickname)
            client_socket.close()
            break

def server_send():
    while True:
        target = input("Enter nickname to reply: ")
        if target in clients:
            message = input(f"Enter message for {target}: ")
            clients[target].send(f"[Server]: {message}".encode())
        else:
            print("Nickname not found.")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 65432))
    server.listen()
    print("Server listening...")

    threading.Thread(target=server_send, daemon=True).start()

    while True:
        client_socket, addr = server.accept()
        client_socket.send("NICKNAME".encode())
        nickname = client_socket.recv(1024).decode()
        clients[nickname] = client_socket
        print(f"{nickname} connected from {addr}")

        thread = threading.Thread(target=handle_client, args=(client_socket, nickname))
        thread.start()

if __name__ == "__main__":
    main()
# This code implements a simple TCP server that handles multiple clients,
# allowing them to send and receive messages. It also allows the server to send messages to specific clients by nickname.