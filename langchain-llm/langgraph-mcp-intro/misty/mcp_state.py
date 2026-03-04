from pydantic import BaseModel
from typing import Annotated, List
from langgraph.graph import add_messages


class AgentState(BaseModel):
    """
    Represents the state of an agent in the multi-agent system.
    """

    messages: Annotated[List, add_messages]
