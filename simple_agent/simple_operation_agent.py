from typing import TypedDict, Optional
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name:Optional[str]
    values: list
    operation: str
    result: str

def process_values(state:AgentState)->AgentState:
    """ Make the process of values."""
    operation_value = 0
    if state["operation"] =="+":
        operation_value = sum(state["values"])
    elif state["operation"] =="*":
        for v in state["values"]:
            if operation_value == 0:
                operation_value = v
            else:
                operation_value *= v
    state["result"] =f"Hi {state['name']}, your answer is: {operation_value}" 
    return state      
graph = StateGraph(AgentState)
graph.add_node("processor",process_values)
graph.set_entry_point("processor")
graph.set_finish_point("processor")
app = graph.compile()

from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))

result =app.invoke({"name":"Medie","operation":"+","values":[1,2,3,4,1,3]})
print(result)

result =app.invoke({"name":"Medie","operation":"*","values":[1,2,3,4,1,3]})
print(result)