from flask import Flask, render_template, request, jsonify
from src.helper import download_hugging_face_embeddings
from src.prompt import PROMPT
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

embeddings = download_hugging_face_embeddings()
vectorstore = PineconeVectorStore.from_existing_index(
    index_name=os.getenv("PINECONE_INDEX_NAME"),
    embedding=embeddings
)

qa_chain = load_qa_chain(embeddings)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    query = request.form["query"]
    docs = vectorstore.similarity_search(query, k=3)
    response = qa_chain.run(input_documents=docs, question=query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)