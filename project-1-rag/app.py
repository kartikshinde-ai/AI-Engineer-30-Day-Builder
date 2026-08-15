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
question = "What is Retrieval-Augmented Generation?"


# 6. Create question embedding
question_vector = embeddings.embed_query(question)


# 7. Calculate similarity
def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))

    magnitude_a = sum(x * x for x in a) ** 0.5
    magnitude_b = sum(y * y for y in b) ** 0.5

    return dot_product / (magnitude_a * magnitude_b)


# 8. Retrieve most relevant chunk
results = []

for item in vector_store:
    score = cosine_similarity(question_vector, item["vector"])

    results.append({
        "text": item["text"],
        "score": score
    })


results.sort(key=lambda x: x["score"], reverse=True)

retrieved_text = results[0]["text"]


# 9. IMPORTANT: Inspect retrieved text
print("\n=== RETRIEVED TEXT ===")
print(retrieved_text)

print("\nSimilarity Score:")
print(results[0]["score"])


# 10. Send retrieved context to LLM
llm = OllamaLLM(
    model="llama3.2:3b"
)

prompt = f"""
Answer the question using ONLY the retrieved context below.

Retrieved Context:
{retrieved_text}

Question:
{question}

Answer:
"""

response = llm.invoke(prompt)


# 11. Final response
print("\n=== FINAL ANSWER ===")
print(response)