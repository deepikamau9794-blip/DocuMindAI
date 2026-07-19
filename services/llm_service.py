import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


api_key = os.getenv("GROQ_API_KEY")


if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found in .env file."
    )


client = Groq(
    api_key=api_key
)


def generate_response(
    prompt,
    temperature=0.2,
    max_tokens=1500
):
    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=temperature,

        max_tokens=max_tokens
    )

    return response.choices[0].message.content