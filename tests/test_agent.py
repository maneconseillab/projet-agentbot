import pytest
from src.agent.agent_setup import setup_agent

def test_agent_response():
    agent = setup_agent()
    response = agent.invoke({"messages": [HumanMessage(content="Salut !")]})
    assert "Fred" in response["messages"][-1].content