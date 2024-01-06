import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
# -----------
import streamlit as st

from langchain.document_loaders import SitemapLoader


@st.cache_data(show_spinner="Loading website..")
def load_website(url):
    loader = SitemapLoader(url, filter_urls=[r"^(.*\/blog\/).*"])
    loader.requests_per_second = 5
    return loader.load()


st.title("SiteGPT")

with st.sidebar:
    url = st.text_input("Write down a URL", placeholder="https://example.com")

if url:
    if ".xml" not in url:
        with st.sidebar:
            st.error("Please write down a sitemap URL.")
    else:
        docs = load_website(url)
        st.write(docs)
