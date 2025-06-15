
import openai
import streamlit as st

# Replace with your actual OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

st.set_page_config(page_title="Mini Copilot", page_icon="🤖")
st.title("🤖 Mini Copilot - Coding & Documentation Assistant")

# Sidebar for functionality selection
option = st.sidebar.selectbox("Choose a feature", [
    "Generate Code",
    "Explain Code",
    "Generate Documentation"
])

prompt = st.text_area("Enter your input:")

if st.button("Run"):
    if prompt:
        st.info(f"Running: {option}")
        if option == "Generate Code":
            instruction = f"Write code for: {prompt}"
        elif option == "Explain Code":
            instruction = f"Explain the following code:
{prompt}"
        elif option == "Generate Documentation":
            instruction = f"Generate detailed documentation for the following code:
{prompt}"

        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": instruction}]
            )
            output = response['choices'][0]['message']['content']
            st.text_area("Output:", value=output, height=300)
    else:
        st.warning("Please enter some text.")
