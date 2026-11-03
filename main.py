
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

app = FastAPI(title="Job Skill Analyzer")


class JobRequest(BaseModel):
    job_description: str


@app.get("/")
def home():
    return {"message": "Job Skill Analyzer is running!"}


@app.post("/analyze")
def analyze_job(job: JobRequest):
    description = job.job_description

    return {
        "message": "Job description received successfully!",
        "job_description": description
    }
