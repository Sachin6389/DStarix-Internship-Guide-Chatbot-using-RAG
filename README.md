# 🤖 DStarix Internship Guide Chatbot using RAG

## 📌 Project Title

**DStarix Internship Guide Chatbot using Retrieval-Augmented Generation (RAG)**

---

# 📖 Project Description

The **DStarix Internship Guide Chatbot** is an AI-powered chatbot built using **React.js**, **Flask**, **LangChain**, **FAISS**, and **Groq LLM**. It uses **Retrieval-Augmented Generation (RAG)** to answer user questions based on the DStarix Internship Guide PDF.

Instead of relying only on the LLM's knowledge, the chatbot retrieves the most relevant information from the internship guide using **Sentence Transformers embeddings** and **FAISS Vector Database**, then generates accurate and context-aware responses using **Groq's Llama model**.

The application provides a modern chat interface where users can ask internship-related questions such as project submission, evaluation process, internship rules, certificates, timelines, and guidelines. The chatbot searches the indexed document and returns precise answers based on the uploaded guide.

---

# ✨ Features

- 🤖 AI-powered Internship Guide Chatbot
- 📄 Retrieval-Augmented Generation (RAG)
- 📚 Answer questions from your own documents
- 📂 Supports multiple file formats
  - 📕 PDF (.pdf)
  - 📄 Text (.txt)
  - 📝 Markdown (.md)
  - 📊 Excel (.xlsx, .xls)
  - 📋 CSV (.csv)
  - 📑 JSON (.json)
- 🔍 Semantic Search using Sentence Transformers
- ⚡ Fast similarity search with FAISS Vector Database
- 🧠 Context-aware responses using Groq LLM
- 💬 Interactive real-time chat interface
- 📝 Markdown-formatted AI responses
- 📜 Chat history support
- 🎯 Accurate document-based question answering
- 🚀 Fast document retrieval and response generation
- 🎨 Modern and responsive React UI
- 🔥 Flask REST API backend
- 🔗 Frontend & Backend integration
- 🔒 Secure API key management using environment variables
- 📁 Easily extendable to new document types
  
  

---

# 🛠 Technologies Used

## Frontend

- React.js
- Vite
- Tailwind CSS
- Axios
- React Markdown
- Remark GFM



---

## Backend

- Flask
- Flask-CORS
- Gunicorn
- LangChain
- LangChain Core
- LangChain Community
- LangChain Groq
- FAISS
- Sentence Transformers
- NumPy
- Python Dotenv
- Python

---

## AI & RAG Stack

- Retrieval-Augmented Generation (RAG)
- FAISS Vector Database
- Sentence Transformers Embeddings
- Semantic Similarity Search
- Groq Llama Model
- LangChain Pipeline

---

## Development Tools

- Git
- GitHub
- VS Code
- Python Virtual Environment

---

# 📥 Installation Instructions

## 1. Clone Repository

```bash
git clone https://github.com/Sachin6389/DStarix-Internship-Guide-Chatbot-using-RAG.git

cd DStarix-Internship-Guide-Chatbot-using-RAG
```

---

# ⚙️ Backend Setup

Navigate to backend

```bash
cd backend
```

### Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file inside backend.

```env
GROQ_API_KEY=
```

---

### Build Vector Database

Run the indexing script once to create the FAISS vector database from the Internship Guide PDF.

```bash
python src/vectorStore.py
```

---

### Run Backend

```bash
python app.py
```

Backend runs on

```
[http://localhost:5000](http://127.0.0.1:5000/)
```

---

# ⚙️ Frontend Setup

Navigate to frontend

```bash
cd frontend
```

---

### Install Packages

```bash
npm install
```

---

### Configure Environment Variables

Create a `.env` file.

```env
VITE_BACKEND_URL=http://localhost:5000
```

---

### Start Development Server

```bash
npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# 🚀 How RAG Works

1. User asks a question.
2. Backend converts the query into embeddings.
3. FAISS performs semantic similarity search.
4. Relevant chunks are retrieved from the Internship Guide.
5. LangChain sends the retrieved context to Groq LLM.
6. Groq generates an accurate contextual response.
7. Response is displayed in the React chat interface.

---

# 🚀 Usage Guide

- Start the Flask backend.
- Start the React frontend.
- Open the application in your browser.
- Ask any internship-related question.
- The chatbot retrieves relevant content from the Internship Guide.
- The AI generates an accurate answer using RAG.
- The response is displayed in markdown format.

---

# 📂 Project Structure

```
DStarix-Internship-Guide-Chatbot-using-RAG/
│
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   ├── Components/
│   │   │   ├── Chatboat.jsx
│   │   │   ├── ChatInput.jsx
│   │   │   └── Message.jsx
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── Main.jsx
│   │   └── index.css
│   │
│   ├── public/
│   ├── .env
│   ├── Sample.env.txt
│   ├── vercel.json
│   ├── .gitignore
│   ├── package.json
│   └── vite.config.js
│
├── backend/
│   ├── app.py
|   ├── Documents
|   ├── faiss_store
│   ├── requirements.txt
│   ├── src
│   │    ├── __init__.py
│   │    ├── documentloader.py
│   │    ├── embedding.py 
│   │    ├── search.py
│   │    └── vectorStore.py
│   ├── .env
│   └── .gitignore
│
├── README.md
└── LICENSE
```

---

# 🔄 API Endpoint

## POST `/chat`

### Request

```json
{
  "question": "what is full name of company"
}
```

---

### Response

```json
{
  
"response": "The full name of the company is DStarix".
}
```

---

# 📸 Example Output

## User

```
how many months it's take for internship
```

## AI Response

```
The internship duration is 3 months.
```

---

# 🌍 Deployment

## Frontend

- Vercel

## Backend

- Render
- Railways

---

# 🔐 Environment Variables

## Backend

```env
GROQ_API_KEY=
```

## Frontend

```env
VITE_BACKEND_URL=http://localhost:5000
```

---



If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and motivates further improvements.
