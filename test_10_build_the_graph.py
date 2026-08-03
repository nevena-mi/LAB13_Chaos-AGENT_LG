# Educational runner for Step 10 graph wiring.
# Prints the workflow graph and saves it to the project root.

from pathlib import Path

from normalobjects_langgraph import app


OUTPUT_FILE = Path("workflow_graph.txt")


if __name__ == "__main__":

    try:
        graph = app.get_graph().draw_ascii()

        print(graph)

        OUTPUT_FILE.write_text(
            graph,
            encoding="utf-8"
        )

        print(f"\nGraph saved to: {OUTPUT_FILE}")

    except ImportError:
        print("Install grandalf to draw the graph as ASCII.")