from typing import  TypedDict,Optional
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name:Optional[str]
    age:Optional[int]
    message:Optional[str]   
    