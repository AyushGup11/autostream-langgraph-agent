from langgraph.graph import StateGraph, END
from state import AgentState
from rag import load_vectorstore, retrieve
from tools import mock_lead_capture
from langchain_groq import ChatGroq
import os

from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)
vectorstore = load_vectorstore()

# ---- NODE 1: Intent Detection ----
def detect_intent(state: AgentState):
    user_input = state["user_input"]

    prompt = f"""
    Classify the user intent into ONLY one word:

    greeting
    query
    high_intent

    User: {user_input}

    Answer ONLY one word.
    """

    intent = llm.invoke(prompt).content.lower()

    return {"intent": intent}


# ---- NODE 2: RAG ----
import json

def rag_node(state: AgentState):
    user_input = state["user_input"].lower()

    
    if "pricing" in user_input:
        with open("data.json") as f:
            data = json.load(f)

        pricing_text = ""

        for name, details in data["pricing"].items():
            pricing_text += (
                f"{name.upper()}:\n"
                f"- Price: {details['price']}\n"
                f"- Features: {', '.join(details['features'])}\n\n"
            )

        return {"response": pricing_text.strip()}

    # fallback to RAG
    context = retrieve(state["user_input"], vectorstore)

    prompt = f"""
    You are a strict assistant.

    ONLY answer from the provided context.
    If not found, say "I don't know".

    Context:
    {context}

    Question:
    {state["user_input"]}
    """

    response = llm.invoke(prompt).content.strip()

    return {"response": response}


# ---- NODE 3: Lead Flow ----
def lead_node(state: AgentState):
    stage = state.get("stage", "start")
    user_input = state["user_input"]

    if stage == "start":
        return {"response": "Great! What's your name?", "stage": "name"}

    elif stage == "name":
        return {"name": user_input, "response": "What's your email?", "stage": "email"}

    elif stage == "email":
        return {"email": user_input, "response": "Which platform do you use?", "stage": "platform"}

    elif stage == "platform":
        result = mock_lead_capture(state["name"], state["email"], user_input)
        return {"platform": user_input, "response": result, "stage": "done"}

    return {"response": "Done"}


# ---- ROUTER ----
def route(state: AgentState):
    intent = state["intent"]

    if "greeting" in intent:
        return "greet"
    elif "high" in intent:
        return "lead"
    else:
        return "rag"


# ---- GREETING NODE ----
def greet_node(state: AgentState):
    return {"response": "Hello! How can I help you today?"}


# ---- BUILD GRAPH ----
builder = StateGraph(AgentState)

builder.add_node("intent", detect_intent)
builder.add_node("rag", rag_node)
builder.add_node("lead", lead_node)
builder.add_node("greet", greet_node)

builder.set_entry_point("intent")

builder.add_conditional_edges(
    "intent",
    route,
    {
        "greet": "greet",
        "rag": "rag",
        "lead": "lead"
    }
)

builder.add_edge("greet", END)
builder.add_edge("rag", END)
builder.add_edge("lead", END)

graph = builder.compile()