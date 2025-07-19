import socket
import threading

def listen(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"\nServer: {data.decode()}\nYou: ", end='', flush=True)

def main():
    server_ip = input("Enter server IP: ")
    server_port = int(input("Enter server port: "))

    local_port = 0  # OS chooses port automatically
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", local_port))

    threading.Thread(target=listen, args=(sock,), daemon=True).start()

    print(f"Sending messages to {server_ip}:{server_port}. Type 'exit' to quit.")

    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            break
        sock.sendto(msg.encode(), (server_ip, server_port))

    sock.close()

if __name__ == "__main__":
    main()