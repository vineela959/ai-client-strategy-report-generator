# 🚀 AI Client Strategy Report Generator

An end-to-end **AI-powered client strategy report generation system** that researches business requirements, generates strategic insights using AI, and creates a downloadable PDF report.

Built with **Python · FastAPI · Groq LLaMA · ReportLab · HTML/CSS/JavaScript · Render**

---

## 🌐 Live Demo

https://ai-client-strategy-report-generator.onrender.com/

---

## 🧠 What It Does

The application allows users to enter:

- Client name
- Industry
- Business goals

The AI agent then:

1. Analyzes the client requirements
2. Generates a structured business strategy
3. Creates a professional PDF report
4. Provides a download option

---

## 🔄 Workflow

```
User enters client details
          ↓
FastAPI receives request
          ↓
AI agent analyzes requirements
          ↓
Groq LLaMA generates strategy
          ↓
ReportLab creates PDF
          ↓
User downloads report
          ↓
Deployed on Render
```

---

## ✨ Features

✅ AI-powered strategy generation  
✅ Client-specific business analysis  
✅ Automatic PDF report creation  
✅ Downloadable reports  
✅ Simple web interface  
✅ FastAPI backend API  
✅ Production deployment  
✅ Environment variable support  

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn

### AI
- Groq API
- LLaMA Model

### Document Generation
- ReportLab

### Frontend
- HTML
- CSS
- JavaScript

### Deployment
- Render

---

## 📂 Project Structure

```
AI-Client-Strategy-Report-Generator
│
├── app.py
├── ai_agent.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── index.html
│
└── reports
    └── generated PDF files
```

---

## ⚙️ Installation & Setup

### Clone repository

```bash
git clone https://github.com/vineela959/ai-client-strategy-report-generator.git
```

Move into project folder:

```bash
cd ai-client-strategy-report-generator
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Locally

Start backend:

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

## 📌 API Endpoint

### Generate Strategy Report

```
POST /generate
```

Request:

```json
{
  "client_name": "ABC Technologies",
  "industry": "SaaS",
  "goals": "Improve customer growth using AI automation"
}
```

Response:

```json
{
  "strategy_report": "Generated AI strategy...",
  "pdf_file": "/reports/report.pdf"
}
```

---

## 🚀 Deployment

The application is deployed using Render.

Deployment configuration:

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

---

## 🔒 Security

- API keys stored using environment variables
- Secrets are not committed to GitHub
- `.env` files ignored using `.gitignore`

---

## 🎯 Project Purpose

This project demonstrates:

- Generative AI integration
- AI agent workflow design
- Backend API development
- Frontend-backend communication
- Automated document generation
- Cloud deployment

---
