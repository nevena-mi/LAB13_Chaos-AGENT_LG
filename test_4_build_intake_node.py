# Educational runner for the step 4 intake node.
from normalobjects_langgraph import ComplaintState, intake_node


# Sample complaints cover each category plus the fallback case.
sample_states: list[ComplaintState] = [
    {
        "complaint": "There is a portal humming in my basement.",
        "category": "",
        "valid": True,
        "investigation": "",
        "resolution": "",
        "final_response": "",
        "status": "pending",
        "workflow_path": [],
    },
    {
        "complaint": "A monster keeps knocking on my window at night.",
        "category": "",
        "valid": True,
        "investigation": "",
        "resolution": "",
        "final_response": "",
        "status": "pending",
        "workflow_path": [],
    },
    {
        "complaint": "My psychic neighbor says the walls are whispering.",
        "category": "",
        "valid": True,
        "investigation": "",
        "resolution": "",
        "final_response": "",
        "status": "pending",
        "workflow_path": [],
    },
    {
        "complaint": "The power keeps going out whenever it rains.",
        "category": "",
        "valid": True,
        "investigation": "",
        "resolution": "",
        "final_response": "",
        "status": "pending",
        "workflow_path": [],
    },
    {
        "complaint": "I lost my socks again.",
        "category": "",
        "valid": True,
        "investigation": "",
        "resolution": "",
        "final_response": "",
        "status": "pending",
        "workflow_path": [],
    },
]


# Print each before/after pair so students can see exactly what changed.
if __name__ == "__main__":
    for index, state in enumerate(sample_states, start=1):
        print(f"Example {index} input:")
        print(state)
        print(f"Example {index} output:")
        print(intake_node(state))
        print("-" * 40)
