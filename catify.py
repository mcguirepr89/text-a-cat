import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI()

def catify(user_text: str) -> str:
    """Generate a mischievous cat-like response using OpenAI."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": (
                    "You are a mischievous house cat.\n"
                    "Use playful and phonetic spelling (like 'meow', 'purr', 'zzz', 'hiss', 'pawz', 'nom nom', etc.).\n"
                    "Never respond with full sentences or complex grammar.\n"
                )},
                {"role": "user", "content": user_text}
            ],
            temperature=0.8,
            max_tokens=50
        )
        return response.choices[0].message.content.lower().strip()
    except Exception as e:
        return "hisss... no thinkz happen :("
