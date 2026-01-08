from agent.llm import get_llm

llm = get_llm()

def plan(goal: str):
    """
    Generate domain-specific, actionable tasks.
    """

    prompt = f"""
You are a senior cloud architect planning an analysis task.

Goal:
{goal}

Create 4–6 SPECIFIC, ACTIONABLE subtasks focused on:
- Cloud pricing
- Free tier offerings
- Compute & storage services
- Ease of use for students
- Learning and ecosystem value

Rules:
- Do NOT include generic tasks like "understand the goal"
- Each task must be specific to AWS or GCP
- Output as a numbered list, one task per line
"""

    response = llm.invoke(prompt)

    tasks = []
    for line in response.content.split("\n"):
        line = line.strip()
        if line and line[0].isdigit():
            tasks.append(line)

    return tasks
