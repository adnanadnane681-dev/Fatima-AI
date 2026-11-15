import os
import streamlit as st
from google import genai

# Set up page config
st.set_page_config(page_title="Fatima AI", page_icon="🤖", layout="centered")

st.title("🤖 Fatima AI")
st.write("Ina kwana! Ni ce Fatima AI, mai taimaka maka da harshen Hausa da Turanci.")

# Initialize the Gemini client using the environment variable for the API key
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.warning("Don Allah a saita GEMINI_API_KEY a matsayin Secret a Render ko yanayin aiki.")
else:
    client = genai.Client(api_key=api_key)

    # Initialize chat history in session state if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ka tambayi Fatima AI ko me kake so..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response using Gemini
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            try:
                # Using the recommended gemini-2.5-flash model
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                bot_response = response.text
                message_placeholder.markdown(bot_response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": bot_response})
            except Exception as e:
                error_msg = f"An samu matsala: {e}"
                message_placeholder.error(error_msg)
              
