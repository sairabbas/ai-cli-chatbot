#!/usr/bin/env python3

from assistant import Assistant
from file_tools import read_file
from terminal import print_system, print_user, print_assistant

def main():

    assistant = Assistant()

    print_system("\nAI Assistant started. Type 'exit', 'quit', or 'q' to quit.")

    while True:
        print_user()
        user_input = input()

        if user_input == "exit" or user_input == "q" or user_input == "quit":
            break

        elif user_input == "/clear":
            assistant.clear_history()
            print_assistant("Conversation cleared.")
            continue

        elif user_input == "/model":
            print_assistant(f"Current Model: {assistant.get_model()}")
            continue

        elif user_input == "/history":
            print_assistant(f"Messages in history: {assistant.get_history()}")
            continue

        elif user_input.startswith("/summarize"):
            parts = user_input.split(" ")
            if len(parts) < 2:
                print_assistant("Usage: /summarize <filename>")
                continue
            
            filename = parts[1]
            content = read_file(filename)

            if content is None:
                print_assistant("File not found.")
                continue

            summary = assistant.summarize(content)
            print_assistant(summary)

            continue

        elif user_input.startswith("/review"):
            parts = user_input.split(" ")
            if len(parts) < 2:
                print_assistant("Usage: /review <filename>")
                continue
            
            filename = parts[1]
            content = read_file(filename)
            
            if content is None:
                print_assistant("File not found.")
                continue

            review = assistant.review_code(content)
            print_assistant(review)

            continue

        print_assistant("")
        assistant.send_message(user_input)

if __name__ == "__main__":
    main()