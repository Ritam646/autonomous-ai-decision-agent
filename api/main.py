from fastapi import FastAPI
from pydantic import BaseModel
from agent.graph import build_graph

app = FastAPI(title="Autonomous Decision Intelligence Agent")

graph = build_graph()

class GoalInput(BaseModel):
    goal: str

@app.post("/run-agent")
def run_agent(input: GoalInput):
    return graph.invoke({"goal": input.goal})
