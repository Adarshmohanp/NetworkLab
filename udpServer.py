import socket
import threading


def main():
    server_ip = "0.0.0.0"  
    server_port = 5005

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((server_ip, server_port))

    threading.Thread(target=listen, args=(sock,), daemon=True).start()

    print(f"Server listening on port {server_port}")

    while True:
        msg = input("Server: ")
        if msg.lower() == "exit":
            break
        if 'last_client' in globals():
            sock.sendto(msg.encode(), last_client)
        else:
            print("No client has sent message yet.")

    sock.close()

if __name__ == "__main__":
    last_client = None

    def listen(sock):
        global last_client
        while True:
            data, addr = sock.recvfrom(1024)
            last_client = addr
            print(f"\nClient ({addr}): {data.decode()}\nServer: ", end='', flush=True)

    main()