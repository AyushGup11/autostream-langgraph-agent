# 🚀 AutoStream LangGraph Agent

## 📌 Overview

AutoStream LangGraph Agent is an AI-powered chatbot built using LangGraph and Retrieval-Augmented Generation (RAG).
It can answer user queries from a knowledge base, detect user intent, and capture leads through a multi-step conversation flow.

---

## ✨ Features

* 🤖 AI Chatbot (LLM-powered)
* 🔍 RAG using FAISS vector database
* 🧠 Intent Detection (greeting, query, high intent)
* 🧾 Lead Capture Flow (name → email → platform)
* 💬 Multi-turn conversation handling
* ⚡ Fast inference using Groq (LLaMA 3.3)
* 🎨 Simple UI using Streamlit

---

## 🏗️ Tech Stack

* LangGraph – Agent workflow orchestration
* LangChain – LLM integration
* FAISS – Vector database
* HuggingFace Embeddings – Text embeddings
* Groq (LLaMA 3.3) – LLM
* Streamlit – Frontend UI
* Python – Backend

---

## 📂 Project Structure

AutoStream-Agent/
│── app.py              # Streamlit UI
│── graph.py            # LangGraph workflow
│── rag.py              # RAG + vector store
│── state.py            # Agent state schema
│── tools.py            # Lead capture tool
│── data.json           # Knowledge base
│── .env                # API keys
│── requirements.txt    # Dependencies

---

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone <https://github.com/AyushGup11/autostream-langgraph-agent.git>
cd AutoStream-Agent

### 2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Add API Key

Create a .env file:
I chose Groq as my LLM since I don’t have access to paid API keys at the moment. If needed, I can easily adapt the system to use the specified models.
GROQ_API_KEY=your_api_key_here

### 5. Run Application

streamlit run app.py

---

## 🧠 How It Works

1. User input is classified into intent (greeting, query, high intent)
2. Query → RAG retrieves relevant context from FAISS
3. LLM generates grounded response
4. High intent → lead capture flow is triggered

---

## 🧪 Example Queries

Hi
What is your pricing?
What features are included?
I want to buy a plan

---

## 🎯 Use Cases

* Customer support chatbot
* SaaS assistant
* Lead generation bot
* Knowledge-based AI assistant

---

## ⚡ Key Highlights

* No hallucination (strict RAG grounding)
* Multi-step conversational agent
* Clean and scalable architecture
* Production-style implementation

---

## 👨‍💻 Author

Ayush Gupta

---

## ⭐ Future Improvements

* Database integration for leads
* Deployment (Streamlit Cloud / AWS)
* Advanced memory handling
* Authentication system

---
