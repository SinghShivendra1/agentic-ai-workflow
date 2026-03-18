from __future__ import annotations

import argparse
import json
from pathlib import Path

from agents.executor import ExecutorAgent
from agents.planner import PlannerAgent
from utils.logger import get_logger

logger = get_logger(__name__)


def load_task_from_file(path: str) -> str:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Task file not found: {path}")
    return file_path.read_text(encoding="utf-8").strip()


def run_workflow(task: str, use_mock_llm: bool = True) -> dict:
    planner = PlannerAgent(use_mock_llm=use_mock_llm)
    executor = ExecutorAgent()

    logger.info("Starting agentic workflow")
    logger.info("Input task: %s", task)

    plan = planner.create_plan(task)
    execution = executor.execute_plan(task=task, plan=plan)

    result = {
        "task": task,
        "plan": plan,
        "execution": execution,
        "status": "completed",
    }

    logger.info("Workflow completed successfully")
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a simple multi-agent AI workflow with planner + executor agents."
    )
    parser.add_argument(
        "--task",
        type=str,
        help="Task to execute. Example: 'Write a short blog outline on AI in healthcare'",
    )
    parser.add_argument(
        "--task-file",
        type=str,
        help="Optional path to a text file containing the task.",
    )
    parser.add_argument(
        "--real-llm",
        action="store_true",
        help="Reserved for real LLM integration. Current demo uses mock planning logic.",
    )
    parser.add_argument(
        "--save",
        type=str,
        default="",
        help="Optional path to save the JSON result.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not args.task and not args.task_file:
        raise ValueError("Provide either --task or --task-file")

    task = args.task or load_task_from_file(args.task_file)
    result = run_workflow(task=task, use_mock_llm=not args.real_llm)

    print("\n=== FINAL RESULT ===")
    print(json.dumps(result, indent=2, ensure_ascii=False))

    if args.save:
        output_path = Path(args.save)
        output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nSaved result to: {output_path}")


if __name__ == "__main__":
    main()
