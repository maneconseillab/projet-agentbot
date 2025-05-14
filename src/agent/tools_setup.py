from langchain_community.tools import TavilySearchResults

def setup_tools():
    return [TavilySearchResults(max_results=2)]