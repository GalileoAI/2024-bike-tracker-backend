import socket
import sys

def udp_server(host="127.0.0.1", port=12345):
    print(f"Starting UDP server on {host}:{port}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (host, port)

    sock.bind(server_address)

    print("\nWaiting for a connection...")

    while True:
        data, client_address = sock.recvfrom(4096)

        print(f"Received {len(data)} bytes from {client_address}: {data.decode()}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])
        udp_server(host, port)
    else :
        udp_server()