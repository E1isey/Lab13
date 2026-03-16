import pickle
import socket


payload = {"name": "alice", "n": 42}

sock = socket.socket()
sock.connect(("localhost", 9090))
sock.sendall(pickle.dumps(payload))
echo = pickle.loads(sock.recv(4096))
sock.close()

print("echo", echo)
