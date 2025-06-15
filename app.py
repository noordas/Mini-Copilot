
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
import os
print("Current working directory:", os.getcwd())
print("API Key from env:", os.getenv("OPENAI_API_KEY"))


# Load API key from .env file
load_dotenv()
from dotenv import load_dotenv
load_dotenv(dotenv_path="D:/Projects/Python/.env")  # 👈 use full path if needed

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Mini Copilot", layout="centered")
st.title("🤖 Mini Copilot – Coding & Documentation Assistant")

mode = st.radio("Choose Mode", ["Generate Code", "Explain Code", "Generate Docs"])
user_input = st.text_area("Enter your prompt or code here:", height=250)
prompt={}
if st.button("Run"):
    if not user_input.strip():
        st.warning("Please enter a prompt or code.")
    else:
        with st.spinner("Thinking..."):
            # Define the prompt based on mode
            if mode == "Generate Code":
                prompt = f"Write Python code for: {user_input}"
            elif mode == "Explain Code":
                prompt = f"Explain the following Python code in detail:\n{user_input}"
            elif mode == "Generate Docs":
                prompt = f"Generate detailed documentation or docstrings for this Python code:\n{user_input}"
            else:
                prompt = user_input

            try:
                response =client.chat.completions.create(
                model="gpt-4o",  # ✅ change this
                messages=[{"role": "user", "content": prompt}]
                )
                result = response.choices[0].message.content.strip()
                st.code(result)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
