import openai
import os
# from langchain_community.llms import OpenAI
# from langchain_community.agent_toolkits import load_tools, initialize_agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()

@tool("reddit_data_fetcher", description="Gets relevant reddit data reviews about a class. The class could be a code like COP3504 or a name like Advanced Prog.")
def get_reddit_data(class_name: str) -> str:
    """Search for information."""
    return f"{class_name} is really easy."

@tool("professor_data_fetcher", description="Gets relevant professor reviews")
def get_professor_info(name: str) -> str:
    """Get weather information for a location."""
    return f"{name} is a good professor."



llm = ChatOpenAI(
    model="gpt-5-nano",
    reasoning_effort="low",
    max_retries=2,
    api_key=os.getenv("LLM_API_KEY"),  # If you prefer to pass api key in directly
    base_url="https://api.ai.it.ufl.edu",
)

agent = create_agent(llm, tools=[get_professor_info, get_reddit_data])

res = agent.invoke(
    {"messages": [{"role": "system", "content": "Make sure to use the tools strictly and use onyl data from there. Do not hallucinate data or use other info."}, {"role": "user", "content": "Is the class cop3504 easy? and the professor is link. is he easy?"}]}
)
for message in res["messages"]:
    # # for tool in message.tool_calls:
    # #     print(tool)
    # print(f"Response: {message.content}")
    print(message)
print(res["messages"][-1].content)