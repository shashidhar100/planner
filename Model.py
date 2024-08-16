import getpass
import os
from langchain_openai import ChatOpenAI

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

def getOpenAIChatModel(**kwargs):
    model = ChatOpenAI(model="gpt-4o", **kwargs)
    return model
