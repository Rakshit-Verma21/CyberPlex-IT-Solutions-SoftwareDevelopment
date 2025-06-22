import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 5000

def recv_messages(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            print("Connection closed by server.")
            sys.exit()
        print("\rPeer:", data.decode(), "\n> ", end='')

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    print(f"Connected to chat server at {HOST}:{PORT}")

    threading.Thread(target=recv_messages, args=(sock,), daemon=True).start()

    while True:
        msg = input("> ")
        if msg.lower() == 'exit':
            print("Exiting chat.")
            sock.close()
            break
        sock.sendall(msg.encode())

if __name__ == '__main__':
    main()