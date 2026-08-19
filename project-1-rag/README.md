# RAG Assistant

A simple Retrieval-Augmented Generation (RAG) based question-answering system built with Python, embeddings, Ollama, and Streamlit.

## Problem

A language model may not always have access to the specific information contained in a user's documents.

This project solves this problem by retrieving relevant information from a local knowledge document and providing that retrieved context to a language model before generating an answer.

## Features

- Ask questions through a simple Streamlit interface
- Convert documents and questions into embeddings
- Perform similarity-based retrieval
- Retrieve the most relevant information from the knowledge base
- Generate answers using Ollama and Llama 3.2
- Display the source document
- Handle questions when the required information is not available
- Test the system with different questions

## Architecture

The system follows this flow:

User Question
      ↓
Question Embedding
      ↓
Similarity Search
      ↓
Retrieve Relevant Context
      ↓
Ollama / Llama 3.2
      ↓
Generated Answer
      ↓
Streamlit Interface

## Technologies Used

- Python
- Streamlit
- Ollama
- Llama 3.2
- Embeddings
- LangChain
- Git & GitHub

## Project Structure

```text
project-1-rag/
│
├── data/
│   └── knowledge.txt
│
├── documents/
│   ├── ai-basics.md
│   ├── python-basics.md
│   └── rag-basics.md
│
├── app.py
├── streamlit_app.py
├── requirements.md
├── test-questions.md
├── test-results.md
└── README.md

Setup
1. Create and activate the virtual environment

python -m venv .venv

Activate it using:

.\.venv\Scripts\Activate.ps1

2. Install dependencies

Install the required Python packages listed in requirements.md.

3. Make sure Ollama is running

The project uses the local Ollama model:

llama3.2:3b

The embedding model used in the project is:

nomic-embed-text
4. Run the Streamlit application
streamlit run streamlit_app.py

The application will open locally in the browser.

-How It Works
The knowledge document is loaded.
The document is split into smaller chunks.
Embeddings are generated for the chunks.
The user's question is converted into an embedding.
Cosine similarity is used to compare the question with stored vectors.
The most relevant chunks are retrieved.
The retrieved context is passed to the language model.
The model generates an answer using the retrieved context.
The Streamlit interface displays the question, answer, and source.
Test Results

The system was tested with questions related to the available knowledge.

Examples:

What is AI Engineering?
What is Retrieval-Augmented Generation?
What do embeddings do?
What is the purpose of embeddings?

The system successfully retrieved relevant information and generated answers from the provided knowledge.

An out-of-context question was also tested:

What is the population of India?

Since this information was not available in the provided documents, the system returned:

I could not find this information in the provided documents.

This confirms that the system is instructed not to use information outside the retrieved context.

## Limitations
The system can only answer accurately when the required information is available in the provided knowledge documents.
The current vector storage is a simple in-memory structure.
The application is designed as a local prototype.
Answer quality depends on the retrieved context and the language model.
The current system does not automatically search the internet for missing information.


## Future Improvements
Use a persistent vector database
Support multiple document formats
Improve retrieval accuracy
Add conversation history
Add document upload functionality
Deploy the application for public access

Project Status

Day 09 completed successfully.

The RAG prototype has been converted into a simple usable Streamlit interface and tested with both relevant and out-of-context questions.

## Screenshots

Screenshots of the working application are added in seperate screenshoots folder.

### RAG Assistant Interface
![RAG Assistant Interface](screenshots/interface.png)

### RAG Answer
![RAG Answer](screenshots/rag%20answer.jpeg)

### Information Not Found
![Information Not Found](screenshots/not%20found.jpeg)

'''

