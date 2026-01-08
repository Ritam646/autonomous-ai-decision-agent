from agent.planner import plan
from agent.tools import web_search
from agent.memory import Memory
from agent.llm import get_llm
from agent.query_rewriter import rewrite_query

llm = get_llm()
memory = Memory()


def run_agent(goal: str):
    """
    Runs an autonomous decision-making agent with:
    - LLM-based planning
    - LLM-based query rewriting
    - Tool usage (web search)
    - Memory
    - Structured final decision
    """

    # 1️⃣ Plan tasks using LLM
    tasks = plan(goal)

    observations = []

    # 2️⃣ Execute tasks with rewritten search queries
    for task in tasks:
        search_query = rewrite_query(goal, task)
        search_results = web_search(search_query)

        observations.append({
            "task": task,
            "search_query": search_query,
            "results": search_results
        })

        memory.store({
            "task": task,
            "query": search_query,
            "results": search_results
        })

    # 3️⃣ LLM-based reasoning + decision (STRICT FORMAT)
    reasoning_prompt = f"""
You are a senior technical decision-making AI.

GOAL:
{goal}

OBSERVATIONS:
{observations}

Based on the observations, respond in EXACTLY the following format:

Final Recommendation:
<one clear recommendation>

Reasoning:
<clear explanation of why this is the best choice>

Pros:
- <point 1>
- <point 2>
- <point 3>

Cons:
- <point 1>
- <point 2>

When to choose the alternative:
- <scenario 1>
- <scenario 2>
"""

    decision_response = llm.invoke(reasoning_prompt)

    # 4️⃣ Final structured output
    return {
    "goal": goal,
    "tasks": tasks,
    "observations": observations,
    "final_decision": decision_response.content,
    "reasoning_trace": {
        "num_tasks": len(tasks),
        "num_tool_calls": len(observations),
        "memory_size": len(memory.retrieve())
    }
}

