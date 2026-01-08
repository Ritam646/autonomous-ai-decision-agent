from langgraph.graph import StateGraph
from agent.decision_agent import run_agent

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("agent", run_agent)
    graph.set_entry_point("agent")
    graph.set_finish_point("agent")

    return graph.compile()
