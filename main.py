from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import groq
import random
import os
from dotenv import load_dotenv
import time
from datetime import datetime, timedelta
import json

app = FastAPI(title="MedPulse API")

load_dotenv()
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

mock_social_posts = [
    {"id": "1", "source": "Reddit", "subreddit": "r/diabetes", "text": "Been on Metformin for 3 months now. Getting really bad nausea every morning, sometimes vomiting. My doctor said it should pass but it's been weeks.", "author": "u/[redacted]", "upvotes": 47, "ts": (datetime.now() - timedelta(hours=2)).isoformat()},
    {"id": "2", "source": "Reddit", "subreddit": "r/AskDocs", "text": "My father started Lisinopril last week for blood pressure. He's developed a persistent dry cough that won't go away. Is this related to the medication?", "author": "u/[redacted]", "upvotes": 23, "ts": (datetime.now() - timedelta(hours=5)).isoformat()},
    {"id": "3", "source": "Twitter/X", "subreddit": "—", "text": "Day 14 on Ozempic. Lost 4kg but dealing with severe constipation and abdominal pain. Anyone else? Should I call my doctor? #Ozempic #weightloss", "author": "@[redacted]", "upvotes": 112, "ts": (datetime.now() - timedelta(hours=1)).isoformat()}
]

active_projects_list = [
    {"id": "p1", "name": "Ozempic / Semaglutide Watch", "keywords": ["ozempic", "semaglutide", "wegovy"], "sources": ["Reddit", "Twitter/X", "Quora"], "frequency": "realtime", "signal_count": 234, "alert_count": 12, "created": "2026-04-01"}
]

class AnalyzeSignalRequest(BaseModel):
    post_id: str
    text: str

class ProjectCreationRequest(BaseModel):
    name: str
    keywords: list[str]
    sources: list[str]
    frequency: str

class AgentChatRequest(BaseModel):
    messages: list[dict]
    system: Optional[str] = None

@app.get("/")
def root():
    return {"status": "MedPulse API running"}

@app.get("/projects")
def get_projects():
    return active_projects_list

@app.post("/projects")
def create_project(project_data: ProjectCreationRequest):
    new_project_entry = {
        "id": f"p{len(active_projects_list)+1}",
        "name": project_data.name,
        "keywords": project_data.keywords,
        "sources": project_data.sources,
        "frequency": project_data.frequency,
        "signal_count": 0,
        "alert_count": 0,
        "created": datetime.now().strftime("%Y-%m-%d"),
    }
    active_projects_list.append(new_project_entry)
    return new_project_entry

@app.get("/signals")
def get_signals(source: Optional[str] = None, severity: Optional[str] = None):
    filtered_posts_list = mock_social_posts
    if source:
        filtered_posts_list = [post_item for post_item in filtered_posts_list if post_item["source"] == source]
    return filtered_posts_list

@app.post("/signals/analyze")
def analyze_signal(analysis_request: AnalyzeSignalRequest):
    analysis_prompt = f"""You are a pharmacovigilance NLP analyst. Analyze this social media post and return a JSON object with these fields:
- entities: list of {{name, type}} where type is one of: Drug, Symptom, Condition, Dosage
- sentiment: one of: Positive, Neutral, Negative, Mixed
- sentiment_score: float from -1.0 (very negative) to 1.0 (very positive)
- adverse_event_detected: boolean
- adverse_event_severity: one of: None, Low, Medium, High, Critical
- adverse_event_description: brief description if detected, else null
- pii_detected: boolean
- pii_types: list of PII types found (e.g. ["Name", "Age"])
- confidence: float 0.0 to 1.0
- summary: one sentence clinical summary

Post: "{analysis_request.text}"

Respond ONLY with valid JSON, no markdown, no explanation."""

    try:
        groq_message_response = client.chat.completions.create(
            model="llama3-70b-8192",
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": analysis_prompt}]
        )
        parsed_analysis_result = json.loads(groq_message_response.choices[0].message.content)
        parsed_analysis_result["post_id"] = analysis_request.post_id
        return parsed_analysis_result
    except Exception as api_exception:
        raise HTTPException(status_code=500, detail=str(api_exception))

@app.get("/stats")
def get_stats():
    return {
        "total_signals": 1247,
        "adverse_events": 89,
        "high_severity": 14,
        "sources_active": 3,
        "signals_today": 47,
        "pii_redacted": 203,
    }

@app.get("/trends")
def get_trends():
    seven_day_trends_list = []
    base_start_date = datetime.now() - timedelta(days=6)
    for day_index in range(7):
        current_trend_date = base_start_date + timedelta(days=day_index)
        seven_day_trends_list.append({
            "date": current_trend_date.strftime("%b %d"),
            "signals": random.randint(120, 280),
            "adverse": random.randint(8, 25),
            "positive": random.randint(30, 80),
            "negative": random.randint(50, 120),
        })
    return seven_day_trends_list

@app.post("/agent/chat")
def agent_chat(chat_request: AgentChatRequest):
    try:
        system_prompt = chat_request.system if chat_request.system else \
            "You are a pharmacovigilance AI assistant. Highlight drug safety risks clearly."

        user_messages = chat_request.messages if chat_request.messages else [
            {"role": "user", "content": "Hello"}
        ]

        formatted_messages = [{"role": "system", "content": system_prompt}] + user_messages

        groq_chat_response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=formatted_messages,
            temperature=0.7
        )

        return {
            "response": groq_chat_response.choices[0].message.content
        }

    except Exception as e:
        print("🚨 GROQ ERROR:", e)
        return {
            "response": "⚠️ AI service temporarily unavailable"
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)
