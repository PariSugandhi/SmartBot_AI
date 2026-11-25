
import streamlit as st
st.set_page_config(page_title="SmartBot AI", page_icon="🤖")
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

# Connect to AI model
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("API key not found. Check your .env file.")
    st.stop()

client = OpenAI(api_key=api_key)

# Website title
st.set_page_config(page_title="SmartBot AI", page_icon="🤖")

st.title("🤖 SmartBot AI")
st.caption("Your personal AI assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Take user input
prompt = st.chat_input("Ask me anything...")

if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.responses.create(
                    model="gpt-4.1-mini",
                    instructions=(
                        "You are SmartBot, a helpful and friendly "
                        "AI assistant. Explain answers clearly."
                    ),
                    input=st.session_state.messages
                )

                answer = response.output_text
                st.markdown(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as e:
                st.error(f"Something went wrong: {e}")
