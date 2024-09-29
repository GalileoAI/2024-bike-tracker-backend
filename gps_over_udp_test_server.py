# udp_server.py

import socket

def udp_server(host="127.0.0.1", port=12345):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the address
    server_address = (host, port)
    print(f"Starting UDP server on {host}:{port}")
    sock.bind(server_address)

    while True:
        print("\nWaiting for a connection...")
        
        # Receive data from client
        data, client_address = sock.recvfrom(4096)
        
        print(f"Received {len(data)} bytes from {client_address}: {data.decode()}")
        
        if data:
            # Respond back to the client
            sent = sock.sendto(data, client_address)
            print(f"Sent {sent} bytes back to {client_address}")

if __name__ == "__main__":
    udp_server()
