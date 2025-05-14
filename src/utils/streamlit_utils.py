import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

def display_message(message):
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(message["content"])

def stream_response(agent_executor, inputs, config):
    full_response = ""
    with st.chat_message("assistant"):
        placeholder = st.empty()
        for s in agent_executor.stream(inputs, config, stream_mode="values"):
            message = s["messages"][-1]
            if isinstance(message, AIMessage):
                full_response += message.content
                placeholder.markdown(full_response + "▌")
        placeholder.markdown(full_response)
    return full_response