FROM langchain/langgraph-api:3.12

WORKDIR /app

COPY pyproject.toml .
COPY src ./src

RUN uv sync

# Set env
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1