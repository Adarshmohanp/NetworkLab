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

def encode_data(data, key):
    """Encode the data using CRC."""
    k = len(key)
    # with data k-1 zeros are been added
    augmented_data = data + '0' * (k - 1)
    # remainder we are finding
    remainder = binary_division(augmented_data, key)
    # adding remainder to the
    return data + remainder

def client_program():
    host = 'localhost'
    port = 12345
    
    # Get user input for binary data and key
    data = input("Enter binary data: ")
    key = input("Enter CRC key (binary): ")
    
    # Ensure the data and key are binary strings
    if not (set(data) <= {'0', '1'}) or not (set(key) <= {'0', '1'}):
        print("Error: Data and key must be binary strings.")
        return

    encoded_data = encode_data(data, key)

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    # Send encoded data
    client_socket.sendall(encoded_data.encode())
    client_socket.close()

if __name__ == '__main__':
    client_program()