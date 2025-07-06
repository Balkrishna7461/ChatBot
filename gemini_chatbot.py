import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Custom CSS for chat bubbles and fixed input bar
st.markdown(
    """
    <style>
    .chat-container {
        max-width: 700px;
        margin: 0 auto;
        padding-bottom: 80px;
    }
    .chat-bubble {
        padding: 12px 18px;
        border-radius: 18px;
        margin-bottom: 10px;
        max-width: 80%;
        font-size: 1.1em;
        line-height: 1.5;
        word-break: break-word;
        display: inline-block;
    }
    .user-bubble {
        background: #0057b8;
        color: #fff;
        margin-left: 20%;
        text-align: right;
        float: right;
    }
    .bot-bubble {
        background: #222;
        color: #fff;
        margin-right: 20%;
        text-align: left;
        float: left;
    }
    .clear { clear: both; }
    .fixed-input {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100vw;
        background: #181818;
        padding: 16px 0 12px 0;
        z-index: 100;
        box-shadow: 0 -2px 8px rgba(0,0,0,0.15);
    }
    .stTextInput>div>div>input {
        font-size: 1.1em;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Hide Streamlit footer and menu
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.title("🤖 Gemini Chatbot")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Display chat history with chat bubbles
for sender, message in st.session_state["chat_history"]:
    if sender == "user":
        st.markdown(f'<div class="chat-bubble user-bubble">{message}</div><div class="clear"></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble bot-bubble">{message}</div><div class="clear"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Fixed input bar at the bottom
with st.container():
    st.markdown('<div class="fixed-input">', unsafe_allow_html=True)
    col1, col2 = st.columns([8,1])
    with col1:
        user_input = st.text_input("You:", "", key="input", label_visibility="collapsed", placeholder="Ask anything...")
    with col2:
        send_clicked = st.button("Send", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

if send_clicked and user_input:
    st.session_state["chat_history"].append(("user", user_input))
    try:
        response = model.generate_content(user_input)
        bot_reply = response.text if hasattr(response, "text") else str(response)
    except Exception as e:
        bot_reply = f"Error: {e}"
    st.session_state["chat_history"].append(("bot", bot_reply))
    st.rerun()
