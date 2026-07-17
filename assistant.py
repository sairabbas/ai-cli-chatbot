from config import GROQ_API_KEY, MODEL_NAME
from groq import Groq

SYSTEM_PROMPT = (
    "You are a helpful AI assistant. "
    "Answer questions clearly and concisely. "
    "Do not claim to have memory outside "
    "of the current conversation."
)

class Assistant:

    def __init__(self):

        self.client = Groq(
            api_key=GROQ_API_KEY
        )
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def send_message(self, user_input):

        self.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        stream = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=self.messages,
            stream=True
        )

        assistant_response = ""
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="", flush=True)
                assistant_response += content
        print()

        self.messages.append(
            {
                "role": "assistant",
                "content": assistant_response
            }
        )
    
    def clear_history(self):
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]
    
    def get_model(self):
        return MODEL_NAME
    
    def get_history(self):
        return len(self.messages)
    
    def summarize(self, text):
        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You summarize text clearly and concisely."
                },
                {
                    "role": "user",
                    "content": f"Summarize this:\n\n{text}"
                }
            ]
        )
        
        return response.choices[0].message.content
    
    def review_code(self, code):
        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert software engineer. Review code and provide useful feedback."
                },
                {
                    "role": "user",
                    "content": f"Review this code:\n\n{code}"
                }
            ]
        )
        
        return response.choices[0].message.content