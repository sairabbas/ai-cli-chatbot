from rich.console import Console
from rich.markdown import Markdown

console = Console()

def print_user():
    console.print("\nYou: ", style="bold cyan", end="")

def print_system(message):
    console.print(message, style="bold blue")

def print_assistant(message):
    console.print("\nAssistant:", style="bold green")
    console.print(Markdown(message))