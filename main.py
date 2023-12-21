import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
from langchain.callbacks import StreamingStdOutCallbackHandler

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(
    openai_api_key=api_key,
    temperature=0.1,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
)

from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter

loader = UnstructuredFileLoader("./files/chapter_one.txt")
splitter = CharacterTextSplitter.from_tiktoken_encoder(separator="\n", chunk_size=100, chunk_overlap=20)

docs = loader.load()
print(splitter.split_documents(docs))
