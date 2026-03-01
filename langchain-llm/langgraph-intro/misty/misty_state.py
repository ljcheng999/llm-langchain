from pydantic import BaseModel
from typing import Annotated, List
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import add_messages


class MistyState(BaseModel):
    messages: Annotated[List[BaseMessage], add_messages] = []
    chart_json: str = ""


# state = MistyState(
#     messages=[HumanMessage(content="What is AI or ML?")],
#     chart_json="this is the chart json",
# )

# print(state.model_dump_json(indent=2))
