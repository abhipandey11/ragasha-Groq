import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = None

def get_client():
    global client
    if client is None:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    return client

def generate_answer(prompt):
    client = get_client()

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content