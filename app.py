import streamlit as st

from normalobjects_langgraph import ComplaintState, app


st.set_page_config(page_title="Downside Up Complaint Processor", page_icon="🌀")
st.title("Downside Up Complaint Processor")


def initialize_chat() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []


def clear_conversation() -> None:
    st.session_state.messages = []


def build_initial_state(complaint: str) -> ComplaintState:
    return {
        "complaint": complaint,
        "category": "",
        "valid": False,
        "investigation": "",
        "resolution": "",
        "final_response": "",
        "status": "pending",
        "workflow_path": [],
    }


def render_message(message: dict) -> None:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        details = message.get("details")
        if details:
            with st.expander("Workflow details", expanded=False):
                st.write(f"**category:** {details['category']}")
                st.write(f"**workflow_path:** {details['workflow_path']}")
                st.write(f"**status:** {details['status']}")
                st.write(f"**investigation:** {details['investigation']}")
                st.write(f"**resolution:** {details['resolution']}")


initialize_chat()

if st.button("Clear conversation"):
    clear_conversation()
    st.rerun()

for message in st.session_state.messages:
    render_message(message)

complaint = st.chat_input("Describe your complaint")

if complaint:
    st.session_state.messages.append({"role": "user", "content": complaint})

    with st.chat_message("user"):
        st.write(complaint)

    try:
        result = app.invoke(build_initial_state(complaint))
        assistant_message = {
            "role": "assistant",
            "content": result["final_response"],
            "details": {
                "category": result["category"],
                "workflow_path": result["workflow_path"],
                "status": result["status"],
                "investigation": result["investigation"],
                "resolution": result["resolution"],
            },
        }
        st.session_state.messages.append(assistant_message)

        with st.chat_message("assistant"):
            st.write(result["final_response"])
            with st.expander("Workflow details", expanded=False):
                st.write(f"**category:** {result['category']}")
                st.write(f"**workflow_path:** {result['workflow_path']}")
                st.write(f"**status:** {result['status']}")
                st.write(f"**investigation:** {result['investigation']}")
                st.write(f"**resolution:** {result['resolution']}")
    except Exception as exc:
        st.error(
            "The complaint processor could not complete this request. "
            "Please try again."
        )
