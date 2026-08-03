# Educational runner for the step 7 resolution node.
from normalobjects_langgraph import ComplaintState, resolution_node


# Sample states already include investigation text from the previous step.
sample_states: list[ComplaintState] = [
    {
        "complaint": "There is a portal under the school gym.",
        "category": "portal",
        "valid": True,
        "investigation": "The portal seems unstable but contained behind debris.",
        "resolution": "",
        "final_response": "",
        "status": "investigation_complete",
        "workflow_path": ["intake", "validate", "investigate"],
    },
    {
        "complaint": "A monster keeps following the car at night.",
        "category": "monster",
        "valid": True,
        "investigation": "The creature avoids bright lights and loud noise.",
        "resolution": "",
        "final_response": "",
        "status": "investigation_complete",
        "workflow_path": ["intake", "validate", "investigate"],
    },
    {
        "complaint": "My psychic dreams are getting louder.",
        "category": "psychic",
        "valid": True,
        "investigation": "The issue appears connected to repeated psychic strain.",
        "resolution": "",
        "final_response": "",
        "status": "investigation_complete",
        "workflow_path": ["intake", "validate", "investigate"],
    },
]


# Print each before/after pair so the resolution change is easy to see.
if __name__ == "__main__":
    for index, state in enumerate(sample_states, start=1):
        print(f"Example {index} input:")
        print(state)
        print(f"Example {index} output:")
        print(resolution_node(state))
        print("-" * 40)
