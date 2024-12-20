import streamlit as st
from langchain.prompts import ChatpromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.llms import Ollama

model = Ollama(model="llama3.1:8b")

# define Prompt Template

generic_template= "Translate the following into {language}:"
prompt = ChatpromptTemplate.from_messages(
    [("sytem",generic_template), ("user",{text})]
)

parser = StrOutputParser()

chain = prompt|model|parser

# Streamlit App

st.title("Language Translator using Ollama")

# Input Fields

input_text = st.text_input("Type the Word or Sentence","Hello")
input_language = st.text_input("Translation Language","Swedish")


# Define Buttons

if st.button("Translate"):
    try:
        translated_output = chain.invoke({"language":input_language, "text":input_text})
        st.write("**Translated output:**", translated_output)
    except Exception as e:
        st.error(f"Error During Translation: {e}")