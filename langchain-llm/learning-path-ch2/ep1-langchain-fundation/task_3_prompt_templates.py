"""
Task 3: Prompt Templates - Dynamic, Reusable Prompts
Show how ONE template can be reused with different variables.

Learning Goal: Master prompt templates for consistent, reusable prompts.
"""

import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


def main():
    print("🎯 Task 3: Dynamic Prompt Templates")
    print("=" * 50)

    print("\n📝 Creating a Reusable Template")
    print("=" * 50)

    template = PromptTemplate(
        input_variables=["topic", "style"],
        template="Explain {topic} in {style}",
    )

    # Test with actual LLM to show it works
    print("\n🤖 Testing Template with AI")
    print("=" * 50)

    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
        # base_url=os.getenv("OPENAI_API_BASE"),
        temperature=0.7,
    )

    if template and llm:
        # Format the template with specific values
        test_prompt = template.format(
            topic="taiwan",
            style="exactly 5 words",
        )

        print(f"📝 Sending to AI: {test_prompt}")

        # Get AI response
        response = llm.invoke(test_prompt)
        print(f"\n🤖 AI Response: {response.content}")

    # Show the benefits
    print("\n💡 Template Benefits:")
    print("  ✓ ONE template, INFINITE uses")
    print("  ✓ Variables make it dynamic")
    print("  ✓ Consistent structure across all prompts")
    print("  ✓ Change inputs, not code!")


if __name__ == "__main__":
    load_dotenv("../../.env")  # Load environment variables
    main()
