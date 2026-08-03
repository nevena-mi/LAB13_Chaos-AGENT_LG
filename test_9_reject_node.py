# Educational runner for the step 9 reject node.
from normalobjects_langgraph import ComplaintState, reject_node


# Sample states represent complaints that failed validation.
sample_states: list[ComplaintState] = [
    {
        "complaint": "My toaster is emotionally unavailable.",
        "category": "other",
        "valid": False,
        "investigation": "",
        "resolution": "",
        "final_response": "",
        "status": "validation_complete",
        "workflow_path": ["intake", "validate"],
    },
    {
        "complaint": "The office stapler is sending me messages from the moon.",
        "category": "other",
        "valid": False,
        "investigation": "",
        "resolution": "",
        "final_response": "",
        "status": "validation_complete",
        "workflow_path": ["intake", "validate"],
    },
    {
        "complaint": "I need more socks and better vibes.",
        "category": "other",
        "valid": False,
        "investigation": "",
        "resolution": "",
        "final_response": "",
        "status": "validation_complete",
        "workflow_path": ["intake", "validate"],
    },
]


# Print each before/after pair so students can see how rejection ends the workflow.
if __name__ == "__main__":
    for index, state in enumerate(sample_states, start=1):
        print(f"Example {index} input:")
        print(state)
        print(f"Example {index} output:")
        print(reject_node(state))
        print("-" * 40)
