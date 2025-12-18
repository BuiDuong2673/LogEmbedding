"""Manage central server actions."""
import json
from helper.global_vocab_processor import GlobalVocabProcessor
from client_program import ClientProgram

class CentralServerProgram:
    """Central server program to manage global vocabulary."""
    def __init__(self):
        """Initialize the CentralServerProgram."""
        self.global_vocab_processor = GlobalVocabProcessor()
        # Read the vocab if not read yet
        self.vocab_global_index = self.global_vocab_processor.get_global_vocab()
        # Define client list
        self.client_list = ["maryangel101", "d2klab"]
        # Initialize full vocab
        self.full_vocab = {}
        # Initialize onehot embedding
        self.onehot_embedding = {}

    def get_all_client_vocabs(self):
        """Get the vocabulary for each client."""
        full_vocab = {}
        reserved_index = 0
        for client in self.client_list:
            # Call the client program to get its vocab's global indices
            client_program = ClientProgram(client_name=client)
            client_vocab = client_program.get_client_vocab()
            # Store all globally known words from all clients in an internal vocab
            for global_index in client_vocab:
                if global_index not in full_vocab:
                    # Assign an index to the word in internal vocab
                    full_vocab[global_index] = reserved_index
                    reserved_index += 1
        self.full_vocab = full_vocab
        # Save full internal vocab to JSON
        with open("dataset/internal_central_vocab.json", "w", encoding="utf-8") as json_file:
            json.dump(self.full_vocab, json_file, ensure_ascii=False, indent=4)
        print(f"Save the vocab to path: dataset/internal_central_vocab.json")
        return self.full_vocab


if __name__ == "__main__":
    central_server_program = CentralServerProgram()
    _ = central_server_program.get_all_client_vocabs()