from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_index_name = os.getenv("PINECONE_INDEX_NAME")
os.environ["PINECONE_API_KEY"] = pinecone_api_key

extracted_data = load_pdf("data")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

vectorstore = PineconeVectorStore.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    index_name=pinecone_index_name
)
