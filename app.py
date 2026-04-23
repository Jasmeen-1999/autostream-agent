from graph import graph
from utils.tools import mock_lead_capture

# 🔹 Global state (memory across turns)
state = {
    "lead_stage": None,
    "name": None,
    "email": None,
    "platform": None
}


# 🔹 Handle multi-step lead collection
def handle_lead_flow(user_input):
    global state

    if state["lead_stage"] == "name":
        state["name"] = user_input
        state["lead_stage"] = "email"
        return "Great! What's your email?"

    elif state["lead_stage"] == "email":
        state["email"] = user_input
        state["lead_stage"] = "platform"
        return "Which platform do you create content on? (YouTube, Instagram, etc.)"

    elif state["lead_stage"] == "platform":
        state["platform"] = user_input

        #  Call tool ONLY after all details collected
        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )

        # Reset flow
        state["lead_stage"] = None

        return "🎉 You're all set! Our team will reach out soon."


# 🔹 Main agent function
def agent(user_input):
    global state

    # If already in lead flow → continue it
    if state["lead_stage"]:
        return handle_lead_flow(user_input)

    # Run LangGraph
    result = graph.invoke({"input": user_input})

    # If graph triggered lead flow → start collecting
    if result.get("lead_stage") == "name":
        state["lead_stage"] = "name"

    return result["response"]


# 🔹 CLI Runner
def run():
    print("🤖 AutoStream Agent Ready! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Agent: Goodbye! 👋")
            break

        response = agent(user_input)
        print("Agent:", response)


if __name__ == "__main__":
    run()