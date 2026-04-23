# 🤖 AutoStream: Conversational AI Agent

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Framework](https://img.shields.io/badge/LangGraph-Agentic-blue)
![Status](https://img.shields.io/badge/Assignment-Completed-brightgreen.svg)

**AutoStream** is an intelligent, agentic AI system designed to transform social media conversations into qualified business leads. Unlike static chatbots, AutoStream leverages a sophisticated state-driven architecture to understand user intent, retrieve context-aware information via RAG, and execute precise lead-capture workflows.

---

##  Key Features

* **Advanced Intent Detection:** Accurately classifies user inputs into specific categories (Greetings, Product/Pricing Inquiries, or High-Intent Lead signals).
* **RAG-Powered Knowledge:** Uses local retrieval-augmented generation (RAG) to provide accurate answers regarding pricing, features, and company policies.
* **Stateful Conversations:** Built with persistent state management to maintain context across 5–6+ turns of conversation.
* **Secure Tool Execution:** Implements a strict "human-in-the-loop" or intent-gated tool execution policy; the lead capture API is only triggered after all required data (Name, Email, Platform) is successfully collected.

---

##  Architecture & Technical Rationale

### Why LangGraph?
I chose **LangGraph** for this agent because it offers the control flow necessary for reliable production-level agents. Unlike linear chains, LangGraph allows for:
1. **Cyclic Workflows:** We can easily route the agent back to the "Ask User" state if a lead capture parameter is missing.
2. **State Persistence:** The `State` object provides a clean, schema-defined way to pass memory across nodes, which is critical for maintaining conversation turns.
3. **Deterministic Control:** By using a graph-based router, we ensure the agent never accidentally triggers the `mock_lead_capture` tool until the state validation confirms all required inputs are present.

### State Management
State is managed using a centralized schema that tracks:
* **`messages`:** The history of the conversation for LLM context.
* **`intent`:** The current classification of the user's goal.
* **`extracted_info`:** A buffer that stores lead details (Name, Email, Platform) as they are collected.
The agent nodes check this state at every step to decide whether to retrieve knowledge (RAG), ask for information, or execute the tool.

---

##  Installation & Setup

1. **Clone the repository:**

   git clone [https://github.com/Jasmeen-1999/autostream-agent.git](https://github.com/Jasmeen-1999/autostream-agent.git)

   cd autostream-agent
2. **Install dependencies:**   
    pip install -r requirements.txt
3. **Run the agent:**
python app.py
 ##  WhatsApp Integration 
To deploy the AutoStream agent on WhatsApp, I would implement the following infrastructure:

1. **Webhook Interface:** Set up a FastAPI or Flask endpoint as a POST webhook.

2. **Platform Integration:** Integrate with the Twilio Messaging API or the Meta Business API to receive incoming WhatsApp messages.

3. **Flow:**
     Incoming messages from WhatsApp are sent to my webhook as JSON payloads.
     The webhook extracts the Sender ID and Message Body.
     These are passed to the LangGraph invoke() method, using the Sender ID as the thread_id to retrieve the correct persistent state.
     The agent's response is generated and sent back to the user via the Twilio/Meta API.

4. **Environment:** This would be containerized (Docker) and deployed on a service like AWS ECS or Google Cloud Run for scalability.
