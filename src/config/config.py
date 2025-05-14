from dotenv import load_dotenv
import os

def load_config():
    load_dotenv()
    return {
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "tavily_api_key": os.getenv("TAVILY_API_KEY")
    }