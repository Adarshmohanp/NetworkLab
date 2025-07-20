import socket

def binary_division(dividend, divisor):
    """Perform modulo-2 binary division and return the remainder."""
    
    m = len(dividend)
    n = len(divisor)
    # Copy the dividend to work on
    remainder = list(dividend)
    
    # Perform division
    for i in range(m - n + 1):
        if remainder[i] == '1':  # Only need to process when bit is '1'
            for j in range(n):
                remainder[i + j] = str(int(remainder[i + j]) ^ int(divisor[j]))
    
    # The remainder is the last (n-1) bits of the updated dividend
    return ''.join(remainder[-(n - 1):])

def server_program():
    host = 'localhost'
    port = 12345
    
    key = input("Enter CRC key (binary): ")

    
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    print("Server is listening...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    # Receive data from client
    encoded_data = conn.recv(1024).decode()
    conn.close()
    
    # Ensure the key is a binary string
    if not (set(key) <= {'0', '1'}):
        print("Error: Key must be a binary string.")
        return
    
    # Perform CRC check
    remainder = binary_division(encoded_data, key)
    
    if remainder == '0' * (len(key) - 1):
        print("No error detected")
    else:
        print("Error detected")

if __name__ == '__main__':
    server_program()