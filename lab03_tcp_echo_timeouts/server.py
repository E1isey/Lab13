import socket


sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("", 9090))
sock.listen(1)
print("server is listening on 9090")

while True:
    try:
        sock.settimeout(30)
        conn, addr = sock.accept()
        sock.settimeout(None)
        conn.settimeout(60)
        print("new client", addr)
        while True:
            try:
                data = conn.recv(1024)
            except socket.timeout:
                print("timeout, closing connection")
                break
            if not data:
                break
            print("received", data.decode())
            if data.strip().lower() == b"exit":
                break
            conn.sendall(data)
        conn.close()
        print("client left")
    except socket.timeout:
        print("no client, listening again")
    except KeyboardInterrupt:
        print("server stop")
        break

sock.close()
