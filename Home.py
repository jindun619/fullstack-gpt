import streamlit as st

st.title("Hello World!")
st.subheader("Welcome to Streamlit")
st.markdown(
    """
 #### I love it!
"""
)

with st.sidebar:
    st.title("Sidebar Title")
    st.text_input("input1")

tab1, tab2, tab3 = st.tabs(["a", "b", "c"])

with tab1:
    st.write("1")
with tab2:
    st.write("2")
with tab3:
    st.write("3")
