import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback

from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from langchain.callbacks import StreamingStdOutCallbackHandler

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    openai_api_key=api_key,
    temperature=0.1,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
)

memory = ConversationSummaryBufferMemory(
    llm=llm, max_token_limit=120, memory_key="chat_history"
)

template = """
    You are a helpful AI talking to a human.

    {chat_history}
    Human:{question}
    You:
"""

chain = LLMChain(
    llm=llm,
    memory=memory,
    prompt=PromptTemplate.from_template(template),
    verbose=True,
)

print(chain.predict(question="Hi, my name is Hoojun"))
print(chain.predict(question="I live in Seoul"))
print(chain.predict(question="what is my name?"))
