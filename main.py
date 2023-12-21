import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback

# from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.prompts.few_shot import (
    FewShotPromptTemplate,
    FewShotChatMessagePromptTemplate,
)
from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from langchain.prompts.example_selector.base import BaseExampleSelector

# from langchain.schema import BaseOutputParser
from langchain.callbacks import StreamingStdOutCallbackHandler

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(
    openai_api_key=api_key,
    temperature=0.1,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
)

examples = [
    {
        "question": "France?",
        "answer": """
        Here is what I know:
        Capital: Paris
        Language: French
        Food: Wine and Cheese
        Currency: Euro
        """,
    },
    {
        "question": "Italy?",
        "answer": """
        I know this:
        Capital: Rome
        Language: Italian
        Food: Pizza and Pasta
        Currency: Euro
        """,
    },
    {
        "question": "Greece?",
        "answer": """
        I know this:
        Capital: Athens
        Language: Greek
        Food: Souvlaki and Feta Cheese
        Currency: Euro
        """,
    },
]


class RandomExampleSelector(BaseExampleSelector):
    def __init__(self, examples):
        self.examples = examples

    def add_example(self, example):
        self.examples.append(example)

    def select_examples(self, input_variables):
        from random import choice

        return [choice(self.examples)]


example_prompt = PromptTemplate.from_template("Human: {question}\nAI:{answer}")

# example_selector = LengthBasedExampleSelector(
#     examples=examples, example_prompt=example_prompt, max_length=80
# )
example_selector = RandomExampleSelector(examples=examples)

prompt = FewShotPromptTemplate(
    example_prompt=example_prompt,
    example_selector=example_selector,
    suffix="Human: What do you know about {country}?",
    input_variables=["country"],
)
# print(prompt.format(country="brazil"))

# final_prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a geography expert, you give short answers"),
#         example_prompt,
#         ("human", "What do you know about {country}?"),
#     ]
# )

# chain = final_prompt | chat
# print(chain.invoke({"country": "germany"}))
with get_openai_callback() as usage:
    chat.predict("너한테 질문을 하고 있는데 왜 usage는 0USD라고 표시돼?")
    print(usage)
