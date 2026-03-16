import socket


sock = socket.socket()
sock.bind(("", 9090))
sock.listen(1)
print("server is listening")

while True:
    conn, addr = sock.accept()
    print("new client accepted", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("received", data.decode())
        if data.strip().lower() == b"exit":
            break
        conn.sendall(data)
    conn.close()
    print("client left, waiting for next")
