#import library
from typing import TypedDict
from langgraph.graph import StateGraph, START,END

class AgentState(TypedDict):
    name:str
    counter:int
    random:int
    result:str

def hello_greating(state:AgentState)->AgentState:
    state["result"]=f"Hello {state['name']}"
    print("print from hello greating",state)
    state["counter"]=0
    return state
def random_number(state:AgentState)->AgentState:
    import random
    state["random"]=random.randint(1,10)
    state["counter"]+=1
    print("print from random_number",state)
    return state
def check_continue(state:AgentState)->AgentState:
    if state["counter"]>5:
        return "exit"
    else:
        return "continue"


graph=StateGraph(AgentState)
graph.add_node("greating_node",hello_greating)
graph.add_node("random_node",random_number)
graph.add_conditional_edges("random_node",
                            check_continue,
                            {
                                "exit":END,
                                "continue":"random_node"

                            })

graph.add_edge("greating_node","random_node")
graph.add_edge(START,"greating_node")
app =graph.compile()


from IPython.display import Image,display
display(Image(app.get_graph().draw_mermaid_png()))

app.invoke({"name":"sazzad","counter":0})