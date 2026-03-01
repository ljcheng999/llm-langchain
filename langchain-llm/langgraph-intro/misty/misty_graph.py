import os
from typing import List
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver

from misty_state import MistyState
from misty_intro import misty_system_prompt

from dotenv import load_dotenv


class Agent:
    """
    Agent class for implementing Langgraph agents.

    Attributes:
        name: The name of the agent.
        tools: The tools available to the agent.
        model: The model to use for the agent.
        system_prompt: The system prompt for the agent.
        temperature: The temperature for the agent.
    """

    def __init__(
        self,
        name: str,
        tools: List = [],
        # tools: List = [query_db, generate_visualization],
        model: str = "gpt-4.1-mini-2025-04-14",
        system_prompt: str = "You are a helpful and friendly assistant.",
        temperature: float = 0.1,
    ):
        self.name = name
        self.tools = tools
        self.model = model
        self.system_prompt = system_prompt
        self.temperature = temperature

        self.llm = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            model=self.model,
            temperature=self.temperature,
        ).bind_tools(self.tools)

    def build_graph(self):
        """
        Build the graph for the agent based on the current state.
        """

        def misty_node(state: MistyState) -> MistyState:
            # response = self.llm.invoke(
            #     [SystemMessage(content=self.system_prompt)] + state.messages
            # )
            response = self.llm.batch(
                [SystemMessage(content=self.system_prompt)] + state.messages
            )
            state.messages = state.messages + [response]

            return state

        def router(state: MistyState) -> str:
            last_message = state.messages[-1]
            if not last_message.tool_calls:
                return END
            else:
                return "tools"

        graph_builder = StateGraph(MistyState)
        graph_builder.add_node("chatbot", misty_node)
        graph_builder.add_node("tools", ToolNode(self.tools))

        graph_builder.add_edge(START, "chatbot")
        graph_builder.add_conditional_edges("chatbot", router, ["tools", END])
        graph_builder.add_edge("tools", "chatbot")

        return graph_builder.compile(checkpointer=MemorySaver())


load_dotenv("../.env")
# Define and instantiate the agent
agent = Agent(name="Misty", system_prompt=misty_system_prompt)
graph = agent.build_graph()

# from IPython.display import display, Image
# display(Image(graph.get_graph(xray=True).draw_mermaid_png()))
