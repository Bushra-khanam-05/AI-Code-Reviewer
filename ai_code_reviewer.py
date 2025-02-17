import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import  SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") 

# Set up the Streamlit app interface
st.title("AI Code Reviewer")
st.write("Paste your code below and click *Review Code* to get an AI-based review.")

# Text area for code input
code_input = st.text_area("Enter your code here:", height=300)

if st.button("Review Code"):
    if code_input.strip():
        # Initialize the language model
        llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro",temperature=0)

        # System message to instruct the model as an expert code reviewer
        system_message = SystemMessage(
            content=
                """You are an expert AI code reviewer. When given code, provide a detailed review 
                including feedback on structure, readability, potential bugs, and suggestions for improvement."""
            
        )

        # Create the human message with the code to review
        human_message = HumanMessage(content=f"Please review the following code:\n{code_input}")

        # Get the review response from the model
        response = llm.invoke([system_message, human_message])

        # Display the review in the Streamlit app
        st.subheader("Review:")
        st.write(response.content)
    else:
        st.error("Please enter some code to review.")