# RAG-Based-QA-Chatbot-using-Langchain
Built a document-aware RAG chatbot enabling dynamic PDF ingestion and grounded question answering using a fully local, cost-free LLM pipeline.
# 📘 Document-Aware RAG Chatbot

## Overview
This project implements a **Document-Aware Retrieval-Augmented Generation (RAG) Chatbot** that allows users to upload PDF documents and ask questions strictly grounded in the uploaded content. The system dynamically ingests documents, builds a session-scoped vector store, and generates coherent, abstractive answers using a fully local and cost-free LLM pipeline.

The chatbot is designed to minimize hallucinations by constraining responses to retrieved document content while still allowing rephrasing, summarization, and explanation.

---

## Key Features
- Upload PDF documents directly via the UI
- Semantic retrieval using vector embeddings
- Grounded, abstractive question answering (RAG)
- Session-scoped vector stores (no cross-document leakage)
- Hallucination-aware fallback for missing information
- Streaming responses for better user experience
- Fully local, no API keys or usage costs

---

## Architecture Overview
<img width="3000" height="4244" alt="RAG_Pipeline_Architecture" src="https://github.com/user-attachments/assets/a8b11095-5a4e-4296-8ac6-12748ec40ff5" />

---

## Tech Stack
- **Language:** Python
- **UI:** Gradio
- **LLM:** Ollama (LLaMA 3)
- **Embeddings:** Sentence-Transformers (all-MiniLM-L6-v2)
- **Vector Database:** Chroma (in-memory)
- **Framework:** LangChain

---

## Project Structure
<img width="1333" height="427" alt="image" src="https://github.com/user-attachments/assets/8e4955e4-e2a5-4b49-91c0-a33e100eeda1" />


---

## How to Run Locally

### Prerequisites
- Python 3.9+
- Ollama installed and running
- LLaMA 3 model pulled locally:
  
ollama pull llama3

### Setup
git clone <repository-url>
cd document-aware-rag-chatbot
pip install -r requirements.txt

### Run the Application
python app.py

### Open your browser and navigate to:
http://127.0.0.1:7860

## Usage
- Upload a PDF document using the file upload option.
- Ask questions related to the uploaded document content.
- Request summaries, explanations, or clarifications.
- If information is not present in the document, the system explicitly indicates this.

## Evaluation Summary
The system was evaluated qualitatively using a custom question set focusing on:
- Retrieval relevance
- Answer groundedness
- Instruction compliance (e.g., word limits)
- Hallucination resistance.
  
Details of the evaluation methodology and observations are documented in evaluation.md.

## Limitations
- Answers depend on the quality and completeness of the uploaded document.
- Evaluation is manual and qualitative.
- Performance may vary for very large or poorly structured PDFs.

## Future Improvements
- Source citations with page-level references
- Support for multiple document uploads
- Advanced retrieval strategies (e.g., MMR)
- Automated evaluation hooks
- Support for additional document formats

## License
This project is licensed under the MIT License.

## Author
Built as a hands-on project to demonstrate applied skills in Retrieval-Augmented Generation, document processing, and system-level AI engineering.
