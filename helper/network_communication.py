import json
import struct
import socket


def send_message(sock: socket.socket, data: dict) -> None:
    """Send a length-prefixed JSON message."""
    payload = json.dumps(data).encode("utf-8")
    header = struct.pack("!I", len(payload))
    sock.sendall(header + payload)


def receive_message(sock: socket.socket) -> dict:
    """Receive a length-prefixed JSON message."""
    header = sock.recv(4)
    if not header:
        return {}

    length = struct.unpack("!I", header)[0]
    payload = b""
    while len(payload) < length:
        chunk = sock.recv(length - len(payload))
        if not chunk:
            break
        payload += chunk

    return json.loads(payload.decode("utf-8"))

