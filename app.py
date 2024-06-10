import streamlit as st
import requests
import json
from PIL import Image


st.set_page_config(
    page_title="Lyzr Test Case Generator",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("lyzr-logo.png")
st.image(image, width=150)

st.title("Lyzr Employee Training Chatbot")
st.markdown("### Welcome to the Lyzr Employee Training Chatbot!")
st.markdown("This app uses Lyzr ChatBot to assist with CNC machines and their parts. We have integrated comprehensive CNC machines and Their parts information. Feel free to ask any questions related to health insurance.")
st.markdown("Suggested Question: ")
st.markdown("1) Types of CNC machines We have?")
st.markdown("2) what is a part number for motor used in cnc milling machine?")
def get_chatbot_response(message):
    url = "http://54.82.183.144:5555/chat/a9e0bfda-df21-489f-bed0-51289af46b07?"

    payload = json.dumps([
        {
            "role": "user",
            "content": "string",
            "metadata": {}
        }
    ])
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 3ewtowetkgsdgpsdgsdgoetewtm'
    }

    params = {"input_message": message}

    response = requests.request("POST", url, headers=headers, data=payload, params=params)

    return response.json()['details']['response']


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = get_chatbot_response(prompt)
        chat_response = response
        response = st.write(chat_response)
    st.session_state.messages.append(
        {"role": "assistant", "content": chat_response}
    )

