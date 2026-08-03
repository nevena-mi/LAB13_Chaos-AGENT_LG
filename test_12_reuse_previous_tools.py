# Educational runner for the tool reuse integration.
# This script exercises the reused investigation and resolution tools end-to-end.
from normalobjects_langgraph import app


# One complaint per category so each reused tool path is exercised at least once.
test_complaints = [
    # Portal -> check_hawkins_records
    "There is a portal under the school gym.",
    # Monster -> consult_demogorgon
    "A monster keeps following the car at night.",
    # Psychic -> consult_eleven
    "My psychic dreams are getting louder.",
    # Environmental -> gather_party_wisdom
    "Our friends keep worrying about the power outage.",
    # Invalid -> reject path unchanged
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
        print("investigation:", result["investigation"])
        print("resolution:", result["resolution"])
        print("final_response:", result["final_response"])
        print("-" * 40)
