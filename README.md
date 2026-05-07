# MedPulse AI – Real-Time Pharmacovigilance Intelligence System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![AI](https://img.shields.io/badge/AI-Groq-orange)
![Frontend](https://img.shields.io/badge/Frontend-Vercel-black)
![Backend](https://img.shields.io/badge/Backend-Railway-purple)
![Status](https://img.shields.io/badge/Status-Live-success)
![License](https://img.shields.io/badge/License-Hackathon-lightgrey)

---

# MedPulse AI

MedPulse AI is a real-time pharmacovigilance intelligence platform designed to monitor, analyze, and detect adverse drug reactions (ADRs) from online social media discussions using artificial intelligence.

The system continuously tracks signals from platforms like Reddit, Twitter/X, and Quora, processes unstructured healthcare discussions, and converts them into actionable pharmacovigilance insights.

---

# Live Deployment

## Frontend (Vercel)

🌐 https://ai-for-bharat-hackathon-med-pulse-9rqwim5j1.vercel.app/

---

## Backend API (Railway)

🌐 https://ai-for-bharat-hackathon-medpulseai-production.up.railway.app/

---

# Overview

Traditional pharmacovigilance systems rely heavily on delayed manual reporting, causing slow identification of adverse drug reactions.

MedPulse AI solves this problem by:

- Monitoring real-time social media discussions
- Detecting possible drug-related adverse events
- Classifying severity levels using AI
- Providing live dashboard analytics
- Generating AI-powered medical insights
- Tracking healthcare sentiment trends

---

# Problem Statement

Traditional pharmacovigilance systems face several challenges:

- Delayed adverse event detection
- Underreporting of patient experiences
- Lack of real-time monitoring
- Difficulty analyzing unstructured medical discussions
- Manual analysis limitations
- Poor scalability for social media surveillance

---

# Proposed Solution

MedPulse AI introduces an AI-powered real-time surveillance system capable of:

- Real-time social media signal monitoring
- AI-driven adverse drug reaction detection
- Drug severity classification
- Sentiment and trend analysis
- Intelligent signal summarization
- Interactive dashboard visualization
- AI-powered pharmacovigilance assistant

---

# Key Features

## Real-Time Monitoring Dashboard
- Live signal tracking
- Active alert monitoring
- Drug trend visualization
- Severity analytics

## AI-Powered Agent Chat
- Interactive pharmacovigilance assistant
- Natural language querying
- AI-generated insights
- Signal summarization

## Adverse Event Detection
- Automatic ADR identification
- Severity classification:
  - Low
  - Medium
  - High
  - Critical

## Multi-Source Signal Feed
- Reddit monitoring
- Twitter/X monitoring
- Quora monitoring

## Data Visualization
- Signal trend charts
- Source distribution analytics
- Sentiment analysis graphs
- Drug comparison insights

## Project-Based Monitoring
- Drug-specific tracking
- Signal grouping
- Alert management

---

# How It Works

1. Social media signals are collected
2. Backend processes incoming discussions
3. AI analyzes medical relevance
4. Severity is classified
5. Insights are generated
6. Dashboard updates in real-time

---

# System Architecture

```text
Frontend (HTML/CSS/JS)
          ↓
     FastAPI Backend
          ↓
     Groq AI Engine
          ↓
 Signal Processing Layer
          ↓
 Dashboard Visualization
```

---

# Tech Stack

## Frontend
- HTML5
- CSS3
- JavaScript

## Backend
- Python
- FastAPI
- Uvicorn

## AI & NLP
- Groq API
- LLM-based analysis

## Deployment
- Vercel (Frontend)
- Railway (Backend)

## Data Sources
- Reddit
- Twitter/X
- Quora

---

# Project Structure

```text
.
├── index.html
├── main.py
├── requirements.txt
├── run.bat
├── .env
├── .gitignore
```

---

# Architecture Diagram

<img width="1536" height="1024" alt="Architecture Diagram" src="https://github.com/user-attachments/assets/17495eb2-105f-4de3-8fa1-9594aa3e362b" />

---

# Application Screenshots

---

## Dashboard Overview

<img width="1910" height="907" alt="image" src="https://github.com/user-attachments/assets/d5628478-d178-4150-a592-8314375f6344" />


Features shown:
- Total signals
- Adverse event analytics
- Severity monitoring
- Source distribution
- AI insights
- Sentiment trends

---

## Signal Feed

<img width="1919" height="906" alt="image" src="https://github.com/user-attachments/assets/43acebf8-eb3c-4acd-855b-317b228cf3a0" />


Features shown:
- Live Reddit signals
- Twitter/X signals
- Real-time healthcare discussions
- NLP analysis integration

---

## Monitoring Projects

<img width="1918" height="899" alt="image" src="https://github.com/user-attachments/assets/73df61a2-deaa-496b-840c-51d55f543080" />


Features shown:
- Drug monitoring projects
- Alert tracking
- Signal grouping
- Project management

---

## Adverse Event Alerts

<img width="1918" height="907" alt="image" src="https://github.com/user-attachments/assets/8454f439-a934-48e8-9741-3e31d818b037" />


Features shown:
- Critical event detection
- Severity tagging
- Drug-specific alerts
- Live pharmacovigilance monitoring

---

## AI Agent Chat

<img width="1912" height="908" alt="image" src="https://github.com/user-attachments/assets/2cd66943-0b4d-4ebd-b3ba-1044792da7fc" />


Features shown:
- AI pharmacovigilance assistant
- Drug safety Q&A
- AI-generated summaries
- Intelligent signal analysis

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/Harshit-0018/AI-For-Bharat-Hackathon-MedPulseAi.git
cd AI-For-Bharat-Hackathon-MedPulseAi
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Setup Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## 4. Run Backend

```bash
uvicorn main:app --reload --port 8000
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

## 5. Run Frontend

```bash
python -m http.server 5500
```

Frontend runs at:

```text
http://127.0.0.1:5500
```

---

# Deployment

## Frontend Deployment (Vercel)

Frontend successfully deployed on Vercel:

```text
https://ai-for-bharat-hackathon-med-pulse-9rqwim5j1.vercel.app/
```

---

## Backend Deployment (Railway)

Backend API successfully deployed on Railway:

```text
https://ai-for-bharat-hackathon-medpulseai-production.up.railway.app/
```

---

# API Health Check

Backend health endpoint:

```text
GET /
```

Response:

```json
{
  "status": "MedPulse API running"
}
```

---

# Use Cases

- Pharmacovigilance automation
- Drug safety monitoring
- Public health analytics
- Social media healthcare intelligence
- Adverse drug reaction detection
- Healthcare AI analytics

---

# Future Improvements

- Real-time Twitter API integration
- Database integration
- Authentication system
- Docker containerization
- Alert notification system
- Advanced ML models
- PDF report generation
- Multi-user support
- Admin dashboard

---

# Achievements

✅ Successfully deployed frontend on Vercel  
✅ Successfully deployed backend on Railway  
✅ Integrated Groq AI successfully  
✅ Real-time AI chat implemented  
✅ Multi-page healthcare dashboard created  
✅ Adverse event detection system working  
✅ Responsive modern UI completed  

---

# Author

## Harshit

GitHub:
https://github.com/Harshit-0018

---

# License

This project was developed for hackathon purposes and is open for learning, research, and demonstration.

---
