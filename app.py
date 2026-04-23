import streamlit as st
from graph import graph

st.title("🎬 AutoStream LangGraph Agent")

if "state" not in st.session_state:
    st.session_state.state = {
        "stage": "start",
        "name": None,
        "email": None,
        "platform": None
    }

user_input = st.text_input("You:")

if user_input:
    st.session_state.state["user_input"] = user_input

    result = graph.invoke(st.session_state.state)

    st.session_state.state.update(result)

    st.write("Bot:", result["response"])