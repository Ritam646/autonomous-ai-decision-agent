import streamlit as st
import requests


st.set_page_config(
    page_title="Autonomous Decision Intelligence Agent",
    layout="wide"
)

API_URL = "https://autonomous-decision-agent-api.onrender.com/run-agent"

st.title("🧠 Autonomous Decision Intelligence Agent")
st.write(
    "Goal-agnostic agent with **planning**, **tool usage**, and "
    "**explainable reasoning**"
)


goal = st.text_input(
    "Enter your decision goal",
    key="decision_goal_input"
)

run_agent = st.button(
    "Run Agent",
    key="run_agent_button"
)


if run_agent and goal:

    with st.spinner("🤖 Agent is thinking..."):
        response = requests.post(
            API_URL,
            json={"goal": goal},
            timeout=120
        )

    if response.status_code != 200:
        st.error("❌ Agent API failed")
    else:
        data = response.json()

        
        st.subheader("🎯 Goal")
        st.info(data["goal"])

        
        st.subheader("🧩 Planned Tasks")
        for idx, task in enumerate(data["tasks"], start=1):
            st.write(f"{idx}. {task}")

        
        st.subheader("🔍 Tool Usage & Evidence")

        for obs in data["observations"]:
            with st.expander(f"Task: {obs['task']}"):
                st.markdown(
                    f"**Search Query:** `{obs['search_query']}`"
                )

                if obs["results"]:
                    for r in obs["results"]:
                        st.write("•", r)
                else:
                    st.warning("No strong evidence found.")

        st.subheader("✅ Final Decision")
        st.success(data["final_decision"])

    
        st.subheader("📊 Reasoning Trace Summary")
        st.json(data["reasoning_trace"])
