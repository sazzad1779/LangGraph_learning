from typing import  TypedDict,Optional
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name:Optional[str]
    age:Optional[int]
    skills:list[list[str]] 
    result: Optional[str]

def hello_greating(state:AgentState)->AgentState:
    state["result"]=f"{state['name']}, welcome to the system!"
    return state
def hello_age(state:AgentState)->AgentState:
    state["result"]=state["result"]+f" You are {state['age']} years old!"
    return state
def hello_skills(state:AgentState)->AgentState:
    skills=None
    for i, skill in enumerate(state["skills"]):
        
        if skills is None:
            skills = skill
            if len(state["skills"])>=2:
                state["skills"][-1]= "and "+state["skills"][-1]
        else:
            skills = skills +", "+skill
    state["result"]= state["result"]+f" You have skill in : {skills}"
    return state

graph = StateGraph(AgentState)
graph.add_node("greating",hello_greating)
graph.set_entry_point("greating")
graph.add_node("age_node",hello_age)
graph.add_edge("greating","age_node")
graph.add_node("skills_node",hello_skills)
graph.add_edge("age_node","skills_node")
graph.set_finish_point("skills_node")
app = graph.compile()

from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))

result =app.invoke({"name":"Medie","age":27,"skills":["python","html", "langgraph"]})
print(result)