from __future__ import annotations

from datetime import datetime, UTC
from typing import List, Dict


class ExecutorAgent:
    """Executes a previously generated plan.

    This demo simulates execution and produces structured logs plus a final output.
    """

    def execute_plan(self, task: str, plan: List[dict]) -> Dict:
        if not plan:
            raise ValueError("Execution plan cannot be empty")

        step_results = []
        collected_notes = []

        for step in plan:
            note = self._simulate_step(task=task, step=step)
            step_results.append(
                {
                    "step_id": step["step_id"],
                    "title": step["title"],
                    "status": "done",
                    "details": note,
                    "timestamp_utc": datetime.now(UTC).isoformat(),
                }
            )
            collected_notes.append(f"Step {step['step_id']} - {step['title']}: {note}")

        final_output = self._build_final_output(task, collected_notes)

        return {
            "step_results": step_results,
            "final_output": final_output,
        }

    @staticmethod
    def _simulate_step(task: str, step: dict) -> str:
        return (
            f"Executed '{step['title']}' for task '{task}'. "
            f"Action summary: {step['description']}"
        )

    @staticmethod
    def _build_final_output(task: str, notes: List[str]) -> str:
        notes_block = "\n".join(f"- {note}" for note in notes)
        return (
            f"Task completed successfully: {task}\n\n"
            f"Execution summary:\n{notes_block}\n\n"
            "This output demonstrates a basic agent orchestration workflow where a planner "
            "decomposes a task and an executor processes each step in sequence."
        )
