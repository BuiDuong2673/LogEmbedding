import os
import json

def aggregate_vocab(directory: str) -> dict:
    """Aggregate all clients vocabs and form a new set of internal indices."""
    client_list = ["client_1", "client_2", "client_3"]
    client_vocabs = {}
    # Read client_{i}_word_dict.json files in directory
    for client in client_list:
        file_path = os.path.join(directory, f"{client}_word_dict.json")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as json_file:
                client_vocabs[client] = json.load(json_file)

    indice_map = {}
    reserved_index = 0
    common_words = set()
    common_count = 0
    for client, client_word_indices in client_vocabs.items():
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
                else:
                    common_count += 1
                    common_words.add(word_index)
    print(f"Number of common words across clients: {len(common_words)}")
    print(f"common_count = {common_count}")
    print(f"Aggregated vocab: number of words: {len(indice_map)}")

aggregate_vocab("models_balanced/10_3_epochs_300_dimensions_4_context_3_negative_0001_learning_rate")