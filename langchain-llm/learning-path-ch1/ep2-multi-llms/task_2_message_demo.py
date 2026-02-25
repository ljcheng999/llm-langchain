import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv("../../.env")  # Load environment variables from .env file
# Initialize model with base_url
model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    # base_url=os.environ.get("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Structure your conversation
messages = [
    SystemMessage(content="You are a helpful Python tutor"),
    HumanMessage(content="Explain variables to a beginner"),
]

# Send to model
response = model.invoke(messages)
print("User: Explain variables to a beginner")
print(f"AI: {response.content}")

# Build a conversation with history
print("\n=== Conversation with Memory ===")
chat_history = [
    SystemMessage(content="You are a friendly assistant who remembers everything"),
    HumanMessage(content="My name is Alice and I love pizza"),
]

# Get first response
ai_response = model.invoke(chat_history)
print("First response:", ai_response.content)

# Add AI response to history
chat_history.append(ai_response)

# Continue conversation
chat_history.append(HumanMessage(content="What's my name and what do I like?"))
response = model.invoke(chat_history)
print("\nAssistant remembers:", response.content)
