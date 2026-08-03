# Core standard-library and LangChain imports for the lab workflow.
import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


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


# Terminal demo: print the sample state and show the intake node result.
if __name__ == "__main__":
    print(example_state)
    print(intake_node(example_state))
    if not api_key:
        print("OPENAI_API_KEY is not set, so llm.invoke() was skipped.")
    else:
        try:
            response = llm.invoke("Say 'LangGraph ready' in one short sentence.")
            print(response.content)
        except Exception as exc:
            print(f"llm.invoke() failed: {exc}")
