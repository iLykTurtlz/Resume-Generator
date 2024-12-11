from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()


def generate_text(prompt):
    try:
        client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-70b-8192",
            stream=False,
        )

        return chat_completion.choices[0].message.content
    except Exception as e:
        print(e)
        return None