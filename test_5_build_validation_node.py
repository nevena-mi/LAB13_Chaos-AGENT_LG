# Educational runner for the step 5 validation node.
from normalobjects_langgraph import ComplaintState, validation_node


# One complaint should validate, and one should fail validation.
sample_states: list[ComplaintState] = [
    {
        "complaint": "A portal opened in my basement last night.",
        "category": "portal",
        "valid": False,
        "investigation": "",
        "resolution": "",
        "final_response": "",
        "status": "intake_complete",
        "workflow_path": ["intake"],
    },
    {
        "complaint": "My toaster is emotionally unavailable.",
        "category": "other",
        "valid": False,
        "investigation": "",
        "resolution": "",
        "final_response": "",
        "status": "intake_complete",
        "workflow_path": ["intake"],
    },
]


# Print each before/after pair so the validation change is easy to see.
if __name__ == "__main__":
    for index, state in enumerate(sample_states, start=1):
        print(f"Example {index} input:")
        print(state)
        print(f"Example {index} output:")
        print(validation_node(state))
        print("-" * 40)
