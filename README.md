# MedPulse AI – Real-Time Pharmacovigilance Intelligence System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![AI](https://img.shields.io/badge/AI-Groq-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-Hackathon-lightgrey)

---

## Overview

MedPulse AI is a real-time pharmacovigilance platform that uses artificial intelligence to monitor, analyze, and interpret patient-reported drug experiences from social media.

It converts unstructured online discussions into actionable insights, enabling early detection of adverse drug reactions (ADRs).

---

## Problem Statement

Traditional pharmacovigilance systems face several limitations:

- Delayed detection of adverse drug reactions  
- Underreporting of patient experiences  
- Lack of real-time monitoring  
- Difficulty analyzing unstructured data  

---

## Proposed Solution

MedPulse AI:

- Monitors social media signals in real time  
- Detects adverse drug reactions using AI  
- Classifies severity (Low, Medium, High, Critical)  
- Tracks sentiment and trends  
- Provides AI-powered insights  
- Visualizes data via dashboard  

---

## How It Works

1. Data is collected from multiple sources (Reddit, Twitter/X, Quora)  
2. Backend processes incoming signals  
3. AI analyzes sentiment and medical relevance  
4. System classifies severity of events  
5. Insights are displayed on dashboard  

---

## System Architecture

```
Frontend (UI)
   ↓
FastAPI Backend
   ↓
Groq AI Processing
   ↓
Signal Analysis
   ↓
Dashboard Visualization
```

---

## Project Structure

```
.
├── index.html
├── main.py
├── requirements.txt
├── run.bat
├── .env
├── .gitignore
```

---

## Tech Stack

### Frontend
- HTML5  
- CSS3  
- JavaScript  

### Backend
- Python  
- FastAPI  

### AI & Processing
- Groq API  

### Data Handling
- REST APIs  
- Environment variables  

---

## Architecture

<img width="1536" height="1024" alt="ChatGPT Image May 3, 2026, 07_23_51 PM" src="https://github.com/user-attachments/assets/17495eb2-105f-4de3-8fa1-9594aa3e362b" />

---

## Features

- Real-time monitoring dashboard  
- AI-powered agent chat  
- Adverse event detection  
- Sentiment trend visualization  
- Signal feed from multiple sources  
- Severity classification system  
- Project-based monitoring  
- Source distribution analytics  

---

## Use Cases

- Drug safety monitoring  
- Early adverse event detection  
- Healthcare analytics  
- Pharmacovigilance automation  
- Public health monitoring  

---

## Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/Harshit-0018/AI-For-Bharat-Hackathon-MedPulseAi.git
cd AI-For-Bharat-Hackathon-MedPulseAi
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Setup Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 4. Run Backend

```
uvicorn main:app --reload --port 8000
```

---

### 5. Run Frontend

```
python -m http.server 5500
```

---

### 6. Open in Browser

```
http://localhost:5500
```

---

## Future Improvements

- Integration with real-world APIs  
- Alert and notification system  
- Database support  
- Authentication system  
- Deployment (Docker / Cloud)  
- Advanced ML models  

---

## Author

Harshit  

---

## License

This project is created for hackathon purposes and is open for learning and demonstration.
