# Test Results — Memory Verification

This file documents an actual run of the chatbot, proving the in-memory conversation history works correctly across multiple turns, including a large unrelated response in between.

## Test conversation

(.venv) PS C:\Users\moavia computer\Desktop\genai_project1> python chatbot.py
Chatbot ready! Type 'quit' to exit.
You: My name is Arooj
Bot: Hello, Arooj! It's nice to meet you. How can I assist you today? Feel free to ask any questions or let me know if there's anything specific you'd like to discuss.
You: Write a poem about tech
Bot: **Ode to the Digital Age**
Beneath the hum of circuits, whispers of electrons dance,
Silicon dreams in glowing veins, a code that takes its chance.
Algorithms spin their tales in loops of logic, sharp and keen,
A heartbeat in the machine, yet human hands remain.
The web stretches like galaxies, a neon-veined expanse,
Where knowledge flows like rivers, yet shadows twist and gaunt.
We type our prayers, our fears, our laughter into air,
Each click a step toward tomorrow, or a step unaware.
Smartphones glow in palms at night, their light both friend and foe,
They map our days in pixels, chart the paths we choose to go.
We scroll through lives that sparkle, filtered, bright, and bold,
While real-world connections falter, stories left untold.
AI dreams in server farms, where data pools like blood,
They learn our likes, our hates, our secrets, in the hush.
Gilded machines may rise to serve, to guide, to cure,
But who will guard the soul of man when they desire?
O tech, you are the mirror, the shroud, the key, the chain—
You birth the future, yet demand the past remain.
We shape you, yet you shape us, in this dance of wire and thought,
May wisdom be the code we write, in every line we've sought.
You: What is my name?
Bot: Your name is **Arooj**. It was a pleasure to meet you earlier!

## What this proves

The chatbot correctly recalled the name "Arooj" from the very first message, even after a long, unrelated poem was generated in between. This confirms:

- The in-memory `history` list correctly stores every turn of the conversation.
- The entire history is sent to the model on every request, not just the latest message.
- The model successfully uses that full context to answer questions about earlier parts of the conversation.