
from langchain.tools import tool
from pydantic import BaseModel, Field

class ParseClassCode(BaseModel):
  prompt: str = Field(description="The prompt provided by the user.")

@tool("parse_class_code", description="Gets class code from the given text prompt.", args_schema=ParseClassCode)
def parse_class_code(prompt: str):
  # Return the parsed class code in correct form from text
  return "COP3504"

class GetClassTimes(BaseModel):
  class_code: str = Field(description="A class code. It will be in form: COP3054, COT3100, CIS4201, ect.")

@tool("get_class_times", description="Gets available class times given a class code.", args_schema=GetClassTimes)
def get_class_times(class_code: str):
  # Return tuple of available times given a class code
  return ("11:45AM", "12:00AM", "1:00PM")

class GetReqsFilled(BaseModel):
  class_code: str = Field(description="A class code. It will be in form: COP3054, COT3100, CIS4201, ect.")

@tool("get_reqs_filled", description="Gets user graduation requirements fulfilled by a class code.", args_schema=GetReqsFilled)
def get_reqs_filled(class_code: str):
  # Get the requirements fulfilled by a course
  return ("core computer class", "humanities")

class GetReqsNeeded(BaseModel):
  ufid: str = Field(description="A unique 8 digit ufid identifier (ex: 36734348)")

@tool("get_reqs_needed", description="Gets user graduation requirements already completed.", args_schema=GetReqsNeeded)
def get_reqs_needed(ufid: str):
  # Return the requirements needed for a student
  return ("core computer class", "humanities")

