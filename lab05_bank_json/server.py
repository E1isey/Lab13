import json
import socket


def handle_request(request, balance):
    action = request.get("action")

    if action == "balance":
        return {"ok": True, "balance": balance}, balance

    if action in {"deposit", "withdraw"}:
        amount = request.get("amount")
        if not isinstance(amount, int) or amount <= 0:
            return {"ok": False, "error": "amount must be positive integer"}, balance

        if action == "deposit":
            balance += amount
            return {"ok": True, "balance": balance}, balance

        if amount > balance:
            return {"ok": False, "error": "not enough money"}, balance

        balance -= amount
        return {"ok": True, "balance": balance}, balance

    return {"ok": False, "error": "unknown action"}, balance


balance = 0
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("", 9092))
sock.listen(1)
print("bank server is listening on 9092")

while True:
    try:
        conn, addr = sock.accept()
    except KeyboardInterrupt:
        print("server stop")
        break

    print("new client", addr)
    data = conn.recv(1024)
    if not data:
        conn.close()
        continue

    try:
        request = json.loads(data.decode())
        reply, balance = handle_request(request, balance)
        print("request", request)
    except json.JSONDecodeError:
        reply = {"ok": False, "error": "invalid json"}
        print("request invalid json")

    conn.sendall(json.dumps(reply).encode())
    print("reply", reply)
    conn.close()

sock.close()
