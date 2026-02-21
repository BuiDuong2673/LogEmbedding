import json
import struct
import socket


def send_message(sock: socket.socket, data: dict, binary_data: dict = None) -> None:
    """
    Send:
        - JSON metadata
        - Optional binary blocks (e.g., numpy arrays)
    """

    # Serialize JSON metadata
    json_payload = json.dumps(data).encode("utf-8")
    json_header = struct.pack("!I", len(json_payload))

    sock.sendall(json_header + json_payload)

    # If no binary data, stop here
    if not binary_data:
        sock.sendall(struct.pack("!I", 0))
        return

    # Send number of binary blocks
    sock.sendall(struct.pack("!I", len(binary_data)))

    for key, array in binary_data.items():
        raw = array.tobytes()

        # Send key length + key
        key_encoded = key.encode("utf-8")
        sock.sendall(struct.pack("!I", len(key_encoded)))
        sock.sendall(key_encoded)

        # Send raw binary length + raw binary
        sock.sendall(struct.pack("!I", len(raw)))
        sock.sendall(raw)

def recv_exact(sock: socket.socket, n: int) -> bytes:
    """Receive exactly n bytes or raise if connection closed."""
    data = b""
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
            raise ConnectionError("Socket closed while receiving data")
        data += chunk
    return data

def receive_message(sock: socket.socket):
    """
    Receive JSON metadata + optional binary blocks.
    Always waits until full message is received.
    """

    # --- JSON header ---
    header = recv_exact(sock, 4)
    json_length = struct.unpack("!I", header)[0]

    # --- JSON payload ---
    json_payload = recv_exact(sock, json_length)
    data = json.loads(json_payload.decode("utf-8"))

    # --- binary block count ---
    header = recv_exact(sock, 4)
    num_blocks = struct.unpack("!I", header)[0]

    binaries = {}

    for _ in range(num_blocks):
        # key
        key_len = struct.unpack("!I", recv_exact(sock, 4))[0]
        key = recv_exact(sock, key_len).decode("utf-8")

        # raw binary
        raw_len = struct.unpack("!I", recv_exact(sock, 4))[0]
        raw = recv_exact(sock, raw_len)

        binaries[key] = raw

    return data, binaries

