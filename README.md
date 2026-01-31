# LogEmbedding

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

## Execution
To run the training process, we have to run central server program and client programs at the same time. This can be done by:
1. Create a new terminal for running central server program
```cmd
[terminal 1] python central_server_program.py
```

2. For each client, create a new terminal and run the client program

Client: maryangel101

```cmd
[terminal 2] python client_program.py maryangel101
```

Client: d2klab

```cmd
[terminal 3] python client_program.py d2klab
```
