# Educational runner for the step 8 closure node.
from normalobjects_langgraph import ComplaintState, closure_node


# Sample states already include investigation and resolution text.
sample_states: list[ComplaintState] = [
    {
        "complaint": "There is a portal under the school gym.",
        "category": "portal",
        "valid": True,
        "investigation": "The portal seems unstable but contained behind debris.",
        "resolution": "Seal the portal and monitor the area overnight.",
        "final_response": "",
        "status": "resolution_complete",
        "workflow_path": ["intake", "validate", "investigate", "resolve"],
    },
    {
        "complaint": "A monster keeps following the car at night.",
        "category": "monster",
        "valid": True,
        "investigation": "The creature avoids bright lights and loud noise.",
        "resolution": "Use bright floodlights and keep everyone together.",
        "final_response": "",
        "status": "resolution_complete",
        "workflow_path": ["intake", "validate", "investigate", "resolve"],
    },
    {
        "complaint": "My psychic dreams are getting louder.",
        "category": "psychic",
        "valid": True,
        "investigation": "The issue appears connected to repeated psychic strain.",
        "resolution": "Rest, reduce stimulation, and monitor the symptoms.",
        "final_response": "",
        "status": "resolution_complete",
        "workflow_path": ["intake", "validate", "investigate", "resolve"],
    },
]


# Print each before/after pair so students can see how closure finishes the workflow.
if __name__ == "__main__":
    for index, state in enumerate(sample_states, start=1):
        print(f"Example {index} input:")
        print(state)
        print(f"Example {index} output:")
        print(closure_node(state))
        print("-" * 40)
