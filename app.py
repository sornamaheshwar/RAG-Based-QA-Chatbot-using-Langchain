import gradio as gr
from langchain_community.chat_models import ChatOllama

#Import ingestion logic
from ingestion import ingest_uploaded_pdf



#Local LLM (Ollama)
llm = ChatOllama(
    model="llama3",
    temperature=0.3
)


#RAG chat function
def stream_response(message, history, vector_store):
    """
    Handles user queries using the session-specific vector store.
    """

    #No document uploaded yet
    if vector_store is None:
        yield "📄 Please upload a PDF first."
        return

    #Retrieve relevant chunks
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})
    docs = retriever.invoke(message)

    #No relevant information found
    if not docs:
        yield "I couldn’t find relevant information in the uploaded document."
        return

    #Combine retrieved content
    knowledge = ""
    for doc in docs:
        knowledge += doc.page_content + "\n\n"

    #Abstractive, grounded RAG prompt
    rag_prompt = f"""
You are an assistant answering questions using ONLY the information
present in the provided knowledge.

You are allowed to:
- rephrase the content in your own words
- combine information from multiple parts of the knowledge
- expand explanations for clarity
- generate summaries of a requested length

You are NOT allowed to:
- introduce facts not present in the knowledge
- use external or prior knowledge

Task:
{message}

Instructions:
- If a word limit is requested, follow it strictly (±10 words).
- If the knowledge is insufficient, say so clearly.

Knowledge:
{knowledge}
"""

    partial_response = ""
    for chunk in llm.stream(rag_prompt):
        partial_response += chunk.content
        yield partial_response


#Gradio UI
with gr.Blocks() as demo:

    gr.Markdown("## 📘 Document-Aware RAG Chatbot")

    #Session state to store vector DB
    vector_state = gr.State(None)

    #PDF upload component
    file_upload = gr.File(
        label="Upload a PDF",
        file_types=[".pdf"]
    )

    #Chat interface
    chat_interface = gr.ChatInterface(
        fn=stream_response,
        additional_inputs=[vector_state],
        textbox=gr.Textbox(
            placeholder="Ask a question about the uploaded document...",
            scale=7
        )
    )

    #Trigger ingestion on file upload
    file_upload.change(
        fn=ingest_uploaded_pdf,
        inputs=file_upload,
        outputs=vector_state
    )


#Launch application
demo.launch()
