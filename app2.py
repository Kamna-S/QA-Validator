from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

# Function to generate a trivia question based on the selected topic
def generate_question(topic):
    prompt = f"Generate a trivia question related to {topic}."
    response = chat.send_message(prompt)
    return response.text if response else "No question generated."

# Function to validate the user's answer
def validate_answer(question, user_answer):
    validation_prompt = f"Question: {question}\nUser Answer: {user_answer}\nIs the answer correct? Please provide a brief validation."
    response = chat.send_message(validation_prompt)
    return response.text if response else "Unable to validate the answer."

# Initialize Streamlit app
st.set_page_config(page_title="Answer Validator")

st.header("Answer Validator")

# 1. Dropdown menu for selecting a topic
topic = st.selectbox("Select a topic for the question:", ["Geography", "Health", "Sports"])

# 2. Placeholder to display the generated question
if 'generated_question' not in st.session_state:
    st.session_state['generated_question'] = None

if st.button("Generate Question"):
    # Generate a question for the selected topic
    st.session_state['generated_question'] = generate_question(topic)

# Display the generated question
if st.session_state['generated_question']:
    st.subheader("Generated Question")
    st.write(st.session_state['generated_question'])

# 3. Input box for the user to provide their answer
user_answer = st.text_input("Your Answer:")

# Button to submit the answer and validate it
if st.button("Submit Answer"):
    if st.session_state['generated_question'] and user_answer:
        # Validate the user's answer
        validation_response = validate_answer(st.session_state['generated_question'], user_answer)
        st.subheader("Validation Result")
        st.write(validation_response)
    else:
        st.error("Please generate a question and provide an answer before submitting.")


