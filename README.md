# Medical-Chatbot 

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1.1-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://docker.com)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.27-00FF00)](https://langchain.com)
[![Google Gemini](https://img.shields.io/badge/Gemini_AI-Powered-4285F4?logo=google&logoColor=white)](https://gemini.google.com)
[![Pinecone](https://img.shields.io/badge/Vector_DB-Pinecone-430098)](https://pinecone.io)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co)
[![SentenceTransformers](https://img.shields.io/badge/Sentence_Transformers-Embeddings-1D8F73)](https://www.sbert.net)
[![RAG Architecture](https://img.shields.io/badge/Architecture-RAG-8A2BE2)](https://github.com/yyigitturan/Medical-Chatbot)

# 🎯 Overview

This project implements Retrieval-Augmented Generation (RAG) system specifically designed for medical knowledge queries. By combining Pinecone's vector database with Google's Gemini LLM, it provides accurate, contextually relevant medical information grounded in verified literature.

# ✨ Project Features

- RAG Implementation
  - Semantic Chunking: Intelligent document segmentation preserving medical context
  - Multi-vector Retrieval: Top-K similarity search with relevance scoring
  - Context-Aware Generation: Prompt engineering optimized for medical accuracy

- Production-Ready Architecture
   - Containerized Deployment: Docker support with multi-stage builds
   - Environment Management: Secure API key handling and configuration

# 📊 Project Workflow

![alt text](flow.png)

# 🖥️ Application Interface

<img width="1918" height="910" alt="image" src="https://github.com/user-attachments/assets/55bb0aa9-67c3-4e41-9491-7468ac5485f1" />


# 🚀 Tech Stack

<div align="left">

| Category | Technologies |
|----------|--------------|
| **🤖 AI Framework & Models** | `LangChain` `Gemini LLM` `Sentence Transformers` |
| **🗄️ Vector Database** | `Pinecone` `HuggingFace` |
| **🌐 Backend** | `Flask` `Flask-CORS` |
| **🎨 Frontend** | `HTML5` `CSS3` `JavaScript` |
| **📄 Document Processing** | `PyPDF` |
| **🔧 Development & Deployment** | `Docker` `Python-Dotenv` `Python 3.10+` |

</div>



# 🛠️ Installation & Setup

### Prerequisites
- Pinecone API account
- Google Gemini API key

## Steps: 

Clone the repository 

```bash 
git clone https://github.com/yyigitturan/Medical-Chatbot.git
```

### Step 01- Create a environment after opening the repository 

```bash 
python -m venv medicalbot
source medicalbot/bin/activate  
``` 
### Step 02- Install Dependencies

```bash 
pip install -r requirements.txt
``` 
### Step 03- Environment Configuration

Create a .env file with your API keys: 

```bash 
PINECONE_API_KEY=your_pinecone_api_key
GEMINI_API_KEY=your_gemini_api_key
``` 

### Step 04- Initialize Vector Database

```bash 
python store_index.py
``` 
### Step 05- Run the Application

```bash 
python app.py
``` 
## Docker Deployment
Build the Image

```bash 
docker build -t medical-chatbot .
``` 

Run the Container

```bash 
docker run -p 5000:5000 --env-file .env medical-chatbot
``` 
# 💡 Usage
Start the application

Access the web interface at http://localhost:5000

Enter medical questions like:

"How can acne be prevented?"




