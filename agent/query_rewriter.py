from agent.llm import get_llm

llm = get_llm()

def rewrite_query(goal: str, task: str) -> str:
    prompt = f"""
    You are an expert search query optimizer.

    Goal: {goal}
    Task: {task}

    Generate ONE concise web search query that would return
    relevant technical or comparative information.

    Return ONLY the query.
    """

    response = llm.invoke(prompt)
    return response.content.strip()
