# agentic-ai-workflow

## Overview
This project demonstrates a simple multi-agent AI workflow using a **Planner Agent** and an **Executor Agent**.

The system takes a user task, breaks it into smaller steps, executes those steps in order, logs the execution, and produces a final structured output.

This project showcase:
- agent orchestration
- modular Python code structure
- logging and execution tracing
- clean project organization
- interview-friendly documentation

## Why This Project Matters
Modern AI systems increasingly use **agent-based workflows** rather than one-shot prompts. This repository simulates how a real-world automation system can:
- receive a high-level request
- decompose it into subtasks
- pass work between agents
- track progress and results

## Architecture
```text
User Task
Planner Agent
Structured Plan
Executor Agent
Final Output + Logs
```

## Features
- Planner agent for task decomposition
- Executor agent for step-by-step execution
- JSON-style final output
- Local logging for traceability
- Easy extension for real LLM APIs later
- Clean structure suitable for GitHub recruiters and interviews

## Example Input
```text
Write a short blog outline on how agentic AI can improve customer support workflows.
```

## Example Run
```bash
python main.py --task-file examples/sample_task.txt
```

## Example Output
```json
{
  "task": "Write a short blog outline on how agentic AI can improve customer support workflows.",
  "plan": [
    {
      "step_id": 1,
      "title": "Understand task",
      "description": "Identify audience, intent, and desired output format."
    }
  ],
  "execution": {
    "step_results": [],
    "final_output": "..."
  },
  "status": "completed"
}
```

## How to Run
1. Clone the repository
2. Move into the project folder
3. Run the workflow

```bash
git clone <your-repo-url>
cd agentic-ai-workflow
python main.py --task "Write a short blog on AI in healthcare"
```

## Future work to Extend
- integrating OpenAI or another LLM API inside `PlannerAgent`
- adding a reviewer agent
- storing execution results in a database
- exposing the workflow as a FastAPI service
- adding unit tests for each agent

## Tech Stack
- Python
- argparse
- logging
- modular OOP structure


