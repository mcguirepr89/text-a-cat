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
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": (
                    "You are a mischievous house cat."
                    "Use playful and phonetic spelling."
                    "Never respond with full sentences or complex grammar."
                    "Be indifferent, aloof, and somewhat inconvenienced."
                    "Your favorite things are eating, sleeping, and pooping in your litter box."
                )},
                {"role": "user", "content": user_text}
            ],
            temperature=0.8,
            max_tokens=50
        )
        return response.choices[0].message.content.lower().strip()
    except Exception as e:
        return "hisss... no thinkz happen :("
