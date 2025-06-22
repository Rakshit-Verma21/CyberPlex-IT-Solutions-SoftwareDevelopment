import socket
import threading

HOST = '127.0.0.1'
PORT = 5000
clients = []

def handle_client(conn, peer_conn):
    try:
        while True:
            data = conn.recv(1024)
            if not data: break
            peer_conn.sendall(data)
    finally:
        conn.close()

def main():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, PORT))
    srv.listen(2)
    print(f"Server listening on {HOST}:{PORT}")

    # accept exactly two clients
    conn1, addr1 = srv.accept()
    print("User1 connected:", addr1)
    conn2, addr2 = srv.accept()
    print("User2 connected:", addr2)

    # spawn threads to shuttle data between them
    t1 = threading.Thread(target=handle_client, args=(conn1, conn2))
    t2 = threading.Thread(target=handle_client, args=(conn2, conn1))
    t1.start(); t2.start()
    t1.join(); t2.join()

if __name__ == '__main__':
    main()