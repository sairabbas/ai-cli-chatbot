#!/usr/bin/env python3

# from openai import OpenAI
# from google import genai
from dotenv import load_dotenv
from groq import Groq
import os

# Load variables from .env
load_dotenv()

# Create connection to OpenAI API
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
# client = genai.Client(
#     api_key=os.getenv("GEMINI_API_KEY")
# )
# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")
# )

def testAPI():

    # Send a request to the model
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": "Explain what an API is"
            }
        ]
    )
    # response = client.models.generate_content(
    #     model="gemini-2.0-flash",
    #     contents="Explain what an API is in one sentence."
    # )
    # response = client.responses.create(
    #     model="gpt-5-mini",
    #     input="Explain what an API is in one sentence."
    # )

    # Print the AI response
    print(response.choices[0].message.content)
    #print(response.text)
    # print(response.output_text)

def main():
    testAPI()

if __name__ == "__main__":
    main()