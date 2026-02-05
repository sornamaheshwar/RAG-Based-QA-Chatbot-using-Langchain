# Evaluation Strategy

This document describes how the Document-Aware RAG Chatbot was evaluated.  
Since this project focuses on Retrieval-Augmented Generation (RAG), evaluation was centered on retrieval quality, answer groundedness, and instruction compliance rather than traditional model accuracy metrics.

---

## 1. Evaluation Objectives

The evaluation aimed to answer the following questions:
- Does the retriever fetch relevant document sections for a given query?
- Are the generated answers strictly grounded in the uploaded document?
- Does the system follow user instructions such as summarization length?
- Does the system avoid hallucinating answers when information is missing?

---

## 2. Evaluation Methodology

### 2.1 Custom Question Set
A set of 15–20 evaluation questions was manually created from the uploaded PDF documents.  
The questions covered multiple categories:
- Fact-based questions (direct information lookup)
- Explanation-based questions (process and concept explanations)
- Summarization tasks (e.g., 100-word summaries)
- Edge cases (questions partially answered in the document)
- Out-of-scope questions (information not present in the document)

---

### 2.2 Retrieval Quality Assessment
For each question:
- The top-k retrieved document chunks were inspected manually.
- Retrieved chunks were checked for relevance to the user query.
- The source section of the PDF was verified to ensure correct retrieval.

This helped validate whether the semantic search was retrieving appropriate context before generation.

---

### 2.3 Groundedness and Hallucination Testing
To test hallucination resistance:
- Questions unrelated to the document content were intentionally asked.
- The expected behavior was a safe fallback response indicating missing information.

The system was considered robust when it avoided introducing external or fabricated information.

---

### 2.4 Instruction Compliance
The system was tested on instruction-following tasks such as:
- Generating summaries of a specified word length
- Rephrasing document content without copying text verbatim

Generated responses were manually checked for:
- Approximate word count compliance (±10 words)
- Coherence and clarity
- Faithfulness to the document content

---

## 3. Evaluation Criteria

Each response was evaluated qualitatively based on:
- **Relevance**: Does the answer address the user question?
- **Faithfulness**: Is the answer strictly grounded in the document?
- **Clarity**: Is the response well-structured and understandable?

---

## 4. Observations

- Retrieval performance improved with moderate chunk overlap and top-k retrieval.
- Explicit prompt constraints reduced hallucinations significantly.
- Abstractive summarization produced better results when multiple relevant chunks were retrieved.
- Performance depends on document quality and clarity.

---

## 5. Limitations

- Evaluation was primarily manual and qualitative.
- No automated scoring metrics (e.g., BLEU or ROUGE) were used, as they are not well-suited for open-ended RAG evaluation.
- Results may vary depending on document structure and length.

---

## 6. Conclusion

The evaluation confirmed that the system reliably retrieves relevant document content, generates grounded responses, and follows user instructions for summarization and explanation tasks. While manual in nature, the evaluation approach provides a realistic and transparent assessment of system behavior for document-based question answering.
