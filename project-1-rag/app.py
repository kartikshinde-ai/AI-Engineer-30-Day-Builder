from pathlib import Path

from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


# 1. Load document
file_path = Path("data/knowledge.txt")
text = file_path.read_text(encoding="utf-8")

document = Document(page_content=text)

print("\n=== DOCUMENT LOADED ===")
print(text)


# 2. Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_documents([document])

print("\n=== CHUNKS CREATED ===")
print(f"Number of chunks: {len(chunks)}")


# 3. Create embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vectors = embeddings.embed_documents(
    [chunk.page_content for chunk in chunks]
)

print("\n=== EMBEDDINGS CREATED ===")
print(f"Number of vectors: {len(vectors)}")
print(f"Vector dimensions: {len(vectors[0])}")


# 4. Simple vector storage
vector_store = []

for chunk, vector in zip(chunks, vectors):
    vector_store.append({
        "text": chunk.page_content,
        "vector": vector
    })

print("\n=== VECTOR STORAGE READY ===")


# 5. Ask a known question
# question = "What is AI Engineering?"
# question = "What is Retrieval-Augmented Generation?"
# question = "What does a RAG system typically contain?"
# question = "What do embeddings do?"
# question = "What does vector search find?"
# question = "What is the purpose of embeddings?"
# question = "What information does RAG retrieve?"
# question = "What should happen before the language model generates an answer?"
# question = "What does a reliable RAG system use to answer questions?"
# question = "What should the retrieved information be before it is passed to the language model?"
# question = "Who invented RAG?"
# question = "What is the capital of France?"
# question = "Who is the CEO of OpenAI?"
# question = "What year was RAG invented?"
# question = "What is the population of India?"



# 6. Create question embedding
question_vector = embeddings.embed_query(question)


# 7. Calculate similarity
def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))

    magnitude_a = sum(x * x for x in a) ** 0.5
    magnitude_b = sum(y * y for y in b) ** 0.5

    return dot_product / (magnitude_a * magnitude_b)


# 8. Retrieve top 3 most relevant chunks

results = []

for item in vector_store:
    score = cosine_similarity(question_vector, item["vector"])

    results.append({
        "text": item["text"],
        "score": score
    })


results.sort(key=lambda x: x["score"], reverse=True)

top_results = results[:3]

retrieved_text = "\n\n---\n\n".join(
    item["text"] for item in top_results
)

source_file = file_path.name


# 9. IMPORTANT: Inspect retrieved text
print("\n=== RETRIEVED TEXT ===")
print(retrieved_text)

print("\n=== SOURCE ===")
print(source_file)

print("\n=== TOP SIMILARITY SCORES ===")

for i, item in enumerate(top_results, start=1):
    print(f"{i}. {item['score']}")

# 10. Send retrieved context to LLM

llm = OllamaLLM(
    model="llama3.2:3b"
)

prompt = f"""
You are a document question-answering assistant.

Use the retrieved context to answer the question.

Retrieved Context:
{retrieved_text}

Question:
{question}

Instructions:
- If the answer is present in the retrieved context, answer it directly.
- Use only information from the retrieved context.
- Do not use outside knowledge.
- If the answer is not present in the retrieved context, say:
  "I could not find this information in the provided documents."

Answer:
"""

print("\n=== GENERATING ANSWER ===")

response = llm.invoke(prompt)

print("\n=== FINAL ANSWER ===")
print(response)