# 🔍 Vector Databases & Semantic Search Lab

Master the technology behind modern AI search systems - from embeddings to production-ready semantic search!

## 📚 Lab Overview

Welcome to the Vector Databases lab! You'll build a semantic search engine for TechDocs Inc., transforming their failing keyword search (60% failure rate) into an intelligent system that understands meaning (95% success rate).

## 🎯 Learning Objectives

By completing this lab, you will:
- ✅ Understand how embeddings capture semantic meaning
- ✅ Master asymmetric search with semantic embeddings
- ✅ Implement smart document chunking with overlap
- ✅ Build production vector stores with ChromaDB
- ✅ Create semantic search that understands meaning

## 🚀 Quick Start

### 1. Setup Environment

```bash
uv venv --python 3.13.11

# Install required packages
uv add sentence-transformers langchain langchain-community langchain-huggingface chromadb numpy
```

### 2. Complete Tasks in Order

Each task builds on the previous one:

```bash

python3 ep3-vector-db/task_1_understanding_embeddings.py
python3 ep3-vector-db/task_2_document_processing.py
python3 ep3-vector-db/task_3_vector_store.py
python3 ep3-vector-db/task_4_semantic_search.py
```

## 📂 File Structure

```
llm-eps/langhchain-llm/learning-path
├── task_1_understanding_embeddings.py
├── task_2_document_processing.py
├── task_3_vector_store.py
├── task_4_semantic_search.py
└── README.md                     # This file
```

## 🎓 Task Details

### Task 1: Understanding How Embeddings Work
**Learning Goal:** See how embeddings capture semantic meaning

**TODOs:**
1. Initialize embedding model (all-MiniLM-L6-v2)
2. Encode search query
3. Encode documents
4. Calculate semantic similarities

**Key Insight:** Embeddings understand that "forgot password" = "password recovery"!

### Task 2: Document Processing
**Learning Goal:** Smart chunking preserves context

**TODOs:**
1. Import RecursiveCharacterTextSplitter
2. Set chunk_size to 500
3. Set chunk_overlap to 100

**Key Insight:** 20% overlap improves retrieval by 40%!

### Task 3: Build Vector Store
**Learning Goal:** Production-ready vector database

**TODOs:**
1. Import Chroma from LangChain
2. Import HuggingFaceEmbeddings
3. Configure embedding model

**Key Insight:** ChromaDB is used by real companies in production!

### Task 4: Semantic Search
**Learning Goal:** Search that understands meaning

**TODOs:**
1. Set search query: "work from home policy"
2. Set k=3 for top results
3. Set score_threshold=0.5

**Key Insight:** "work from home" finds "remote work policy" - semantic magic!

## 📊 Performance Metrics

After completing this lab:
- **Before:** 60% search failure rate
- **After:** 95% search success rate
- **Speed:** <100ms per search
- **No API keys required:** Everything runs locally!

## 🔬 Technical Concepts

### Embeddings
- Convert text to numerical vectors
- Similar meanings = similar vectors
- 384-768 dimensions capture semantic meaning

### Vector Databases
- Store and search embeddings efficiently
- ChromaDB provides production-ready performance
- Metadata filtering for advanced queries

### Semantic Search
- Understands meaning, not just keywords
- "password reset" matches "password recovery"
- Works across languages and synonyms

## 🎉 Completion

Upon completing all 4 tasks:
- ✅ You've built a production-ready semantic search engine
- ✅ Mastered vector databases and embeddings
- ✅ Ready for Lab 5: RAG Systems (adding AI generation)

## 💡 Pro Tips

1. **Start simple:** Get basic search working first
2. **Test thoroughly:** Try different queries to understand behavior
3. **Monitor performance:** Embedding dimensions affect speed/quality tradeoff
4. **Experiment:** Try different chunk sizes and overlap values

## 🔗 Next Steps

After mastering vector databases:
1. **Lab 5: RAG Systems** - Add LLM generation to your search
2. **Production deployment** - Scale to millions of documents
3. **Hybrid search** - Combine keyword and semantic search
4. **Multi-modal** - Search images and text together

---