# RAG Knowledge Assistant

## Problem Statement

Users may need information from a set of approved documents.
Searching through multiple documents manually can be time-consuming.

The goal of this project is to build a document-based AI assistant
that retrieves relevant information from approved documents and
generates answers based on the retrieved content.

If the required information is not available in the provided documents,
the assistant should clearly state that it could not find the answer
in the provided documents.

## Target User

The primary user of this RAG assistant is a student who wants to
quickly find information from a collection of study documents.

The user can ask questions in natural language instead of manually
searching through multiple documents.

## Scope

### In Scope

- Answer questions using information from approved study documents.
- Retrieve relevant document content for each user question.
- Generate clear answers based on the retrieved content.
- Inform the user when the required information is not available in the documents.

### Out of Scope

- Answering questions using information that is not present in the provided documents.
- General web search.
- Generating unsupported or fabricated answers.
- Replacing the original documents as the source of information.

## Source Documents

The RAG assistant will use a small collection of approved public
study documents as its knowledge base.

Initial document categories:

- Python fundamentals
- AI fundamentals
- Machine Learning fundamentals
- RAG fundamentals

The documents will be used only for retrieval and answer generation.
The assistant should rely on the provided documents when answering
user questions.

@Simple Understanding
Approved Documents
       ↓
Knowledge Base
       ↓
RAG searches relevant content
       ↓
Relevant content → LLM
       ↓
Answer 

## Fallback Behavior

If the required information cannot be found in the provided documents,
the assistant must not guess or fabricate an answer.

Instead, it should clearly state:

"The answer could not be found in the provided documents."

This behavior helps keep the assistant grounded in the available
knowledge base.

@simple flow
User Question
      ↓
Search Provided Documents
      ↓
Information Found?
   ↙          ↘
 YES           NO
 ↓             ↓
Answer       Fallback
             Response
       
## Basic RAG Architecture

User Question
      ↓
Retriever
      ↓
Relevant Document Chunks
      ↓
LLM
      ↓
Grounded Answer

@basic flow

The user asks a question in natural language.
The retriever searches the approved document collection.
Relevant document chunks are retrieved.
The retrieved context is provided to the language model.
The language model generates an answer based on the retrieved context.
If relevant information is not found, the fallback behavior is triggered.

