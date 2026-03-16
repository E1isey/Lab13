import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 9091))
print("udp server is listening on 9091")

while True:
    data, addr = sock.recvfrom(1024)
    print("received", data.decode(), "from", addr)
    sock.sendto(data, addr)
