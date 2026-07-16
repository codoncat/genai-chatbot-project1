import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the secret key from the .env file
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Connect to OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# This empty list is our chatbot's memory
history = []

MAX_TURNS = 10  # keeps the last 10 user+bot exchanges (20 messages total)

def trim_history(history, max_turns=MAX_TURNS):
    max_messages = max_turns * 2
    if len(history) > max_messages:
        history = history[-max_messages:]
    return history

print("Chatbot ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input == "":
        continue

    if user_input.lower() == "quit":
        break

    history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="poolside/laguna-xs-2.1:free",
        messages=history,
    )

    reply = response.choices[0].message.content

    history.append({"role": "assistant", "content": reply})

    history = trim_history(history)

    print("Bot:", reply)