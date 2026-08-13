# Day 04 — Define the RAG Knowledge Assistant

## Goal

Define the purpose, users, scope, data sources, testing strategy, and
correct-answer boundary for a document-based RAG assistant.

---

## What I Learned

### 1. Problem Statement

A RAG assistant retrieves relevant information from approved documents
and uses that information to generate an answer.

The system should rely on the provided documents instead of inventing
unsupported information.

### 2. Target User

The primary user is a student who wants to quickly find information
from a collection of study documents.

### 3. Scope

The assistant should:

- Search approved documents.
- Retrieve relevant information.
- Generate answers based on retrieved content.
- Clearly respond when the required information is unavailable.

The assistant should not:

- Invent information.
- Perform general web searches.
- Provide unsupported answers.

### 4. Source Documents

The initial knowledge base will contain approved public study material
covering:

- Python fundamentals
- AI fundamentals
- Machine Learning fundamentals
- RAG fundamentals

### 5. Test Strategy

I created 15 realistic test questions:

- 10 questions that should be answerable from the documents.
- 5 questions whose answers should not be available in the documents.

This will help test both successful retrieval and safe fallback behavior.

### 6. Correct-Answer Boundary

A key RAG concept is the difference between:

- Information the LLM may already know.
- Information actually available in the supplied documents.

The assistant should answer based on the supplied knowledge base.

If the required information is unavailable, it should use the fallback
response instead of guessing.

### 7. Fallback Rule

If the answer cannot be found in the provided documents, the assistant
should say:

"I could not find this in the provided documents."

The assistant should not guess or fabricate an answer.

---

## RAG Architecture

```text
Documents
    ↓
Chunks
    ↓
Embeddings
    ↓
Vector Store
    ↓
Retrieval
    ↓
LLM
    ↓
Answer

@Architecture Flow

Documents are prepared as smaller chunks.
Chunks are converted into embeddings.
Embeddings are stored in a vector store.
A user question is used to retrieve relevant information.
The retrieved context is provided to the LLM.
The LLM generates a grounded answer.
If relevant information is not available, the fallback rule is used.
