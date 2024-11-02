# AI-Powered Question-Answer Bot

## Project Overview
This project is a web-based question-answer bot that uses Generative AI to dynamically generate questions and validate user responses. It allows users to select a topic, answer generated questions, and receive feedback on the accuracy of their answers.

## Features
- **Interactive Web Interface**: Built with Streamlit, the interface includes:
  - A dropdown menu for selecting a topic (Geography, Health, or Sports).
  - A display area for showing the generated question.
  - An input box where users can submit their answers.

- **LLM Integration**:
  - The bot generates questions dynamically based on the chosen topic using a Large Language Model (LLM) such as OpenAI's GPT.
  - User answers are validated by sending both the question and user response to the LLM for accuracy checks.

- **Real-Time Feedback**: After submitting an answer, the bot provides feedback on whether the answer is correct or not.

## Technologies Used
- **Streamlit**: For building the web-based user interface.
- **Python-dotenv**: For managing environment variables.
- **Generative AI API**: For question generation and answer validation.
