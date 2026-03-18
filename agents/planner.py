from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class PlanStep:
    step_id: int
    title: str
    description: str


class PlannerAgent:
    """Breaks a high-level task into structured executable steps.

    In production, this class could call an LLM. In this portfolio project,
    it uses deterministic mock logic so the project runs without external keys.
    """

    def __init__(self, use_mock_llm: bool = True) -> None:
        self.use_mock_llm = use_mock_llm

    def create_plan(self, task: str) -> List[dict]:
        cleaned_task = task.strip()
        if not cleaned_task:
            raise ValueError("Task cannot be empty")

        lowered = cleaned_task.lower()

        if any(word in lowered for word in ["blog", "article", "write", "content"]):
            steps = [
                PlanStep(1, "Understand task", "Identify audience, intent, and desired output format."),
                PlanStep(2, "Research key points", "List the main ideas or arguments to include."),
                PlanStep(3, "Create structure", "Build an outline with sections and supporting details."),
                PlanStep(4, "Draft output", "Produce the requested written content in concise form."),
                PlanStep(5, "Review", "Check clarity, completeness, and consistency."),
            ]
        elif any(word in lowered for word in ["analyze", "analysis", "data", "dataset"]):
            steps = [
                PlanStep(1, "Inspect input", "Understand the data source, fields, and expected result."),
                PlanStep(2, "Preprocess", "Clean data and handle missing or invalid values."),
                PlanStep(3, "Analyze", "Extract patterns, trends, or summary statistics."),
                PlanStep(4, "Summarize", "Convert findings into actionable conclusions."),
            ]
        else:
            steps = [
                PlanStep(1, "Understand objective", "Clarify the goal and expected deliverable."),
                PlanStep(2, "Break down task", "Split the request into smaller actionable subtasks."),
                PlanStep(3, "Execute subtasks", "Perform each subtask in a logical order."),
                PlanStep(4, "Compile result", "Combine outputs into a final structured response."),
            ]

        return [step.__dict__ for step in steps]
