# Day 08 - Make RAG Usable

## Goal

Turn the working RAG prototype into a simple usable interface.

## Today's Tasks

- Create a simple interface for the RAG system
- Allow a user to enter a question
- Display the generated answer
- Test the interface with another person
- Record feedback and issues
- Document the result

## Success Criteria

- User can enter a question
- RAG retrieves relevant information
- Answer is displayed clearly
- Unanswerable questions are handled safely
- Another person can use and test the system

## Evaluation

## RAG System Evaluation

## Evaluation

| Question | Expected | Retrieved Source | Actual Result | Pass/Fail | Reason/Fix |
|---|---|---|---|---|---|
| What do embeddings do? | Explain the purpose of embeddings | knowledge.txt | Correct answer generated from retrieved context | PASS | No fix needed |
| What is Retrieval-Augmented Generation? | Definition of RAG | knowledge.txt | Correct RAG definition generated from retrieved context | PASS | No fix needed |
| What is the population of India? | System should not answer from outside knowledge | knowledge.txt | Correct fallback message shown: information not found in provided documents | PASS | No fix needed |

## What I Learned

- Connected the RAG backend with a Streamlit user interface.
- Learned how a user can enter a question through the UI.
- Learned how the question is converted into an embedding and compared with stored vectors.
- Learned how the most relevant context is retrieved before generating an answer.
- Learned how the LLM uses retrieved context to generate the final answer.
- Learned how to display the question, answer, and source in the UI.
- Learned how to handle questions that are not available in the provided documents.

## Problems Faced

- The Streamlit UI initially displayed the question input but was not connected to the RAG backend.
- Python virtual environment activation caused a PowerShell execution-policy issue.
- Streamlit was initially not installed in the virtual environment.
- The application needed a separate Streamlit interface file.

## Fixes

- Connected `streamlit_app.py` with the existing RAG components from `app.py`.
- Enabled the PowerShell execution policy for the current process.
- Installed Streamlit and required dependencies inside the virtual environment.
- Created and tested the Streamlit RAG Assistant interface.
- Added a fallback response when information is not available in the retrieved documents.

## Improvements

- Show source information together with the generated answer.
- Add clear error messages for invalid or empty questions.
- Test the interface with different questions.
- Improve the UI design and user experience.
- Add conversation history in a future version.