from setuptools import setup, find_packages

setup(
    name="medical-chatbot",
    version="0.1.0",
    packages=find_packages(),
    author = "Theophilus Olayiwola",
    install_requires=[
        "langchain",
        "langchain-groq",
        "langchain-community",
        "langchain-core",
        "langchain-classic",
        "sentence-transformers",
        "langchain_text_splitters",
        "python-dotenv",
        "flask",
        "pypdf",
        "langchain-pinecone",
        "pinecone-client",
    ],
)
