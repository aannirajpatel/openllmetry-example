from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks import FileCallbackHandler
from langchain.globals import set_debug

set_debug(True)

# For a tool-calling agent, we need 3 things: LLM (compatible with the "tool calling" concept), tools, and a chat prompt template

# LLM
llm = ChatOpenAI()


# Tools
@tool
def add_numbers(a: int, b: int) -> int:
    """Adds the two given numbers `a` and `b` and returns the sum."""
    return a + b


@tool
def subtract_numbers(a: int, b: int) -> int:
    """Subtracts the second number `b` from the first number `a` and returns the difference. In mathematical terms, this is `a - b`."""
    return a - b


@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiplies the two given numbers `a` and `b` and returns the product."""
    return a * b


@tool
def divide_numbers(a: int, b: int) -> float:
    """Divides the first number `a` by the second number `b` and returns the
    quotient."""
    return a / b


tools = [add_numbers, subtract_numbers, multiply_numbers, divide_numbers]

# ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an assistant designed to help with basic arithmetic. In "
            "order to ensure the mathematical correctness, be sure to utilize"
            " the tools provided to you, as required. Ensure to convert"
            " provided numbers to decimal values before calling any tool. Your"
            " response must be solely a number calculated using the provided"
            "tools, even for the most trivial of operations.",
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

# Create agent
agent = create_tool_calling_agent(llm, tools, prompt)

# Create agent executor (in a nutshell, the executor calls the agent
# repeatedly and passes tool execution results until goal is achieved
# or we reach the tool call or duration limit)
agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, callbacks=[FileCallbackHandler("tmp.log")]
)
