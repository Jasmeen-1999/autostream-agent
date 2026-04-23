from langchain_core.prompts import PromptTemplate
import json

def load_knowledge_base():
    with open("knowledge_base.json", "r") as f:
        data = json.load(f)
    return data["content"]

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    Answer the question based only on the context below:

    {context}

    Question: {question}
    """
)

def get_answer(query):
    query = query.lower()

    if any(word in query for word in ["price", "pricing", "plan", "plans", "cost"]):
        return """AutoStream offers two plans:

Basic Plan – $29/month (10 videos, 720p resolution)
Pro Plan – $79/month (unlimited videos, 4K resolution, AI captions)

Note:
• No refunds after 7 days
• 24/7 support available only on Pro plan"""

    elif "refund" in query:
        return "No refunds are allowed after 7 days."

    elif "support" in query:
        return "24/7 support is available only for Pro plan users."

    else:
        return "I can help with pricing, features, or getting you started. What would you like to know?"