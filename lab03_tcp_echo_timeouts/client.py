import socket


sock = socket.socket()
sock.settimeout(10)

try:
    sock.connect(("localhost", 9090))
    msg = input("message (exit to quit): ")
    sock.sendall(msg.encode())
    if msg.strip().lower() != "exit":
        data = sock.recv(1024)
        print("echo", data.decode())
except socket.timeout:
    print("timeout")
except ConnectionRefusedError:
    print("server not running")
finally:
    sock.close()
