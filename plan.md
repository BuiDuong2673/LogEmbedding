# Log Embedding Project Plan
**Research Goal**: Use an embedding model to determine if a new input log belongs to the same category (log template matching)

---

## 0. Project Objective

### Core Problem
Map logs with identical semantic structure but different variables to the same category:
- Input 1: `"Error: failure type ABC observed at 17:57 21/11/2025"`
- Input 2: `"Error: failure type ABC observed at 17:00 21/12/2026"`
- Expected Output: **Same Category** (identical log template)

### Technical Approach
1. **Log Template Extraction** - Identify fixed parts and variable parts of logs
2. **Embedding Learning** - Learn vector representations for log templates
3. **Classification/Matching** - Determine which known template a new log belongs to

---

## 1. Current Project Status

### Completed Features
✅ Global vocabulary management (`GlobalVocabProcessor`)
- Load 370K+ English word dictionary
- Word-to-index mapping

✅ Client vocabulary extraction (`VocabExtractor`)
- Timestamp removal
- Tokenization (supports camelCase, underscore, hyphen splitting)
- Word frequency and context window
- Known/unknown word classification

✅ Distributed architecture
- Central server + multiple clients
- Vocabulary aggregation

### Datasets
- **maryangel101**: CI/CD failure detection logs
  - `pass/` and `fail/` subdirectories (labeled)
- **d2klab**: GitHub Actions build logs
- **words_alpha.txt**: Global English dictionary

---

## 2. Implementation Plan - Next Steps

### Phase 1: Log Template Extraction (Priority: High)

#### Objective
Extract structured templates from raw logs, for example:
```
Raw:      "Error: failure type ABC observed at 17:57 21/11/2025"
Template: "Error: failure type <VAR> observed at <TIME> <DATE>"
```

#### Implementation Options (Choose One)

**Option A: Drain Algorithm (Recommended)**
- Use mature log parsing algorithm
- Library: `drain3` or `logparser`
- Advantages: No labeled data ne eded, online parsing
- Output: Log templates + parameter lists

**Option B: Rule-Enhanced Variable Recognition**
- Extend existing `delete_time_stamp()` method
- Recognize more variable types:
  - Timestamps (already implemented)
  - Numbers/IDs
  - File paths
  - IP addresses
  - UUIDs/hashes
- Replace with placeholders `<NUM>`, `<PATH>`, `<ID>`, etc.

**Option C: Deep Learning End-to-End**
- Use LogBERT / Log2Vec
- Automatically learn semantic representations
- Requires more compute resources

#### Implementation Steps
1. Create `helper/log_parser.py`
2. Implement template extraction function
3. Integrate into `VocabExtractor` pipeline
4. Save templates to JSON file

**Expected Deliverables**
- `helper/log_parser.py` - Log parsing module
- `dataset/client_name_templates.json` - Extracted template library
- Test script to validate template quality

---

### Phase 2: Template Embedding (Priority: High)

#### Objective
Learn fixed-dimension vector representations for each log template

#### Approach Selection

**Option A: Word2Vec / Doc2Vec (Recommended for Start)**
- Based on existing vocabulary and context window
- Fast training, easy to understand
- Suitable for word-level semantics

**Option B: Sentence-BERT**
- Use pretrained models
- Stronger semantic understanding
- Requires GPU and more dependencies

**Option C: TF-IDF + SVD (Baseline)**
- Simplest baseline approach
- Use for comparison experiments

#### Implementation Steps
1. Create `models/log_embedder.py`
2. Implement training function
   - Input: Templated logs
   - Output: Embedding model
3. Save model checkpoint
4. Implement inference function: `log_text → embedding_vector`

**Expected Deliverables**
- `models/log_embedder.py` - Embedding model
- `models/checkpoints/` - Trained models
- `models/embedding_config.json` - Hyperparameter configuration

---

### Phase 3: Classification/Matching System (Priority: Medium)

#### Objective
Given a new log, determine which known template it belongs to

#### Methods

**Method A: Similarity Retrieval**
- Compute similarity between new log and all known templates
- Return top-k most similar templates
- Use cosine similarity or Euclidean distance

**Method B: Classifier**
- Train classification model (SVM, neural network)
- Input: Log embedding
- Output: Template category ID

**Method C: Approximate Nearest Neighbor (ANN) Search**
- Use FAISS or Annoy
- Fast retrieval for large-scale template libraries

#### Implementation Steps
1. Create `inference/log_classifier.py`
2. Build template index
3. Implement query interface
4. Add threshold judgment (whether it's a new template)

**Expected Deliverables**
- `inference/log_classifier.py` - Classifier
- `inference/template_index.faiss` - Template index
- REST API or CLI tool

---

### Phase 4: Evaluation & Optimization (Priority: Medium)

#### Evaluation Metrics
- **Template Accuracy**: Whether new log matches correct template
- **Clustering Quality**: F1-score, ARI
- **Retrieval Performance**: Recall@K, MRR

#### Experiment Setup
1. Use `maryangel101/pass` and `fail` data for supervised learning
2. Cross-validation
3. Compare different methods:
   - Baseline: TF-IDF
   - Word2Vec
   - Doc2Vec
   - (Optional) BERT-based

#### Visualization
- t-SNE dimensionality reduction for embedding space visualization
- Template cluster visualization
- Confusion matrix

**Expected Deliverables**
- `evaluation/eval_script.py`
- Experiment report
- Visualization charts

---

## 3. Technology Stack

### Required Libraries
```python
# Log parsing
drain3           # Drain algorithm
logparser        # Multiple log parsing algorithms

# Embedding
gensim           # Word2Vec, Doc2Vec
sentence-transformers  # BERT-based (optional)

# Similarity retrieval
faiss-cpu        # or faiss-gpu
annoy            # Optional ANN library

# Data processing
numpy
pandas
scikit-learn

# Visualization
matplotlib
seaborn
```

---

## 4. Suggested Project Structure Reorganization

```
LogEmbedding/
├── dataset/                 # Dataset (existing)
├── helper/                  # Preprocessing tools (existing)
│   ├── global_vocab_processor.py
│   ├── vocab_extractor.py
│   └── log_parser.py       # [NEW] Log template extraction
├── models/                  # [NEW] Model definitions
│   ├── log_embedder.py     # Embedding model
│   └── checkpoints/         # Model weights
├── inference/               # [NEW] Inference system
│   ├── log_classifier.py   # Classification/matching
│   └── template_index/      # Template index files
├── evaluation/              # [NEW] Evaluation scripts
│   └── eval_script.py
├── central_server_program.py  # (existing, may need updates)
├── client_program.py          # (existing, may need updates)
└── train.py                   # [NEW] Training entry point
```

---

## 5. Implementation Priority & Timeline

### Short-term (1-2 weeks)
1. ✅ Understand existing codebase
2. 🔲 Implement log template extraction (Drain or rules)
3. 🔲 Train basic Word2Vec embedding

### Mid-term (3-4 weeks)
4. 🔲 Implement classification/retrieval system
5. 🔲 Evaluate system performance
6. 🔲 Iterative optimization

### Long-term (Optional)
7. 🔲 Try deep learning methods (BERT)
8. 🔲 Federated learning integration
9. 🔲 Online learning capability

---

## 6. Key Challenges & Solutions

### Challenge 1: Inaccurate variable part identification
**Solutions**:
- Use Drain algorithm for automatic learning
- Manual verification of high-frequency templates
- Iteratively optimize parsing rules

### Challenge 2: New template detection
**Solutions**:
- Set similarity threshold
- Below threshold → mark as new template
- Support online template library updates

### Challenge 3: Log format differences across clients
**Solutions**:
- Train independent parser for each client
- Central server unifies embedding space
- Federated learning for shared template semantics

---

## 7. References

- **Drain**: He et al., "Drain: An Online Log Parsing Approach with Fixed Depth Tree"
- **LogBERT**: Guo et al., "LogBERT: Log Anomaly Detection via BERT"
- **Word2Vec**: Mikolov et al., "Efficient Estimation of Word Representations"

---

## 8. Next Action Items

**Fastest Validation Path** (Minimum Viable Solution):
1. Use Drain3 to extract templates from `maryangel101` data
2. Train template embeddings with Word2Vec
3. Implement simple similarity matching
4. Validate effectiveness on pass/fail data

**Code Implementation Order**:
```bash
# 1. Install dependencies
pip install drain3 gensim scikit-learn

# 2. Create log parser
# Create helper/log_parser.py

# 3. Run template extraction
python helper/log_parser.py

# 4. Train embedding
# Create models/log_embedder.py
python models/log_embedder.py

# 5. Test inference
# Create inference/log_classifier.py
python inference/log_classifier.py
```

---

**Questions to Discuss**:
- Which log parsing approach to choose? (Recommend Drain)
- Embedding dimension size? (Recommend 128 or 256)
- Need distributed training?
