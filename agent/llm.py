import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()  

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Please export it or add it to a .env file."
        )

    return ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=api_key,
        temperature=0.2
    )
