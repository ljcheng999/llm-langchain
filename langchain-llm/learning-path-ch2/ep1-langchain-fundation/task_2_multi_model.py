"""
Task 2: Multi-Model Support - One Interface, Many Providers!
Test OpenAI, Google, and X.AI models using the same LangChain interface.

Learning Goal: Experience provider flexibility without code changes.

Note: This can only work with chat-based models nowadays, so we will use the init_chat_model wrapper for all providers.
Refer here: https://docs.langchain.com/oss/python/langchain/models
"""

import os
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv


def main():
    print("🎯 Task 2: Multi-Model Support with LangChain")
    print("=" * 50)

    print("\n🌐 Initialize Multiple AI Providers")
    print("=" * 50)

    ### Use init_chat_model
    # print("Setting up OpenAI GPT-4.1-mini...")
    # openai_llm = init_chat_model(
    #     model="gpt-4.1-mini",
    #     api_key=os.getenv("OPENAI_API_KEY"),
    # )

    # print("Setting up Google Gemini...")
    # google_llm = init_chat_model(
    #     model="google_genai:gemini-2.5-flash-lite",
    #     api_key=os.getenv("GEMINI_API_KEY"),
    # )
    ### Use init_chat_model End

    print("Setting up OpenAI GPT-4.1-mini...")
    openai_llm = ChatOpenAI(
        model="gpt-4.1-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
        # base_url=os.getenv("OPENAI_API_BASE")
    )

    print("Setting up Google Gemini...")
    google_llm = ChatGoogleGenerativeAI(
        model="google_genai:gemini-2.5-flash-lite",
        api_key=os.getenv("GEMINI_API_KEY"),
    )

    # print("Setting up X.AI Grok...")
    # xai_llm = ChatOpenAI(
    #     model="grok-code-fast-1",
    #     api_key=os.getenv("OPENAI_API_KEY"),
    #     # base_url=os.getenv("OPENAI_API_BASE")
    # )

    # Compare all models with the same prompt
    print("\n✅ All models initialized! Now let's compare them...")
    print("\nModel Comparison - Same Prompt, Different Models")
    print("=" * 50)

    test_prompt = "Explain cloud computing in one sentence"
    print(f"📝 Prompt: '{test_prompt}'\n")

    # Test all models with the same prompt
    if openai_llm:
        response = openai_llm.invoke(test_prompt)
        print(f"OpenAI: {response.content[:100]}...")

    if google_llm:
        response = google_llm.invoke(test_prompt)
        print(f"Google: {response.content[:100]}...")

    # if xai_llm:
    #     response = xai_llm.invoke(test_prompt)
    #     print(f"X.AI: {response.content[:100]}...")

    print("\n💡 Same code, different providers - perfect for A/B testing!")
    print("\n✅ Task 2 completed! You can now switch models at will!")
    print("🎉 You tested 3 different AI providers with identical code!")


if __name__ == "__main__":
    load_dotenv("../../.env")  # Load environment variables
    main()
