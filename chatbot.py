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

    print("Bot:", reply)