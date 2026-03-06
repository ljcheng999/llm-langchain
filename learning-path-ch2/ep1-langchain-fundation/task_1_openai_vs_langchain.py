import os
from dotenv import load_dotenv


def raw_openai_approach():
    """Raw OpenAI SDK - complex and verbose"""
    print("\n🔴 RAW OPENAI SDK APPROACH")

    import openai

    client = openai.OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        # base_url=os.getenv("OPENAI_API_BASE")
    )

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": "Explain machine learning in one sentence"}
        ],
    )

    if response:
        text = response.choices[0].message.content
        print(f"Response: {text[:100]}...")
        return text

    return None


def langchain_approach():
    """LangChain - clean and simple"""
    print("\n🟢 LANGCHAIN APPROACH")

    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
        # base_url=os.getenv("OPENAI_API_BASE")
    )

    response = llm.invoke("Explain machine learning in one sentence")

    if response:
        print(f"Response: {response.content[:100]}...")
        return response.content

    return None


def main():
    print("🎯 Task 1: OpenAI SDK vs LangChain Comparison")
    print("=" * 50)

    # Run both approaches
    raw_result = raw_openai_approach()
    langchain_result = langchain_approach()

    # Show the difference
    if raw_result or langchain_result:
        print("\n📊 COMPARISON:")
        print("✅ Both approaches work, but LangChain is:")
        print("  - 70% less code")
        print("  - Cleaner response handling")
        print("  - Provider agnostic")


if __name__ == "__main__":
    load_dotenv("../../.env")  # Load environment variables
    main()
