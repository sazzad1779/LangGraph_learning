# import the library
from typing import TypedDict
from langgraph.graph import StateGraph, START,END


class AgentState(TypedDict):
    n1:int
    n2:int
    op:str
    result:int
    n12:int
    n22:int
    op2:str
    result2:int

def add_node(state:AgentState)->AgentState:
    """ this node is responsible for addition n1 and n2"""
    print(state)
    state["result"]= state["n1"]+state["n2"]
    return state
def add_node2(state:AgentState)->AgentState:
    """ this node is responsible for addition n12 and n22"""
    print(state)
    state["result2"]= state["n12"]+state["n22"]
    return state
def sub_node(state:AgentState)->AgentState:
    """ this node is responsible for substraction n1 and n2"""
    print(state)
    state["result"]= state["n1"]-state["n2"]
    return state
def sub_node2(state:AgentState)->AgentState:
    """ this node is responsible for substraction n12 and n22"""
    print(state)
    state["result2"]= state["n12"]-state["n22"]
    return state
def decide_next_node (state:AgentState)->AgentState:
    """this node is responsible for taking decision"""
    if state["op"]=="+":
        return "add_condition"
    elif state["op"]=="-":
        return "sub_condition"
def decide_next_node1(state:AgentState)->AgentState:
    """this node is responsible for taking decision"""
    if state["op2"]=="+":
        return "add_condition"
    elif state["op2"]=="-":
        return "sub_condition"

graph = StateGraph(AgentState)
graph.add_node("add_node", add_node)
graph.add_node("sub_node", sub_node)
graph.add_node("route", lambda state:state)
graph.add_conditional_edges(
    "route",
    decide_next_node,
    {   # edge name: node name
        "add_condition": "add_node",
        "sub_condition": "sub_node"
    }
)
graph.add_edge(START, "route")
# graph.add_edge("add_node", END)
# graph.add_edge("sub_node", END)

graph.add_node("add_node2", add_node2)
graph.add_node("sub_node2", sub_node2)
graph.add_node("route2", lambda state:state)
graph.add_conditional_edges(
    "route2",
    decide_next_node1,
    {   # edge name: node name
        "add_condition": "add_node2",
        "sub_condition": "sub_node2"
    }
)
graph.add_edge("add_node", "route2")
graph.add_edge("sub_node", "route2")
graph.add_edge("add_node2", END)
graph.add_edge("sub_node2", END)
app =graph.compile()

print(app.get_graph().draw_mermaid())

from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))

app.invoke({"n1":1,"n2":2,"op":"+","n12":1,"n22":2,"op2":"-"})
app.invoke({"n1":1,"n2":2,"op":"+","n12":1,"n22":10,"op2":"-"})







