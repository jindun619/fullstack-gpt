import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
from langchain.callbacks import StreamingStdOutCallbackHandler

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(
    openai_api_key=api_key,
    temperature=0.1,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
)

# -------------------------------------------------------------------------------
from langchain.llms import gpt4all
from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("A {word} is a")

llm = gpt4all(path="./falcon.bin")

chain = prompt | llm

print(chain.invoke({"word": "tomato"}))
