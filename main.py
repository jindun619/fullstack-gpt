import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.schema import BaseOutputParser
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(openai_api_key=api_key, temperature=0.1)

chef_template = ChatPromptTemplate.from_messages([
    ("system", "You are a world-class international chef. You create easy to follow recipies for any type of cuisine with easy to find ingredients"),
    ("human", "I want to cook {} food")
])