import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.prompts import PromptTemplate, ChatPromptTemplate

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(openai_api_key=api_key, temperature=0.1)

template = ChatPromptTemplate.from_messages([
    ("system", "You are a geography expert. And you only reply in {language}."),
    ("ai", "Ciao, mi chiamo {name}"),
    ("human", "What is the distance between {country_a} and {country_b}. Also, what is your name?")
])
prompt = template.format_messages(language="korean", name="Nicolas", country_a="argentina", country_b="brazil")

print(chat.predict_messages(prompt))