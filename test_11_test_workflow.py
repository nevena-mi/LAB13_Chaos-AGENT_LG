# Educational runner for the step 11 workflow test.
# This script runs the compiled graph end-to-end and prints key output fields.
from normalobjects_langgraph import app


# Sample complaints cover the main happy-path categories plus one invalid case.
test_complaints = [
    "There is a portal under the school gym.",
    "A monster keeps following the car at night.",
    "My psychic dreams are getting louder.",
    "The power keeps going out whenever it rains.",
    "My toaster is emotionally unavailable.",
]


if __name__ == "__main__":
    for index, complaint in enumerate(test_complaints, start=1):
        print(f"Example {index} complaint:")
        print(complaint)

        result = app.invoke(
            {
                "complaint": complaint,
                "category": "",
                "valid": False,
                "investigation": "",
                "resolution": "",
                "final_response": "",
                "status": "pending",
                "workflow_path": [],
            }
        )

        print("category:", result["category"])
        print("workflow_path:", result["workflow_path"])
        print("status:", result["status"])
        print("final_response:", result["final_response"])
        print("-" * 40)
