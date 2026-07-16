# Custom AI Chatbot with Memory

**Project 1 — Generative AI Industrial Training Kit (DecodeLabs, Batch 2026)**

## What this is
A terminal-based chatbot that remembers previous messages during a live conversation session. It demonstrates how to turn a stateless LLM API into a stateful, context-aware conversational tool.

## How it works
- The chatbot connects to an LLM through the OpenRouter API (OpenAI-compatible SDK).
- Every user message and every model response is stored in an in-memory Python list called `history`.
- On every new turn, the entire `history` list is sent to the model — not just the latest message — so the model has full context of the conversation so far.
- This proves the core concept: the LLM itself has no memory. All "memory" is built and maintained on the client side.

## Requirements
- Python 3.10+
- An OpenRouter API key (free) from https://openrouter.ai/keys

## Setup

1. Install dependencies: pip install openai python-dotenv
2. Create a `.env` file in the project folder (see `.env.example` for the format): OPENROUTER_API_KEY=your_actual_key_here
3. Run the chatbot: python chatbot.py
4. Type messages normally. Type quit to exit.

## Example test (memory verification)
You: My name is Arooj
Bot: Hello, Arooj! Nice to meet you...

You: Write a poem about tech
Bot: (long poem generated)

You: What is my name?
Bot: Your name is Arooj.

This confirms the chatbot correctly recalls information from earlier in the conversation, even after a large unrelated response was generated in between.

## Notes
- The free model used (poolside/laguna-xs-2.1:free) is subject to change on OpenRouter's end — if it stops working, check https://openrouter.ai/models?max_price=0 for a current free alternative and update the model= line in chatbot.py.
- .env is excluded from version control via .gitignore to keep the API key private.