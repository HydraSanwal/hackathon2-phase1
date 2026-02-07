"""
Main entry point for the Todo App
"""
from .cli.todo_cli import TodoCLI


def main():
    """Main function to run the Todo CLI application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()