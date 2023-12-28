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
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, CacheBackedEmbeddings
from langchain.vectorstores import Chroma
from langchain.storage import LocalFileStore
from langchain.chains import RetrievalQA

cache_dir = LocalFileStore("./.cache/")


splitter = CharacterTextSplitter.from_tiktoken_encoder(
    separator="\n",
    chunk_size=600,
    chunk_overlap=100,
)
loader = UnstructuredFileLoader("./files/chapter_one.txt")

docs = loader.load_and_split(text_splitter=splitter)

embeddings = OpenAIEmbeddings()

cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embeddings, cache_dir)

vectorstore = Chroma.from_documents(docs, cached_embeddings)

chain = RetrievalQA.from_chain_type(
    llm=model, chain_type="stuff", retriever=vectorstore.as_retriever()
)

chain.run("")
