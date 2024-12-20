# Import necessary libraries
import streamlit as st  # For building the web app interface
from langchain.prompts import ChatPromptTemplate  # For creating prompt templates
from langchain_core.output_parsers import StrOutputParser  # For processing output text
from langchain.llms import Ollama  # For using the Ollama language model

# Initialize the Ollama model with a specific model version (llama3.1:8b)
model = Ollama(model="llama3.1:8b")

# Define a generic prompt template for language translation
generic_template = "Translate the following into {language}:"

# Create a chat-based prompt template using the defined generic template
prompt = ChatPromptTemplate.from_messages(
    [("system", generic_template), ("user", "{text}")]
)

# Set up the output parser to process the model's output as a string
parser = StrOutputParser()

# Chain the prompt, model, and parser together
chain = prompt | model | parser

# Streamlit app interface begins

# Set the title of the web app
st.title("Language Translator using Ollama")

# Create input fields for users to type the text and the target translation language
input_text = st.text_input("Type the Word or Sentence", "Hello")
input_language = st.text_input("Translation Language", "Swedish")

# Define a button that will trigger the translation process
if st.button("Translate"):
    try:
        # Invoke the chain of prompt, model, and parser to generate the translated output
        translated_output = chain.invoke({"language": input_language, "text": input_text})
        
        # Display the translated output in the app
        st.write("**Translated output:**", translated_output)
    except Exception as e:
        # Handle errors and display error message if translation fails
        st.error(f"Error During Translation: {e}")
