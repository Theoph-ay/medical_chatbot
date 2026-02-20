from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_pdf(data):
    loader = PyPDFDirectoryLoader(data)

    documents = loader.load()
    return documents



#Create text chunks
def text_split(extracted_data):
    test_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
    )
    test_chunks = test_splitter.split_documents(extracted_data)
    return test_chunks


#download embedding model
def download_hugging_face_embeddings():
    emebeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return emebeddings


