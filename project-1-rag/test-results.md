# Day 07 - RAG Test Results

## Answerable Questions

| # | Question | Result |
|---|---|---|
| 1 | What is AI Engineering? | PASS |
| 2 | What is Retrieval-Augmented Generation? | PASS |
| 3 | What does a RAG system typically contain? | PASS |
| 4 | What do embeddings do? | PASS |
| 5 | What does vector search find? | PASS |
| 6 | What is the purpose of embeddings? | PASS |
| 7 | What information does RAG retrieve? | PASS |
| 8 | What should happen before the language model generates an answer? | PASS |
| 9 | What does a reliable RAG system use to answer questions? | PASS |
| 10 | What should the retrieved information be before it is passed to the language model? | PASS |

## Unanswerable Questions

| # | Question | Result |
|---|---|---|
| 1 | Who invented RAG? | PASS |
| 2 | What is the capital of France? | PASS |
| 3 | Who is the CEO of OpenAI? | PASS |
| 4 | What year was RAG invented? | PASS |
| 5 | What is the population of India? | PASS |

## Fallback Behavior

The system correctly avoids answering questions that are not supported by the provided documents.

Expected behavior:

`I could not find this information in the provided documents.`

## Day 07 Result

- 10 answerable questions tested
- 5 unanswerable questions tested
- Safe fallback verified
- Source information verified