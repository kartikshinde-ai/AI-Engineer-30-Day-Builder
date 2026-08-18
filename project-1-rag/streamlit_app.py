import streamlit as st

from app import embeddings, vector_store, cosine_similarity, llm, file_path


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="RAG Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 RAG Assistant")
st.write("Ask a question based on the available knowledge.")


# -----------------------------
# Question Input
# -----------------------------
question = st.text_input(
    "Enter your question:",
    placeholder="What is Retrieval-Augmented Generation?"
)


# -----------------------------
# Ask Button
# -----------------------------
if st.button("Ask"):

    if not question.strip():
        st.warning("Please enter a question.")
    else:

        # Create question embedding
        question_vector = embeddings.embed_query(question)

        # Calculate similarity
        results = []

        for item in vector_store:

            score = cosine_similarity(
                question_vector,
                item["vector"]
            )

            results.append({
                "text": item["text"],
                "score": score
            })

        # Sort by similarity
        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        # Top 3 relevant chunks
        top_results = results[:3]

        # Retrieved context
        retrieved_text = "\n\n---\n\n".join(
            item["text"]
            for item in top_results
        )

        # Source
        source_file = file_path.name

        # -----------------------------
        # Generate Answer
        # -----------------------------
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

        response = llm.invoke(prompt)

        # -----------------------------
        # Display Result
        # -----------------------------
        st.success("Answer generated successfully.")

        st.subheader("Question")
        st.write(question)

        st.subheader("Answer")
        st.write(response)

        st.subheader("Source")
        st.write(source_file)