import socket


sock = socket.socket()
sock.bind(("", 9090))
sock.listen(1)
print("server is listening")

conn, addr = sock.accept()
print("new client accepted", addr)

data = conn.recv(1024)
print("received data", data.decode())

conn.sendall(data)
conn.close()
sock.close()
