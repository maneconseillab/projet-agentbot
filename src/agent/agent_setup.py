from langchain_openai import ChatOpenAI
from langchain_community.tools import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.prompts import ChatPromptTemplate

def setup_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", "Tu es Fred, un robot serviable qui répond toujours à la cool."),
        ("placeholder", "{messages}"),
        ("user", "n'hésite pas à répondre avec humour !"),
    ])

def setup_agent():
    model = ChatOpenAI(model="gpt-4")
    search = TavilySearchResults(max_results=2)
    tools = [search]
    memory = MemorySaver()
    prompt = setup_prompt()
    return create_react_agent(
        model, tools, checkpointer=memory, state_modifier=lambda state: prompt.invoke({"messages": state["messages"]})
    )