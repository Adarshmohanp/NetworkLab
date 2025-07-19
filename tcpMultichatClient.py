import socket
import threading

def receive(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print(msg)
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 65432))

    msg = client.recv(1024).decode()
    if msg == "NICKNAME":
        nickname = input("Enter your nickname: ")
        client.send(nickname.encode())

    threading.Thread(target=receive, args=(client,), daemon=True).start()

    while True:
        message = input()
        client.send(message.encode())

if __name__ == "__main__":
    main()
# This code implements a simple TCP client that connects to a server, allows the user to send messages,
# and displays messages received from the server. It also handles nickname registration.