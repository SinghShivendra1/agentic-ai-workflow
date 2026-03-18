from agents.planner import PlannerAgent


def test_planner_returns_list():
    planner = PlannerAgent()
    plan = planner.create_plan("Write a short blog on AI in healthcare")

    assert isinstance(plan, list)
    assert len(plan) > 0


def test_each_plan_step_has_required_fields():
    planner = PlannerAgent()
    plan = planner.create_plan("Write a short blog on AI in healthcare")

    for step in plan:
        assert "step_id" in step
        assert "title" in step
        assert "description" in step


def test_step_ids_are_ordered():
    planner = PlannerAgent()
    plan = planner.create_plan("Write a short blog on AI in healthcare")

    step_ids = [step["step_id"] for step in plan]
    assert step_ids == sorted(step_ids)


def test_empty_task_still_returns_plan_or_handles_cleanly():
    planner = PlannerAgent()
    plan = planner.create_plan("")

    assert isinstance(plan, list)
