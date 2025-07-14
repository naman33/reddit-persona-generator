# persona_builder.py

import os
from dotenv import load_dotenv
import requests

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_persona(posts, comments):
    prompt = f"""
    Based on the following Reddit posts and comments, generate a detailed user persona.

    Posts:
    {posts[:10]}

    Comments:
    {comments[:10]}

    The persona should include:
    - Interests
    - Writing style
    - Personality traits
    - Occupation (if guessable)
    - Age group
    - Political/social views
    - Mental health insights (if applicable)

    Cite the post/comment used to infer each trait.
    """

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "mistralai/mistral-7b-instruct",  # Free model
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        raise Exception(f"OpenRouter Error: {response.status_code} - {response.text}")
