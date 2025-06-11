from typing import TypedDict, Optional
from langgraph.graph import StateGraph,START,END


class AgentState(TypedDict):
    n1:int
    n2:int
    op:str
    result:int

def add_node(state:AgentState)->AgentState:
    """ this node is responsible for addition"""
    print(state)
    state["result"]= state["n1"]+state["n2"]
    return state

def sub_node(state:AgentState)->AgentState:
    """ this node is responsible for substraction"""
    print(state)
    state["result"]= state["n1"]-state["n2"]
    return state
def mul_node(state:AgentState)->AgentState:
    """ this node is responsible for multiplication"""
    print(state)
    state["result"]= state["n1"]*state["n2"]
    return state
def div_node(state:AgentState)->AgentState:
    """ this node is responsible for division"""
    print(state)
    state["result"]= state["n1"]/state["n2"]
    return state
def decide_next_node (state:AgentState)->AgentState:
    """this node is responsible for taking decision"""
    if state["op"]=="+":
        return "add_condition"
    elif state["op"]=="-":
        return "sub_condition"
    elif state["op"]=="*":
        return "mul_condition"
    elif state["op"]=="/":
        return "div_condition"

graph = StateGraph(AgentState)
graph.add_node("add_node", add_node)
graph.add_node("sub_node", sub_node)
graph.add_node("mul_node", mul_node)
graph.add_node("div_node", div_node)
graph.add_node("route", lambda state:state)
graph.add_conditional_edges(
    "route",
    decide_next_node,
    {   # edge name: node name
        "add_condition": "add_node",
        "sub_condition": "sub_node",
        "mul_condition": "mul_node",
        "div_condition": "div_node"
    }
)
graph.add_edge(START, "route")
graph.add_edge("add_node", END)
graph.add_edge("sub_node", END)

app =graph.compile()


from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))

app.invoke({"n1":1,"n2":2,"op":"+"})
app.invoke({"n1":1,"n2":2,"op":"-"})
app.invoke({"n1":10,"n2":2,"op":"*"})
app.invoke({"n1":12,"n2":2,"op":"/"})

