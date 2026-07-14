#!/usr/bin/env python3

from dotenv import load_dotenv
from openai import OpenAI
import os

# Load variables from .env
load_dotenv()

# Create connection to OpenAI API
client = OpenAI()

def testAPI():

    # Send a request to the model
    response = client.responses.create(
        model="gpt-5-mini",
        input="Explain what an API is in one sentence."
    )

    # Print the AI response
    print(response.output_text)

def main():
    testAPI()

if __name__ == "__main__":
    main()