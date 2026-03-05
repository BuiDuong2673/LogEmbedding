# LogEmbedding

## Repository Structure
```bash
logembedding/
├── dataset/                            # Contains all data used for training and testing
│   ├── origin/                         # Contains datasets collected from public datasets
│   ├── balanced_data/                  # Split origin dataset into 3 clients' datasets
│   ├── train_test_imbalanced/          # train and test sets if each public dataset is a client
│   ├── train_test_balanced/            # train and test sets, 80:20 from balanced_data/
│   ├── english_word_dictionary.txt     # The set of English words
│   ├── global_vocab_imbalance.json     # Global dictionary of train set in train_test_imbalanced
│   ├── global_vocab_balanced.json      # Global dictionary of train set in train_test_balanced
│   └── log_common_words.txt            # A set of words that are not included in english dataset but included in all our three public datasets
│
├── embedding_techniques/    
│   ├── __init__.py
│   ├── word2vec.py                     # Methods for training word embedding model
│   ├── sentence2vec.py                 # Methods for training sentence embedding model
│   └── doc2vec.py                      # Methods for training document embedding model
│
├── helper/
│   ├── __init__.py
│   ├── discover_logsage_dataset.py     # Rearrange a dataset to have similar structure as other
│   ├── global_vocab_processor.py       # How to form the global dictionary
│   ├── network_communication.py        # How server and clients contact
│   ├── separate_training_test_set.py   # Split client's datasets into train, test sets (80:20)
│   └── vocab_extractor.py              # Split the logs into words
│
├── test/
│   ├── __init__.py
│   ├── add_balanced_dataset.py         # Split origin dataset into 3 clients' datasets
│   ├── analyse_test_result.py          # Statistical analysis and report of the models performance
│   ├── analyse_test_result_old.py      # The old, simpler version used in final presentation
│   ├── find_similar_log_test.py        # Test the models' accuracies in finding most similar logs
│   └── generate_similar_logs.py        # Generate similar logs for logs in clients' test sets
│
├── models_imbalanced/                  # Models which trained with dataset/train_test_imbalanced/
├── models_balanced/                    # Models which trained with dataset/train_test_balanced/
│
├── test_result_imbalanced_.../         # The old models' test results
├── test_result_balanced/               # The models' test results
│
├── test_analysis_result_imbalanced     # The analysis result of test_result_imbalanced/
├── test_analysis_result_balanced       # The analysis result of test_result_balanced/
│
├── central_server_program.py           # set the actions for central server in the training process
├── client_program.py                   # set the actions for clients in the training process
├── .env.example                        # contains HUGGINGFACE_TOKEN, not published.
├── .gitattributes                      # To upload big W1, W2 to GitHub LFS
└── requirements.txt                    # packages that should be installed for executing this project
```

## Dataset

This file shows the sources of `dataset/` folder.

### maryangel101: ci-cd-failure-detector

Link: https://github.com/maryangel101/ci-cd-failure-detector/tree/main

```python
"dataset/maryangel101/"
```

### D2KLab: gha-dataset

Link: https://github.com/D2KLab/gha-dataset/tree/master

```python
"dataset/d2klab"
```

## ByteLuo1029: LogSage

Link: https://github.com/ByteLuo1029/dataset/tree/main/dataset

```python
"dataset/logsage"
```

### dwyl: english-words

Link: https://github.com/dwyl/english-words

```python
"dataset/english_word_dictionary.txt"
```

## Setup
Please install the required packages in `requirements.txt` with the following command:

```bash
pip install -r requirements.txt
```

If you want to test the pretrained models, some models require HuggingFace token. You can get this token in the HuggingFace website. Then, please create a `.env` file and store your token there.
```env
HUGGINGFACE_TOKEN=[YOUR HUGGINGFACE TOKEN HERE]
```

## Training

You can set the embedding dimension and number of epochs in central server in the `__init__` function of central_server_program.py.

You can set the context window size, number of negative samples, learning rate, number of epochs in client's training in the main program of the client_program.py.

To save the model, please provide the its name in the `model_name` variable in the main program of central_server_program.py and client_program.py. Note that the model_name in central_server_program.py and the model_name in client_program.py should be similar.

After setting these variables, we can run the training process. We have to run central server program and client programs at the same time. This can be done by:

1. Create a new terminal for running central server program

```cmd
[terminal 1] python central_server_program.py
```

2. For each client, create a new terminal and run the client program

Client: client_1

```cmd
[terminal 2] python client_program.py client_1
```

Client: client_2

```cmd
[terminal 3] python client_program.py client_2
```

Client: client_3

```cmd
[terminal 4] python client_program.py client_3
```

## Testing
To test the model, first enter the path to the model `model_path`. Then, run the following command:

```cmd
python -m test.find_similar_log_test > test_result/[name of the model being tested].txt
```

This command execute the test program and save the output to a file for later analysis.

*  Because the files storing matrices W1, W2 of the model are too big to be pushed to GitHub, we use Git LFS to store W1, W2 files instead of using normal Git storage. Therefore, to test the models that are uploaded to GitHub, you may need `git lfs pull` instead of `git pull`.

## Analyzing Testing Result
File `test/analyse_test_result.py` performs the statistical analysis of the test result collected and visualizes the results in appropriate plots. 

This can be done by calling the functions in the `main_balance()` program in `analyse_test_result.py`, which correspond to the analysis you want.

Then execute `analyse_test_result.py`.

```bash
python test/analyze_test_result.py
```

