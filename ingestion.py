from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def ingest_uploaded_pdf(file):
    """
    Ingests a user-uploaded PDF file and returns an in-memory
    Chroma vector store for retrieval-augmented generation.
    """

    #Load PDF content
    loader = PyPDFLoader(file.name)
    documents = loader.load()

    #Split document into semantically meaningful chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100
    )
    chunks = text_splitter.split_documents(documents)

    #Initialize local embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    #Create an in-memory vector store (session-scoped)
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vector_store
