LangGraph Lab Implementation Plan
## Step 1 — Project setup

Goal: Create a clean project structure.

Do:

create .env
create .gitignore
create README.md
create lab_proof.md
create requirements.txt
create normalobjects_langgraph.py

Reuse from previous lab:

config.py (or equivalent environment loading)
.env

Install:

pip install langgraph langchain langchain-openai python-dotenv

Verify:

imports work
OpenAI client initializes
## Step 2 — Define workflow state

Goal: Define one object that flows through every node.

Create:

class ComplaintState(TypedDict):

Suggested fields:

complaint
category
valid
investigation
resolution
final_response
status
workflow_path

Explanation:
Every node receives this dictionary, updates it, and returns it.

Verify:

create an example state
print it
## Step 3 — Create the LLM

Reuse only:

load_dotenv()
ChatOpenAI(...)

Do not recreate:

tools
agent
AgentExecutor
prompt

LangGraph nodes call the LLM directly.

Verify:
Simple:

llm.invoke(...)
## Step 4 — Build Intake node

Purpose:

read complaint
classify into
portal
monster
psychic
environmental
other

Update:

category
status
workflow_path

Verify:
Run node independently.

## Step 5 — Build Validation node

Purpose:
Determine whether complaint belongs to the Downside Up universe.

Output:

valid=True

or

valid=False

Update:

workflow_path
status

Verify:
Test:

valid complaint
nonsense complaint
## Step 6 — Build Investigation node

Purpose:
Use LLM to gather relevant information based on

category
complaint

Store:

investigation

Update:

workflow_path
status

Verify:
Run independently.

## Step 7 — Build Resolution node

Purpose:
Generate solution using

complaint
+
investigation

Store:

resolution

Update:

workflow_path
status
## Step 8 — Build Closure node

Purpose:
Produce final response.

Store:

final_response

Update:

workflow_path
status
## Step 9 — Build Reject node

Purpose:
Handle invalid complaints.

Store:

final_response

Example:

Complaint rejected because it is unrelated to the Downside Up workflow.

Update:

workflow_path
status
## Step 10 — Build the graph

Create

StateGraph(ComplaintState)

Add nodes

intake
validate
investigate
resolve
close
reject

Create edges

intake
      ↓
validate
      ↓
   valid?
   /    \
 yes    no
 ↓       ↓
investigate reject
 ↓          ↓
resolve     END
 ↓
close
 ↓
END

Compile

app = workflow.compile()

Verify:
Print graph.

## Step 11 — Test workflow

Create

test_complaints = [...]

Include

portal
monster
psychic
environmental
invalid complaint

For every complaint print

category
workflow_path
status
final_response
## Step 12 — Visualize execution

Print

workflow_path

Example

intake
→ validate
→ investigate
→ resolve
→ close

For invalid complaint

intake
→ validate
→ reject
## Step 13 — Document comparison

In lab_proof.md

Include

LangChain
LLM decides path
flexible
unpredictable
LangGraph
developer defines path
deterministic
easy to debug
traceable
Optional Extensions (after the core lab)
Parallel investigation
Retry failed nodes
Human approval node
Persistent state
Streamlit interface
Codex recommendation

Have Codex implement one step at a time:

Setup
State
Intake node
Validation node
Investigation node
Resolution node
Closure node
Reject node
Graph
Tests

After each step:

run the code,
fix errors,
commit,
then continue.

## follow and update
update AGENT.md after every step
mark every step from the implementat_plan as completed once it was successfully tested