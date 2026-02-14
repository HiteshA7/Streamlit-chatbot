import os
import dotenv
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = "AIzaSyBQbWaKhSr6kTftPDLfEeuwNJhaFD4GTZo"

chat_model = ChatGoogleGenerativeAI(model = "models/gemini-flash-lite-latest")

import streamlit as st

if "conver" not in st.session_state:
    st.session_state["conver"] = []
    st.session_state["memory"] = []
    st.session_state["memory"].append(('system','act as my mother'))

user_data = st.chat_input("user message")

if user_data:
    st.session_state["memory"].append(("human",user_data))
    
    output = chat_model.invoke(st.session_state["memory"])

    st.session_state["memory"].append(("ai",output.content))

    st.session_state["conver"].append({"role":"human","data": user_data})
    st.session_state["conver"].append({"role":"ai","data":output.content})

    if user_data=="bye":
        st.session_state["memory"] = []

for y in st.session_state["conver"]:
    with st.chat_message(y["role"]):
        st.write(y["data"])
