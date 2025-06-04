# backend/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "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"  # Replace with your actual API key or load from env

class TaskRequest(BaseModel):
    description: str

@app.post("/generate")
def generate_mermaid(task: TaskRequest):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are a strict Mermaid code generator.

ONLY respond with Mermaid flowchart code in this format:

\\`\\`\\`mermaid
flowchart TD
  A[Start] --> B[Next Step]
  B --> C[Final Step]
\\`\\`\\`

DO NOT add explanations, comments, or alternate versions.

Convert this description into a Mermaid flowchart:

"{task.description}"
"""

    data = {
        "model": "mistralai/mixtral-8x7b",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        content = response.json()['choices'][0]['message']['content']
        # Strip ```mermaid block
        clean_code = content.strip("```").replace("mermaid", "").strip()
        return {"code": clean_code}
    else:
        return {"error": response.text}
