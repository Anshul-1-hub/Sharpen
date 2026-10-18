from groq import Groq
import os
import json
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def gen_problems(scores):
    weakest = None
    highest = 0
    for pattern in scores:
        if scores[pattern] > highest:
            highest = scores[pattern]
            weakest = pattern

    def gen_prompt(weakest, highest):
        return f"""
        You are DSA mentor. You are given a pattern on which the user struggles the most. Your job is to generate 5 problems related to that pattern only so that the user improves at it, if the weakness score is high, start with some easier questions else start with some moderate questions.

        Pattern: {weakest}
        Score: {highest}

        In the input, Pattern tells the user's weakest pattern and the score tells about the user's weakness score in that particular pattern. If the pattern is "None", dont give any problems and just say "No weak topics as of now!"

        Reply with JSON structure like below:

        [
            {{"title": "...", "difficulty": "...", "description": "..."}},
            {{"title": "...", "difficulty": "...", "description": "..."}}
        ]

        Reply in JSON format strictly.
    """

    prompt = gen_prompt(weakest, highest)
    result = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="openai/gpt-oss-120b"
    )

    res = result.choices[0].message.content
    return json.loads(res)