import streamlit as st

from normalobjects_langgraph import ComplaintState, app





st.set_page_config(
    page_title="Downside Up Complaint Processor",
    page_icon="🌀"
)

# Opening image
st.image(
    "background.jpg",
    use_container_width=True
)


st.markdown(
    f"""
    <style>

    /* Main app background */
    .stApp {{
        background:
            radial-gradient(circle at top, rgba(180,40,10,0.25), transparent 40%),
            linear-gradient(
                180deg,
                #050505 0%,
                #0b0000 50%,
                #120300 100%
            );

        color: #eeeeee;
    }}


    /* Hide default Streamlit header */
    header[data-testid="stHeader"] {{
        background: transparent;
    }}


    /* Title */
    h1 {{
        color: #ff4b1f !important;
        font-family: "Courier New", monospace;
        text-transform: uppercase;
        letter-spacing: 4px;
        text-shadow:
            0 0 5px #ff4b1f,
            0 0 15px #ff1a00,
            0 0 30px #8b0000;
    }}


    /* Subtitle / text */
    p, label {{
        color: #dddddd !important;
    }}


    /* Chat messages */
    [data-testid="stChatMessage"] {{
        background: rgba(20, 5, 5, 0.85);
        border: 1px solid rgba(255,70,20,0.35);
        border-radius: 12px;
        padding: 10px;
        box-shadow:
            0 0 10px rgba(255,50,0,0.15);
    }}


    /* User messages */
    [data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {{
        border-left: 4px solid #ff8c00;
    }}


    /* Assistant messages */
    [data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) {{
        border-left: 4px solid #b30000;
    }}


    /* Chat input */
    textarea {{
        background-color: #120606 !important;
        color: white !important;
        border: 1px solid #ff4500 !important;

        box-shadow:
            0 0 15px rgba(255,69,0,0.4);
    }}


    /* Buttons */
    button {{
        background:
            linear-gradient(
                90deg,
                #8b0000,
                #ff4500
            ) !important;

        color:white !important;
        border:none !important;
        border-radius:8px !important;

        box-shadow:
            0 0 10px rgba(255,70,0,0.5);
    }}


    button:hover {{
        box-shadow:
            0 0 25px rgba(255,80,0,0.9);
        transform: scale(1.03);
    }}


    /* Expanders */
    details {{
        background: rgba(30,5,5,0.7);
        border: 1px solid #661100;
        border-radius:10px;
    }}


    /* Scrollbar */
    ::-webkit-scrollbar {{
        width: 8px;
    }}

    ::-webkit-scrollbar-track {{
        background:#050505;
    }}

    ::-webkit-scrollbar-thumb {{
        background:#8b0000;
        border-radius:10px;
    }}


    </style>
    """,
    unsafe_allow_html=True
)


# Custom title
st.markdown(
    """
    <h1>
    🌀 DOWNSIDE UP<br>
    <span style="font-size:28px;">
    Complaint Processing Lab
    </span>
    </h1>

    <p style="
    color:#ff8c00;
    font-family:Courier New;
    letter-spacing:3px;
    ">
    AI INVESTIGATION SYSTEM // ONLINE
    </p>
    """,
    unsafe_allow_html=True
)


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
