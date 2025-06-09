from typing import TypedDict,Union,Optional,Any,List
from langgraph.graph import StateGraph,START,END

class AgentState(TypedDict):
    messages:Optional[str]

def hello_function(state:AgentState)->AgentState:
    state["messages"] = f"Hi {state['messages']}"
    return state

graph  = StateGraph(AgentState)
graph.add_node("greating",hello_function)
graph.add_edge(START,"greating")
graph.add_edge("greating",END)
# graph.set_entry_point("greating")
# graph.set_finish_point("greating")
app = graph.compile()

from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))



app.invoke({"messages":"Medie"})