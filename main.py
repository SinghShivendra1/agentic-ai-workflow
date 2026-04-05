from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.service import run_workflow

# intialize fast api with meta data
app = FastAPI(
    title="AI Task API",
    description="FastAPI service for running an agentic AI workflow.",
    version="1.0.0",
)

#Define request schema, this ensures input validation and structured data handling
class TaskRequest(BaseModel):
    task: str = Field(..., min_length=1, description="Task to process")

# Root Endpoint
@app.get("/")
def root():
    return {
        "message": "AI Task API is running",
        "docs": "/docs",
        "health": "/health",
    }

# Health check endpoint, used by monitoring tools
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Main endpoint to process task
@app.post("/task")
def process_task(request: TaskRequest):
    result = run_workflow(request.task)
    return result
