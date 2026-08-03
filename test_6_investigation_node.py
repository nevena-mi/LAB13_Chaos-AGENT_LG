# Educational runner for the step 6 investigation node.
from normalobjects_langgraph import ComplaintState, investigation_node


# Sample states already reflect intake and validation having run.
sample_states: list[ComplaintState] = [
    {
        "complaint": "There is a portal under the school gym.",
        "category": "portal",
        "valid": True,
        "investigation": "",
        "resolution": "",
        "final_response": "",
        "status": "validation_complete",
        "workflow_path": ["intake", "validate"],
    },
    {
        "complaint": "A monster keeps following the car at night.",
        "category": "monster",
        "valid": True,
        "investigation": "",
        "resolution": "",
        "final_response": "",
        "status": "validation_complete",
        "workflow_path": ["intake", "validate"],
    },
    {
        "complaint": "My psychic dreams are getting louder.",
        "category": "psychic",
        "valid": True,
        "investigation": "",
        "resolution": "",
        "final_response": "",
        "status": "validation_complete",
        "workflow_path": ["intake", "validate"],
    },
]


# Print each before/after pair so students can see how investigation fills in.
if __name__ == "__main__":
    for index, state in enumerate(sample_states, start=1):
        print(f"Example {index} input:")
        print(state)
        print(f"Example {index} output:")
        print(investigation_node(state))
        print("-" * 40)
