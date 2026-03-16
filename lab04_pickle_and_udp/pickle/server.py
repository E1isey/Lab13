import pickle
import socket


sock = socket.socket()
sock.bind(("", 9090))
sock.listen(1)
print("pickle server is listening on 9090")

conn, addr = sock.accept()
print("new client accepted", addr)

data = conn.recv(4096)
obj = pickle.loads(data)
print("received object", obj)

conn.sendall(data)
conn.close()
sock.close()
