import openai
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from typing import Any

from timing import time_it
from tools.core import parse_class_code, get_class_times, get_reqs_filled, get_reqs_needed

load_dotenv()

# mercury_llm = ChatOpenAI(
#   model="inception/mercury",
#   api_key=os.getenv("MERCURY_LLM_API_KEY"),
#   base_url="https://openrouter.ai/api/v1"
# )

llm = ChatOpenAI(
    model="gpt-5-nano",
    reasoning_effort="low",
    max_retries=2,
    api_key=os.getenv("LLM_API_KEY"),
    base_url="https://api.ai.it.ufl.edu",
)

# llm.invoke("test")
@time_it
def ask(prompt: str, llm: Any):
  agent = create_agent(llm, tools=[
    parse_class_code,
    get_class_times,
    get_reqs_filled,
    get_reqs_needed
  ])
  res = agent.invoke(
      {"messages": [
         {"role": "system", "content": "Make sure to use the tools strictly and use onyl data from there. Do not hallucinate data or use other info."}, 
         {"role": "user", "content": prompt}
      ]}
  )
  tools_used: list[str] = []
  for message in res["messages"]:
      try:
          tools_used += message.tool_calls
      except:
          pass
  return tools_used, res["messages"][-1].content

tools, response = ask(prompt="I want to take COP3504 and I would like to see what requirements it fulfills.", llm=llm)
print(tools)
print(response)
# ask(prompt="I want to take COP3504 and I would like to see what requirements it fulfills.", llm=mercury_llm)

