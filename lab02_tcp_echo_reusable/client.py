import socket


sock = socket.socket()
sock.connect(("localhost", 9090))

while True:
    msg = input("message (exit to quit): ")
    sock.sendall(msg.encode())
    if msg.strip().lower() == "exit":
        break
    data = sock.recv(1024)
    print("echo", data.decode())

sock.close()
