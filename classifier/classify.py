from groq import Groq
import os
import json
from .prompt import make_prompt

from dotenv import load_dotenv
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

def classify(question, code):
    prompt = make_prompt(question, code)
    result = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="openai/gpt-oss-120b"
    )

    res = result.choices[0].message.content
    return json.loads(res)