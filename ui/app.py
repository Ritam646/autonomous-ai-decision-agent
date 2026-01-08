import streamlit as st
import requests

API_URL = "http://localhost:8000/run-agent"

st.set_page_config(page_title="Autonomous Decision Agent")

st.title("🧠 Autonomous Decision Intelligence Agent")

goal = st.text_input("Enter your decision goal")

if st.button("Run Agent"):
    response = requests.post(API_URL, json={"goal": goal})

    if response.status_code == 200:
        data = response.json()

        st.subheader("📋 Tasks Planned")
        for t in data["tasks"]:
            st.write("-", t)

        st.subheader("🔍 Analysis")
        for item in data["analysis"]:
            st.write(f"**{item['task']}**")
            for res in item["results"]:
                st.write("-", res)

        st.subheader("✅ Final Decision")
        st.success(data["decision"])
import streamlit as st
import requests

API_URL = "http://localhost:8000/run-agent"

st.set_page_config(page_title="Autonomous Decision Agent", layout="wide")

st.title("🧠 Autonomous Decision Intelligence Agent")
st.write("Goal-agnostic agent with planning, tool use, and explainable reasoning")

goal = st.text_input("Enter your decision goal")

if st.button("Run Agent") and goal:
    with st.spinner("Agent is thinking..."):
        response = requests.post(API_URL, json={"goal": goal})

    if response.status_code == 200:
        data = response.json()

        st.subheader("🎯 Goal")
        st.info(data["goal"])

        # ---- PLANNER OUTPUT ----
        st.subheader("🧩 Planned Tasks")
        for t in data["tasks"]:
            st.write("•", t)

        # ---- TOOL USAGE ----
        st.subheader("🔎 Tool Usage & Evidence")
        for obs in data["observations"]:
            with st.expander(f"Task: {obs['task']}"):
                st.markdown(f"**Search Query Used:** `{obs['search_query']}`")
                if obs["results"]:
                    for r in obs["results"]:
                        st.write("–", r)
                else:
                    st.warning("No strong evidence found for this step.")

        # ---- FINAL DECISION ----
        st.subheader("✅ Final Decision")
        st.success(data["final_decision"])

        # ---- TRACE META ----
        st.subheader("📊 Reasoning Trace Summary")
        st.json(data["reasoning_trace"])

    else:
        st.error("Agent API error")
