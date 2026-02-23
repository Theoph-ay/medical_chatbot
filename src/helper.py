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


def download_hugging_face_embeddings():
    # This creates a folder in the project called 'model_cache'
    # It will download from the internet the VERY FIRST time, 
    # and load instantly from the hard drive every time after that.
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        cache_folder="./model_cache" 
    )
    return embeddings

