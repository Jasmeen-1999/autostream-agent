from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

def rule_based_intent(user_input: str) -> str:
    text = user_input.lower()

    if any(x in text for x in ["buy", "start", "subscribe", "want", "try"]):
        return "high_intent"
    elif any(x in text for x in ["hi", "hello", "hey"]):
        return "greeting"
    elif any(x in text for x in ["price", "plan", "cost", "pricing"]):
        return "product_query"
    return "product_query"


# LangChain pipeline (simple wrapper)
intent_chain = RunnableLambda(lambda x: rule_based_intent(x["input"]))


def detect_intent(user_input: str) -> str:
    text = user_input.lower()

    #  High intent (expanded)
    if any(x in text for x in [
        "buy", "start", "subscribe", "want", "try",
        "interested", "sign up", "get started", "purchase"
    ]):
        return "high_intent"

    #  Greeting
    elif any(x in text for x in ["hi", "hello", "hey"]):
        return "greeting"

    #  Product query
    elif any(x in text for x in ["price", "pricing", "plan", "cost"]):
        return "product_query"

    return "product_query"