"""Handle Central Server tasks."""
import json
import socket
import os
import numpy as np
from helper.network_communication import send_message, receive_message


HOST = "127.0.0.1"
PORT = 5000


class CentralServerProgram:
    """Handle Central Server tasks."""

    def __init__(self):
        """Initialize CentralServerProgram class."""
        self.client_list = ["maryangel101", "d2klab", "logsage"]  # ["maryangel101", "d2klab", "logsage"]
        self.client_sockets = {}
        self.client_vocabs = {}
        self.indice_map = {}
        # Training coefficients
        self.embed_dimension = 500
        self.num_epochs = 50

    def aggregate_vocab(self) -> dict:
        """Aggregate all clients vocabs and form a new set of internal indices."""
        indice_map = {}
        reserved_index = 0
        for client, client_word_indices in self.client_vocabs.items():
            print(f"Client {client}, number of words: {len(client_word_indices)}")
            for word_index in client_word_indices:
                if word_index.startswith("unk_"):
                    # Make unknown words unique per client
                    key = f"{client}_{word_index}"
                    if key not in indice_map:
                        indice_map[key] = reserved_index
                        reserved_index += 1
                else:
                    if word_index not in indice_map:
                        indice_map[word_index] = reserved_index
                        reserved_index += 1
        self.indice_map = indice_map
        print(f"Aggregated vocab: number of words: {len(indice_map)}")

        # Save for later inspection
        save_path = "dataset/all_indice_map.json"
        with open(save_path, "w", encoding="utf-8") as json_file:
            json.dump(indice_map, json_file, indent=4, ensure_ascii=False)
        return indice_map
    
    def get_client_new_vocab(self, client_name: str) -> dict:
        """From the new internal vocab, extract client's words and return a dict mapping previous to new indices.
        
        Args:
            client_name (str): the name of client we want to extract the words.
        """
        client_indice_map = {}
        for client_global_index in self.client_vocabs.get(client_name):
            if client_global_index.startswith("unk_"):
                internal_index = self.indice_map.get(f"{client_name}_{client_global_index}")
            else:
                internal_index = self.indice_map.get(client_global_index)
            client_indice_map[client_global_index] = internal_index
        return client_indice_map
    
    def run(self) -> None:
        """Run the training process at Central Server side."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((HOST, PORT))
            server.listen()

            print("Central server listening...")

            while len(self.client_sockets) < len(self.client_list):
                conn, addr = server.accept()
                msg = receive_message(conn)

                if msg.get("type") != "VOCAB":
                    # conn.close()
                    continue

                client = msg["client"]
                client_word_indices = msg["word indices"]

                print(f"Client {client} connected from {addr}")
                self.client_sockets[client] = conn
                self.client_vocabs[client] = client_word_indices

            # Build aggregated vocab
            all_indice_map = self.aggregate_vocab()

            # Calculate the total number of words of all clients
            num_words = len(all_indice_map.values())

            # Initialize global weights
            # W₁: Input embeddings (V × N) - Xavier initialization
            W1 = np.random.normal(0, 0.1, (num_words, self.embed_dimension))
            # W₂: Output embeddings (N × V) - Xavier initialization  
            W2 = np.random.normal(0, 0.1, (self.embed_dimension, num_words))

            # Send the inital setup to each client
            for client, sock in self.client_sockets.items():
                # Get client indice map
                client_indice_map = self.get_client_new_vocab(client)
                send_message(sock, {
                    "type": "INITIAL",
                    "indice map": client_indice_map,
                    "W1": W1.tolist(),
                    "W2": W2.tolist()
                })
            
            # Training loop
            for epoch in range(self.num_epochs):
                print(f"\nEpoch {epoch + 1}")
                client_updates = []

                for client, sock in self.client_sockets.items():
                    try:
                        msg = receive_message(sock)
                    except socket.timeout:
                        raise RuntimeError(f"Client {client} did not respond")

                    client_updates.append(
                        (np.array(msg["W1"]), np.array(msg["W2"]))
                    )

                # Aggregate weights
                W1 = np.mean([w1 for w1, _ in client_updates], axis=0)
                W2 = np.mean([w2 for _, w2 in client_updates], axis=0)

                if epoch < 49:
                    for sock in self.client_sockets.values():
                        send_message(sock, {
                            "type": "AGGREGATED_WEIGHTS",
                            "W1": W1.tolist(),
                            "W2": W2.tolist()
                        })
                else:
                    # Notify all clients training is finished
                    for sock in self.client_sockets.values():
                        send_message(sock, {
                            "type": "FINISH",
                            "W1": W1.tolist(),
                            "W2": W2.tolist()
                        })
                        sock.close()
                    print("Training completed. Sent final weights to clients.")

            # Save final weights
            os.makedirs("models", exist_ok=True)
            np.save("models/W1_word2vec.npy", W1)
            np.save("models/W2_word2vec.npy", W2)

            print("Weights saved in models folder.")

                

if __name__ == "__main__":
    CentralServerProgram().run()
