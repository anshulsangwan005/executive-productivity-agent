from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .data import commitments, calendar, emails, voice_notes
from .agent import (
    answer_question,
    get_dashboard,
    get_open_items
)


app = FastAPI(
    title="Executive Productivity Agent",
    description="AI-powered productivity assistant for Arjun Malhotra",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Question(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "Executive Productivity Agent is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/dashboard")
def dashboard():
    return get_dashboard()


@app.get("/commitments")
def get_commitments():
    return commitments


@app.get("/open-items")
def open_items():
    return get_open_items()


@app.get("/calendar")
def get_calendar():
    return calendar


@app.get("/emails")
def get_emails():
    return emails


@app.get("/voice-notes")
def get_voice_notes():
    return voice_notes


@app.post("/ask")
def ask_agent(data: Question):

    answer = answer_question(data.question)

    return {
        "question": data.question,
        "answer": answer
    }