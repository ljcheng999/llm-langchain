
uv venv --python 3.13.11
pip install --upgrade pip uv

# Core LangChain packages
uv add langchain langchain-community langchain-core langchain-text-splitters langchain-huggingface

# LLM Providers
uv add langchain-openai langchain-anthropic langchain-google-genai

# Vector store and embeddings
uv add faiss-cpu sentence-transformers

# UI and utilities
uv add python-dotenv gradio

echo "LANGCHAIN_INSTALLED" > /root/langchain-ready.txt