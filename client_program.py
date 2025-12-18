"""Manage client actions."""
from helper.vocab_extractor import VocabExtractor


class ClientProgram:
    """Client program to manage local vocabulary."""
    def __init__(self, client_name: str):
        """Initialize the ClientProgram."""
        self.client_name = client_name
        # Extract the vocab.
        self.vocab_extractor = VocabExtractor(client_name=self.client_name)
        self.word_dict, self.known_words_indices, self.unknown_words = self.vocab_extractor.get_vocab()

    def get_client_vocab(self):
        """Provide client's globally known words to the central server."""
        print(f"Client {self.client_name}:")
        print(f"Number of known words: {len(self.known_words_indices)}")
        print(f"Number of unknown words: {len(self.unknown_words)}")
        return self.known_words_indices