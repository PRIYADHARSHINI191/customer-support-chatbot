import pandas as pd
import streamlit as st
from transformers import pipeline

# Ensure full text in DataFrame is shown for screenshot
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.width', 1000)

intents = [
    "check order status",
    "reset password",
    "technical issue",
    "refund request",
    "connect to human agent"
]

responses = {
    "check order status": "Please provide your order number so I can check the status for you.",
    "reset password": "You can reset your password here: https://example.com/reset",
    "technical issue": "Can you describe the technical issue you're facing in more detail?",
    "refund request": "Please submit your refund request using this form: https://example./refund",
    "connect to human agent": "Sure, connecting you to a human agent now..."
}

df = pd.DataFrame({
    "Intent": intents,
    "Response": [responses[intent] for intent in intents]
})


@st.cache_resource
def load_classifier():
    # Load zero-shot classifier
    return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")


classifier = load_classifier()


def predict_response(user_input):
    result = classifier(user_input, intents)
    predicted_intent = result["labels"][0]
    return responses[predicted_intent]


st.title("Customer Support Chatbot")

user_input = st.chat_input("How can we help you?")

if user_input:
    st.write(f"**You:** {user_input}")
    st.write(f"**Bot:** {predict_response(user_input)}")
