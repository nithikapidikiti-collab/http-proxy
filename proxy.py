import socket, threading

def handle(client):
    req = client.recv(4096)
    if not req: return
    lines = req.split(b"\r\n")
    method, path, _ = lines[0].split(b" ")
    host = [l for l in lines if l.startswith(b"Host:")][0].split(b" ")[1].decode()
    port = 80
    if ":" in host:
        host, port = host.split(":")
        port = int(port)
    print(f"[>] {method.decode()} {path.decode()} -> {host}:{port}")
    srv = socket.socket()
    srv.connect((host, port))
    srv.send(req)
    while True:
        data = srv.recv(4096)
        if not data: break
        client.send(data)
    srv.close()
    client.close()

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 8888))
s.listen(50)
print("[*] Proxy running on :8888")
while True:
    c, _ = s.accept()
    threading.Thread(target=handle, args=(c,)).start()