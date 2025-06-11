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
    if state["op"]=="+":
        return "add_condition"
    elif state["op"]=="-":
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
graph.add_edge("add_node", END)
graph.add_edge("sub_node", END)

app =graph.compile()


from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))








