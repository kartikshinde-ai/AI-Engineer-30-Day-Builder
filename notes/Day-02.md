# Day 02 — AI Concepts in My Own Words

## 🎯 Goal

Understand and explain the core AI concepts in simple, professional English without relying on notes.

---

# 1. AI vs Machine Learning

### AI
Artificial Intelligence is the broader field of creating systems that can perform tasks that normally require human-like intelligence.

### Machine Learning
Machine Learning is a subset of AI where systems learn patterns from data and use them to make predictions or decisions.

### Key Difference
**AI = Broad field of intelligent systems**  
**ML = A method of learning from data**

### Interview Answer
> AI is the broader field of creating intelligent systems, while Machine Learning is a subset of AI that enables systems to learn patterns from data.

---

# 2. Large Language Model (LLM)

### Definition
A Large Language Model is an AI model trained on large amounts of text data to understand and generate human-like language.

### Common Uses
- Question answering
- Text generation
- Summarization
- Translation
- Code assistance

### Interview Answer
> An LLM is an AI model trained on large amounts of text data that can understand and generate human-like language.

---

# 3. Embeddings

### Definition
Embeddings are numerical representations of information that capture its semantic meaning.

They allow AI systems to compare information based on meaning rather than only exact keywords.

### Common Uses
- Semantic search
- Similarity search
- Recommendation systems
- RAG

### Interview Answer
> Embeddings are numerical representations of information that capture semantic meaning and allow AI systems to compare and retrieve similar information.

---

# 4. Vector Database

### Definition
A Vector Database is designed to store and search vector representations such as embeddings.

It helps applications retrieve information based on semantic similarity.

### Role in RAG
**Documents → Embeddings → Vector Database → Similarity Search → Relevant Information**

### Interview Answer
> A vector database stores embeddings and allows AI applications to retrieve information based on semantic similarity.

---

# 5. RAG — Retrieval-Augmented Generation

### Definition
RAG is an approach where an AI system retrieves relevant information from an external knowledge source and provides it to an LLM as context before generating an answer.

### Basic Flow

**Documents → Chunks → Embeddings → Vector Database → Retrieval → LLM → Answer**

### Key Point
RAG does not retrain the LLM every time new documents are added. Instead, relevant information is retrieved and provided as context.

### Interview Answer
> RAG stands for Retrieval-Augmented Generation. It retrieves relevant information from an external knowledge source and provides it to an LLM as context before generating an answer.

---

# 6. AI Agent

### Definition
An AI Agent is a system that uses an AI model to understand a goal, choose an appropriate action or tool, execute it, observe the result, and complete the task.

### Basic Agent Loop

**Goal → AI Model → Tool/Action → Execute → Observe → Result**

### AI Agent vs Chatbot
A simple chatbot mainly generates responses, while an AI Agent can interact with external tools and perform controlled actions.

### Interview Answer
> An AI Agent uses an AI model to understand a goal, choose and use tools, observe results, and complete a task through controlled actions.

---

# 7. API — Application Programming Interface

### Definition
An API is a defined way for different software applications or services to communicate with each other.

One application sends a request and receives a response from another system.

### Basic Flow

**Application → API Request → External Service → API Response → Application**

### Common HTTP Methods
- GET — Retrieve data
- POST — Send or create data
- PUT — Update data
- PATCH — Partially update data
- DELETE — Delete data

### Interview Answer
> An API provides a defined way for software applications to communicate by sending requests and receiving responses.

---

# 8. Webhook

### Definition
A Webhook is an event-driven mechanism that allows one application to automatically send data to another application when a specific event occurs.

### Basic Flow

**Event → Webhook → Receiving Application → Workflow**

### API vs Webhook

**API → Application requests information**

**Webhook → Application receives information when an event occurs**

### Interview Answer
> A webhook allows one system to automatically send data to another system when a specific event occurs. It is commonly used to trigger automation workflows.

---

# 9. Automation

### Definition
Automation is the use of software or workflows to perform tasks automatically with little or no manual intervention.

### Basic Flow

**Trigger → Process → Logic → Action → Result**

### Automation vs AI

**Traditional Automation:**  
Follows predefined rules and steps.

**AI-Powered Automation:**  
Uses AI for tasks such as understanding, classification, summarization, or content generation.

### Interview Answer
> Automation uses software and workflows to perform tasks automatically based on triggers and rules, while AI can add intelligent capabilities to the workflow.

---

# 🔗 Core Concept Relationships

### AI Foundation

**AI → ML → LLM**

### RAG

**Documents → Embeddings → Vector Database → Retrieval → LLM → Answer**

### AI Agent

**Goal → LLM/AI Model → Tool → Result → Decision → Answer**

### Automation

**Trigger → Workflow → AI/Logic → Action → Result**

---

# 🧠 Day 02 Key Takeaways

- AI is the broader field of intelligent systems.
- ML is a subset of AI that learns from data.
- LLMs work with human language.
- Embeddings represent semantic meaning as vectors.
- Vector databases store and search embeddings.
- RAG connects external knowledge with an LLM.
- AI Agents can use tools to complete tasks.
- APIs enable software-to-software communication.
- Webhooks enable event-driven communication.
- Automation executes workflows with minimal manual effort.

---
---

# 10. AI Application Architecture

## Basic Architecture

A simple AI application can be understood through the following flow:

**User → App → LLM → Tool/Data → Answer**

### Components

**1. User**  
The user provides a question, instruction, or request.

**2. App**  
The application receives the user input and manages the AI workflow.

**3. LLM**  
The LLM understands the request and generates or processes language.

**4. Tool/Data**  
The application may provide external data or tools when the LLM needs additional information or needs to perform an action.

**5. Answer**  
The system returns the final response or result to the user.

### Flow

```text
┌──────────┐
│   User   │
└────┬─────┘
     │ Request
     ↓
┌──────────┐
│   App    │
└────┬─────┘
     │
     ↓
┌──────────┐
│   LLM    │
└────┬─────┘
     │
     ↓
┌──────────────┐
│  Tool / Data │
└──────┬───────┘
       │
       ↓
┌──────────┐
│  Answer  │
└──────────┘

# 🎯 Self-Check

I should be able to explain the following without reading my notes:

- AI vs ML
- LLM
- Embeddings
- Vector Database
- RAG
- AI Agent
- API
- Webhook
- Automation
-basic architecture


