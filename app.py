from flask import Flask, render_template, request, jsonify
from src.helper import download_hugging_face_embeddings
from src.prompt import prompt
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os

load_dotenv()

app = Flask(__name__)

embeddings = download_hugging_face_embeddings()
index_name = os.getenv("PINECONE_INDEX_NAME")
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

PROMPT = ChatPromptTemplate.from_template(prompt)

llm = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature = 0.8,
    api_key = os.getenv("GROQ_API_KEY"),
)
retriever = docsearch.as_retriever(search_kwargs={"k": 6})
llm_chain = create_stuff_documents_chain(llm, PROMPT)
qa = create_retrieval_chain(retriever, llm_chain)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.form.get("query")
    print(f"User asked: {msg}")
    response = qa.invoke({"input": msg})
    final_answer = response["answer"]
    print(f"AI Response: {final_answer}")
    return jsonify({"response": final_answer})

if __name__ == "__main__":
    app.run(debug=True)