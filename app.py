import streamlit as st
from src.agent.agent_setup import setup_agent
from src.config.config import load_config
from src.utils.streamlit_utils import display_message, stream_response
from langchain_core.messages import HumanMessage

# Charger les configurations
config = load_config()

# Initialiser l'agent
agent_executor = setup_agent()

# Interface Streamlit
st.title("Chat avec Agent_Mané 😎")

# Initialiser l'historique des messages
if "messages" not in st.session_state:
    st.session_state.messages = []
if "thread_id" not in st.session_state:
    st.session_state.thread_id = "thread-1"

# Afficher l'historique
for msg in st.session_state.messages:
    display_message(msg)

# Zone de saisie
user_input = st.chat_input("Tape ton message pour l'agent Agent_Mané...")

# Traiter l'entrée utilisateur
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    display_message({"role": "user", "content": user_input})

    config = {"configurable": {"thread_id": st.session_state.thread_id}}
    inputs = {"messages": [HumanMessage(content=user_input)]}

    response = stream_response(agent_executor, inputs, config)
    st.session_state.messages.append({"role": "assistant", "content": response})