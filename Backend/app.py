import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from  src.search import RAGSearch

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "status":"success",
        "Message":"Dstarix-Guider-Chatbot is live 🚀"
    })

@app.route("/chat", methods=["POST"])
def chat():
    rag = RAGSearch()
    data = request.get_json()
    question = data.get("question")
    if not question:
        return jsonify({"status": "error", "message": "Question is required"}), 400

    response = rag.search_and_summerize(query=question)
    return jsonify({"status": "success", "response": response})

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )