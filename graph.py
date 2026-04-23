from typing import TypedDict
from langgraph.graph import StateGraph, END

from utils.intent import detect_intent
from utils.rag import get_answer

#  Define state schema 
class AgentState(TypedDict, total=False):
    input: str
    intent: str
    response: str
    lead_stage: str


#  Nodes (mutate + return state)
def detect_intent_node(state: AgentState) -> AgentState:
    user_input = state.get("input", "")
    state["intent"] = detect_intent(user_input)
    return state


def greeting_node(state: AgentState) -> AgentState:
    state["response"] = "Hey! 👋 How can I help you with AutoStream?"
    return state


def rag_node(state: AgentState) -> AgentState:
    user_input = state.get("input", "")
    state["response"] = get_answer(user_input)
    return state


def lead_node(state: AgentState) -> AgentState:
    state["lead_stage"] = "name"
    state["response"] = "Awesome! Let's get you started. What's your name?"
    return state


#  Router
def route_intent(state: AgentState) -> str:
    intent = state.get("intent", "")
    if intent == "greeting":
        return "greeting"
    elif intent == "product_query":
        return "rag"
    elif intent == "high_intent":
        return "lead"
    return "rag"  # fallback


#  Build Graph
builder = StateGraph(AgentState)

builder.add_node("intent", detect_intent_node)
builder.add_node("greeting", greeting_node)
builder.add_node("rag", rag_node)
builder.add_node("lead", lead_node)

builder.set_entry_point("intent")

builder.add_conditional_edges(
    "intent",
    route_intent,
    {
        "greeting": "greeting",
        "rag": "rag",
        "lead": "lead",
    },
)

builder.add_edge("greeting", END)
builder.add_edge("rag", END)
builder.add_edge("lead", END)

graph = builder.compile()