import os
import chainlit as cl
from dotenv import load_dotenv
from cohere import ClientV2

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
client = ClientV2(api_key=COHERE_API_KEY)


@cl.on_message
async def process_user_query(message: cl.Message):
    user_question = message.content.strip()

    # Build the system + user messages for math solving
    messages = [
        {
            "role": "system",
            "content": "You are a helpful math assistant. Solve the following problem step-by-step."
        },
        {
            "role": "user",
            "content": user_question
        }
    ]

    response_text = ""
    for chunk in client.chat_stream(
            model="command-a-03-2025",
            messages=messages,
            temperature=0.3
    ):
        if hasattr(chunk, "message") and hasattr(chunk.message, "content"):
            response_text += chunk.message.content
