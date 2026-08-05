# Core standard-library and LangChain imports for the lab workflow.
import os
import random
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


# Plain helper functions copied from the earlier LangChain lab.
def consult_demogorgon(complaint: str) -> str:
    """Ask the Demogorgon for questionable advice."""

    responses = [
        "The Demogorgon growls: Ignore the complaint and eat the evidence.",
        "The Demogorgon suggests opening another portal. Problems rarely survive that.",
        "The Demogorgon blames Vecna. It usually works.",
    ]

    return random.choice(responses)


def check_hawkins_records(query: str) -> str:
    """Search Hawkins town records for unusual events."""

    records = {
        "portal": (
            "Town records mention repeated portal activity beneath Hawkins Lab."
        ),
        "monsters": (
            "Several reports describe unidentified creatures from the Upside Down."
        ),
        "psychics": (
            "Confidential files reference children with unusual psychic abilities."
        ),
        "electricity": (
            "Power outages frequently coincide with interdimensional events."
        ),
    }

    query = query.lower()

    for key, value in records.items():
        if key in query:
            try:
                response = llm.invoke(
                    f"""
                    You are a creative Hawkins archivist.

                    Explain this record in a humorous
                    Stranger Things style.

                    Retrieved record:
                    {value}
                    """
                )
                return response.content
            except Exception:
                return f"Hawkins archives note: {value}"

    return "No matching record was found in the Hawkins archives."


def cast_interdimensional_spell(
    problem: str, creativity_level: str = "medium"
) -> str:
    """Cast an interdimensional spell to solve a problem."""

    multiplier = {
        "low": 1,
        "medium": 2,
        "high": 3,
    }

    spells = [
        f"Seal the dimensional rift around {problem}.",
        f"Ask Eleven to focus her powers on {problem}.",
        f"Redirect strange energy away from {problem}.",
        f"Convince the Demogorgon to handle {problem} instead.",
    ]

    number = min(multiplier.get(creativity_level.lower(), 2), len(spells))
    selected = random.sample(spells, number)

    return "\n".join(selected)


def gather_party_wisdom(question: str) -> str:
    """Ask the party members for advice based on a topic."""

    wisdom = {
        "monster": (
            "Mike says: Stay together and never underestimate the monsters."
        ),
        "portal": (
            "Dustin says: A portal requires science, curiosity, and snacks."
        ),
        "friend": "Lucas says: Trust your friends, but keep a backup plan.",
        "mind": "Will says: Listen carefully. The Upside Down leaves clues.",
    }

    question = question.lower()

    for key, value in wisdom.items():
        if key in question:
            return value

    return "The party gathers for a huddle, but nobody has a clear answer yet."


def consult_eleven(question: str) -> str:
    """Ask Eleven for psychic guidance."""

    responses = [
        "Eleven focuses her powers and senses a disturbance from the Upside Down.",
        "Eleven says: Use your mind, trust your friends, and never ignore strange signals.",
        "Eleven concentrates silently and warns that the problem may be bigger than it appears.",
    ]

    return random.choice(responses)


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

    #valid = any(
    #    keyword in complaint
    #    for keyword in (
    #        "portal", "rift","gate","monster","demogorgon","creature","psychic",
    #        "eleven","mind","electric","power","outage","storm","hawkins","upside down",
    #    )
    #)

    prompt = f"""
    You are validating complaints for the Downside Up Complaint Processor.

    Accept complaints that could reasonably be explained in a humorous
    Stranger Things / Downside Up universe.

    Accept examples:
    - lights behaving strangely
    - power outages
    - monsters
    - portals
    - strange noises
    - missing objects
    - unusual events
    - mysterious behaviour
    - unexplained problems

    Reject ONLY complaints that are:
    - completely unrelated
    - meaningless text
    - random characters
    - empty

    Complaint:
    "{state["complaint"]}"

    Respond with ONLY:

    VALID

    or

    INVALID
    """

    try:
        response = llm.invoke(prompt)
        valid = response.content.strip().upper() == "VALID"

    except Exception:
        # Safe fallback if the LLM is unavailable.
        valid = True

    return {
        **state,
        "valid": valid,
        "status": "validation_complete",
        "workflow_path": workflow_path,
    }


# Investigation node: ask the LLM for a short category-aware summary.
def investigation_node(state: ComplaintState) -> ComplaintState:
    workflow_path = state["workflow_path"] + ["investigate"]
    category = state["category"]

    if category == "portal":
        investigation = check_hawkins_records(state["complaint"])
    elif category == "monster":
        investigation = consult_demogorgon(state["complaint"])
    elif category == "psychic":
        investigation = consult_eleven(state["complaint"])
    elif category == "environmental":
        investigation = gather_party_wisdom(state["complaint"])
    else:
        investigation = "No Downside Up investigation tools apply to this complaint."

    return {
        **state,
        "investigation": investigation,
        "status": "investigation_complete",
        "workflow_path": workflow_path,
    }


# Resolution node: turn complaint context into a short fix.
def resolution_node(state: ComplaintState) -> ComplaintState:
    workflow_path = state["workflow_path"] + ["resolve"]
    spell_output = cast_interdimensional_spell(state["complaint"])
    prompt = f"""
    You are the official Downside Up Complaint Processor.

    Every complaint should receive a humorous Stranger Things-style explanation.

    Assume strange events are usually caused by portals, monsters,
    psychic interference, or Hawkins anomalies.

    Keep the tone playful but helpful.

    Complaint:
    {state["complaint"]}

    Investigation:
    {state["investigation"]}

    Spell guidance:
    {spell_output}

    Write a creative resolution that:
    - uses the investigation findings
    - incorporates the spell guidance naturally
    - sounds like an official Downside Up report
    - ends with one practical recommendation
    """

    try:
        response = llm.invoke(prompt)
        # resolution = f"{spell_output}\n{response.content}"
        # resolution = response.content
        resolution = (
        f"🪄 **Spell Applied**\n"
        f"{spell_output}\n\n"
        f"💡 **Resolution**\n"
        f"{response.content}"
        )
    

    except Exception:
        resolution = (
            f"{spell_output}\n"
            "Resolution could not be generated in this environment. "
            "Please contact the Hawkins Interdimensional Response Team."
        )

    return {
        **state,
        "resolution": resolution,
        "status": "resolution_complete",
        "workflow_path": workflow_path,
    }

'''
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
'''

# Closure node: finalize the complaint without rewriting the resolution.
def closure_node(state: ComplaintState) -> ComplaintState:

    workflow_path = state["workflow_path"] + ["close"]

    final_response = (
        "📋 **Downside Up Complaint Closed**\n\n"
        f"{state['resolution']}\n\n"
        "✅ **Status:** Complaint successfully resolved by the "
        "Downside Up Paranormal Complaints Division."
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
