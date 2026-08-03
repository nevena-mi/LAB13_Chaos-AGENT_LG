# Core standard-library and LangChain imports for the lab workflow.
import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph


# Shared workflow state passed between LangGraph nodes.
class ComplaintState(TypedDict):
    complaint: str
    category: str
    valid: bool
    investigation: str
    resolution: str
    final_response: str
    status: str
    workflow_path: list[str]


# Simple example state used to show the state shape in a terminal run.
example_state: ComplaintState = {
    "complaint": "The portal in my basement keeps making strange noises.",
    "category": "portal",
    "valid": True,
    "investigation": "",
    "resolution": "",
    "final_response": "",
    "status": "pending",
    "workflow_path": [],
}


# Load environment variables and create the reusable LLM instance.
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    api_key=api_key,
)


# Intake node: classify the complaint and record that intake ran.
def intake_node(state: ComplaintState) -> ComplaintState:
    complaint = state["complaint"].lower()
    workflow_path = state["workflow_path"] + ["intake"]

    if any(keyword in complaint for keyword in ("portal", "rift", "gate")):
        category = "portal"
    elif any(keyword in complaint for keyword in ("monster", "demogorgon", "creature")):
        category = "monster"
    elif any(keyword in complaint for keyword in ("psychic", "eleven", "mind")):
        category = "psychic"
    elif any(keyword in complaint for keyword in ("electric", "power", "outage", "storm")):
        category = "environmental"
    else:
        category = "other"

    return {
        **state,
        "category": category,
        "status": "intake_complete",
        "workflow_path": workflow_path,
    }


# Validation node: decide whether the complaint belongs in the workflow.
def validation_node(state: ComplaintState) -> ComplaintState:
    complaint = state["complaint"].lower()
    workflow_path = state["workflow_path"] + ["validate"]

    valid = any(
        keyword in complaint
        for keyword in (
            "portal",
            "rift",
            "gate",
            "monster",
            "demogorgon",
            "creature",
            "psychic",
            "eleven",
            "mind",
            "electric",
            "power",
            "outage",
            "storm",
            "hawkins",
            "upside down",
        )
    )

    return {
        **state,
        "valid": valid,
        "status": "validation_complete",
        "workflow_path": workflow_path,
    }


# Investigation node: ask the LLM for a short category-aware summary.
def investigation_node(state: ComplaintState) -> ComplaintState:
    workflow_path = state["workflow_path"] + ["investigate"]
    prompt = (
        "You are helping with a Downside Up complaint workflow.\n"
        f"Complaint: {state['complaint']}\n"
        f"Category: {state['category']}\n"
        "Write a short investigation summary with the most relevant findings."
    )

    try:
        response = llm.invoke(prompt)
        investigation = response.content
    except Exception:
        investigation = (
            f"Investigation could not be completed for the {state['category']} "
            "complaint in this environment."
        )

    return {
        **state,
        "investigation": investigation,
        "status": "investigation_complete",
        "workflow_path": workflow_path,
    }


# Resolution node: turn complaint context into a short fix.
def resolution_node(state: ComplaintState) -> ComplaintState:
    workflow_path = state["workflow_path"] + ["resolve"]
    prompt = (
        "You are helping with a Downside Up complaint workflow.\n"
        f"Complaint: {state['complaint']}\n"
        f"Investigation: {state['investigation']}\n"
        "Write a short resolution that directly addresses the complaint."
    )

    try:
        response = llm.invoke(prompt)
        resolution = response.content
    except Exception:
        resolution = (
            "Resolution could not be generated in this environment, but the "
            "complaint should be handled with a practical Downside Up fix."
        )

    return {
        **state,
        "resolution": resolution,
        "status": "resolution_complete",
        "workflow_path": workflow_path,
    }


# Closure node: turn the work done into a final response.
def closure_node(state: ComplaintState) -> ComplaintState:
    workflow_path = state["workflow_path"] + ["close"]
    prompt = (
        "You are helping with a Downside Up complaint workflow.\n"
        f"Complaint: {state['complaint']}\n"
        f"Investigation: {state['investigation']}\n"
        f"Resolution: {state['resolution']}\n"
        "Write a short final response that confirms the complaint was handled."
    )

    try:
        response = llm.invoke(prompt)
        final_response = response.content
    except Exception:
        final_response = (
            "Your complaint has been handled and the workflow is now closed."
        )

    return {
        **state,
        "final_response": final_response,
        "status": "closure_complete",
        "workflow_path": workflow_path,
    }


# Reject node: end the workflow for invalid complaints.
def reject_node(state: ComplaintState) -> ComplaintState:
    workflow_path = state["workflow_path"] + ["reject"]
    final_response = (
        "Complaint rejected because it is unrelated to the Downside Up workflow."
    )

    return {
        **state,
        "final_response": final_response,
        "status": "rejection_complete",
        "workflow_path": workflow_path,
    }


# Graph routing helper: choose the next step after validation.
def route_after_validation(state: ComplaintState) -> str:
    return "investigate" if state["valid"] else "reject"


# Build and compile the full workflow graph for the lab.
workflow = StateGraph(ComplaintState)
workflow.add_node("intake", intake_node)
workflow.add_node("validate", validation_node)
workflow.add_node("investigate", investigation_node)
workflow.add_node("resolve", resolution_node)
workflow.add_node("close", closure_node)
workflow.add_node("reject", reject_node)

workflow.set_entry_point("intake")
workflow.add_edge("intake", "validate")
workflow.add_conditional_edges(
    "validate",
    route_after_validation,
    {
        "investigate": "investigate",
        "reject": "reject",
    },
)
workflow.add_edge("investigate", "resolve")
workflow.add_edge("resolve", "close")
workflow.add_edge("close", END)
workflow.add_edge("reject", END)

app = workflow.compile()


# Terminal demo: print the sample state and show the intake node result.
if __name__ == "__main__":
    print(example_state)
    print(intake_node(example_state))
    print(
        investigation_node(
            {
                **example_state,
                "workflow_path": ["intake", "validate"],
            }
        )
    )
    print(
        resolution_node(
            {
                **example_state,
                "investigation": "The portal appears unstable but contained.",
                "workflow_path": ["intake", "validate", "investigate"],
            }
        )
    )
    print(
        closure_node(
            {
                **example_state,
                "investigation": "The portal appears unstable but contained.",
                "resolution": "Seal the portal and monitor the basement overnight.",
                "workflow_path": ["intake", "validate", "investigate", "resolve"],
            }
        )
    )
    print(
        reject_node(
            {
                **example_state,
                "category": "other",
                "valid": False,
                "status": "validation_complete",
                "workflow_path": ["intake", "validate"],
            }
        )
    )
    try:
        print(app.get_graph().draw_ascii())
    except ImportError:
        print("Install grandalf to draw the graph as ASCII.")
    if not api_key:
        print("OPENAI_API_KEY is not set, so llm.invoke() was skipped.")
    else:
        try:
            response = llm.invoke("Say 'LangGraph ready' in one short sentence.")
            print(response.content)
        except Exception as exc:
            print(f"llm.invoke() failed: {exc}")
