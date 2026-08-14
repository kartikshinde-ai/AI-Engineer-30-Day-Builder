# RAG Basics

## Metadata

- Topic: Retrieval-Augmented Generation
- Source: Internal Study Document
- Document Type: Study Notes

## Retrieval-Augmented Generation

Retrieval-Augmented Generation (RAG) is an approach that combines information retrieval with a language model.

The system retrieves relevant information from a knowledge base and provides that information to the language model to generate a grounded answer.

## RAG Pipeline

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
Relevant Context
    ↓
LLM
    ↓
Answer

@Vector Store

A vector store is used to store vector representations of document chunks and support similarity-based retrieval.

@Grounded Answers

A grounded answer is an answer generated using relevant information retrieved from the provided knowledge base.

@Fallback Behavior

If the required information is not available in the provided documents, the system should clearly state that it could not find the answer instead of guessing.

@Key Takeaway

RAG improves the usefulness of language models by connecting them with an external knowledge base and retrieving relevant information before generating an answer.
