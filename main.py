#!/usr/bin/env python3

from assistant import Assistant
from file_tools import read_file

def main():

    assistant = Assistant()

    print("AI Assistant started. Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")

        if user_input == "exit" or user_input == "q" or user_input == "quit":
            break

        elif user_input == "/clear":
            assistant.clear_history()
            print("\nAssistant:")
            print("Conversation cleared.")
            continue

        elif user_input == "/model":
            print("\nAssistant:")
            print(f"Current Model: {assistant.get_model()}")
            continue

        elif user_input == "/history":
            print("\nAssistant:")
            print(f"Messages in history: {assistant.get_history()}")
            continue

        elif "/summarize" in user_input:
            parts = user_input.split(" ")
            if len(parts) < 2:
                print("Usage: /summarize <filename>")
                continue
            
            filename = parts[1]
            content = read_file(filename)

            if content is None:
                print("File not found.")
                continue

            summary = assistant.summarize(content)
            print("\nAssistant:")
            print(summary)

            continue

        elif "/review" in user_input:
            parts = user_input.split(" ")
            if len(parts) < 2:
                print("Usage: /review <filename>")
                continue
            
            filename = parts[1]
            content = read_file(filename)
            
            if content is None:
                print("File not found.")
                continue

            review = assistant.review_code(content)
            print("\nAssistant:")
            print(review)

            continue

        response = assistant.send_message(user_input)

        print("\nAssistant:")
        print(response)

if __name__ == "__main__":
    main()