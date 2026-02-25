import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv("../../.env")  # Load environment variables from .env file


# Different models for different purposes

# 1. Fast & Low-cost for simple tasks
fast_model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
)

# 2. Coding expert for programming
coding_model = ChatOpenAI(
    model="qwen3-coder-plus",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
)

# 4. Conversational for chatting
chat_model = ChatOpenAI(
    model="deepseek-chat",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Test each model with appropriate tasks
print("=== FAST MODEL (Simple Math) ===")
print(fast_model.invoke("What is 25 * 4?").content)

print("\n=== CODING MODEL (Write Code) ===")
code_task = "Write a Python function to reverse a string"
print(coding_model.invoke(code_task).content[:250] + "...")

print("\n=== CHAT MODEL (Friendly Talk) ===")
print(chat_model.invoke("Tell me a fun fact about dolphins!").content)
