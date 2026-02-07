"""
TodoCLI providing command-line interface for the todo application
"""
import sys
import os
from typing import List
from ..services.todo_service import TodoService


class TodoCLI:
    """Command-line interface for the todo application."""

    def __init__(self):
        """Initialize the CLI with a TodoService instance."""
        self.service = TodoService()
        # Try to set UTF-8 encoding for better emoji support
        try:
            if sys.platform == 'win32':
                os.system('chcp 65001 > nul')
        except:
            pass

    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        """Print the application header."""
        print("=" * 60)
        print("                    TODO APP                             ")
        print("=" * 60)

    def display_todos(self):
        """Display all current todos in a nice format."""
        todos = self.service.get_all_todos()

        if not todos:
            print("\n>> Your Todo List: (Empty)")
            print("-" * 60)
            print("   No todos yet. Add one to get started!")
        else:
            print(f"\n>> Your Todo List: ({len(todos)} items)")
            print("-" * 60)
            for todo in todos:
                status_icon = "[X]" if todo['completed'] else "[ ]"
                status_text = "Complete" if todo['completed'] else "Incomplete"
                print(f"   {status_icon} [{todo['id']}] {todo['description']}")
                print(f"       Status: {status_text}")
                print()

    def show_menu(self):
        """Display the main menu."""
        print("-" * 60)
        print("                      MAIN MENU                           ")
        print("-" * 60)
        print("   1. Add a new todo")
        print("   2. View all todos")
        print("   3. Update a todo")
        print("   4. Mark todo as complete")
        print("   5. Mark todo as incomplete")
        print("   6. Delete a todo")
        print("   7. Exit")
        print("-" * 60)

    def run(self):
        """Start the CLI loop with menu-driven interface."""
        while True:
            try:
                self.clear_screen()
                self.print_header()
                self.display_todos()
                self.show_menu()

                choice = input("\n>> Enter your choice (1-7): ").strip()

                if choice == '1':
                    self._handle_add_menu()
                elif choice == '2':
                    self._handle_view_menu()
                elif choice == '3':
                    self._handle_update_menu()
                elif choice == '4':
                    self._handle_complete_menu()
                elif choice == '5':
                    self._handle_incomplete_menu()
                elif choice == '6':
                    self._handle_delete_menu()
                elif choice == '7':
                    self.clear_screen()
                    print("\n" + "=" * 60)
                    print("         Thank you for using Todo App!")
                    print("=" * 60)
                    break
                else:
                    print("\n[!] Invalid choice! Please enter a number between 1-7.")
                    input("\nPress Enter to continue...")

            except KeyboardInterrupt:
                self.clear_screen()
                print("\n\n" + "=" * 60)
                print("         Thank you for using Todo App!")
                print("=" * 60)
                break
            except EOFError:
                self.clear_screen()
                print("\n\n" + "=" * 60)
                print("         Thank you for using Todo App!")
                print("=" * 60)
                break

    def _handle_add_menu(self):
        """Handle adding a new todo through menu."""
        print("\n" + "=" * 60)
        print("                  ADD NEW TODO")
        print("=" * 60)

        description = input("\n>> Enter todo description: ").strip()

        if not description:
            print("\n[!] Error: Description cannot be empty!")
            input("\nPress Enter to continue...")
            return

        try:
            todo_id = self.service.add_todo(description)
            print(f"\n[+] Success! Todo added with ID: {todo_id}")
            print(f"    Description: {description}")
            input("\nPress Enter to continue...")
        except ValueError as e:
            print(f"\n[!] Error: {e}")
            input("\nPress Enter to continue...")

    def _handle_view_menu(self):
        """Handle viewing all todos through menu."""
        print("\n" + "=" * 60)
        print("                  VIEW ALL TODOS")
        print("=" * 60)

        todos = self.service.get_all_todos()

        if not todos:
            print("\n[i] Your todo list is empty!")
            print("    Add some todos to get started.")
        else:
            print(f"\n>> Total todos: {len(todos)}")
            print("-" * 60)
            for todo in todos:
                status_icon = "[X]" if todo['completed'] else "[ ]"
                status_text = "Complete" if todo['completed'] else "Incomplete"
                print(f"\n   {status_icon} ID: {todo['id']}")
                print(f"       Description: {todo['description']}")
                print(f"       Status: {status_text}")
                print(f"       Created: {todo['created_at'].strftime('%Y-%m-%d %H:%M:%S')}")

        print("\n" + "-" * 60)
        input("\nPress Enter to continue...")

    def _handle_update_menu(self):
        """Handle updating a todo through menu."""
        todos = self.service.get_all_todos()

        if not todos:
            print("\n[!] No todos available to update!")
            input("\nPress Enter to continue...")
            return

        print("\n" + "=" * 60)
        print("                  UPDATE TODO")
        print("=" * 60)

        todo_id_str = input("\n>> Enter todo ID to update: ").strip()

        try:
            todo_id = int(todo_id_str)

            # Check if todo exists
            current_todo = self.service.get_todo(todo_id)
            print(f"\n>> Current description: {current_todo['description']}")

            new_description = input(">> Enter new description: ").strip()

            if not new_description:
                print("\n[!] Error: Description cannot be empty!")
                input("\nPress Enter to continue...")
                return

            self.service.update_todo(todo_id, new_description)
            print(f"\n[+] Success! Todo {todo_id} updated!")
            print(f"    New description: {new_description}")
            input("\nPress Enter to continue...")

        except ValueError:
            print("\n[!] Error: Please enter a valid number for ID!")
            input("\nPress Enter to continue...")
        except KeyError:
            print(f"\n[!] Error: No todo found with ID {todo_id_str}!")
            input("\nPress Enter to continue...")

    def _handle_complete_menu(self):
        """Handle marking a todo as complete through menu."""
        todos = self.service.get_all_todos()

        if not todos:
            print("\n[!] No todos available to mark as complete!")
            input("\nPress Enter to continue...")
            return

        print("\n" + "=" * 60)
        print("                MARK TODO AS COMPLETE")
        print("=" * 60)

        todo_id_str = input("\n>> Enter todo ID to mark as complete: ").strip()

        try:
            todo_id = int(todo_id_str)

            # Get todo before marking
            todo = self.service.get_todo(todo_id)

            if todo['completed']:
                print(f"\n[i] Todo {todo_id} is already marked as complete!")
            else:
                self.service.mark_todo_completed(todo_id)
                print(f"\n[+] Success! Todo {todo_id} marked as complete!")
                print(f"    Description: {todo['description']}")

            input("\nPress Enter to continue...")

        except ValueError:
            print("\n[!] Error: Please enter a valid number for ID!")
            input("\nPress Enter to continue...")
        except KeyError:
            print(f"\n[!] Error: No todo found with ID {todo_id_str}!")
            input("\nPress Enter to continue...")

    def _handle_incomplete_menu(self):
        """Handle marking a todo as incomplete through menu."""
        todos = self.service.get_all_todos()

        if not todos:
            print("\n[!] No todos available to mark as incomplete!")
            input("\nPress Enter to continue...")
            return

        print("\n" + "=" * 60)
        print("               MARK TODO AS INCOMPLETE")
        print("=" * 60)

        todo_id_str = input("\n>> Enter todo ID to mark as incomplete: ").strip()

        try:
            todo_id = int(todo_id_str)

            # Get todo before marking
            todo = self.service.get_todo(todo_id)

            if not todo['completed']:
                print(f"\n[i] Todo {todo_id} is already marked as incomplete!")
            else:
                self.service.mark_todo_incomplete(todo_id)
                print(f"\n[+] Success! Todo {todo_id} marked as incomplete!")
                print(f"    Description: {todo['description']}")

            input("\nPress Enter to continue...")

        except ValueError:
            print("\n[!] Error: Please enter a valid number for ID!")
            input("\nPress Enter to continue...")
        except KeyError:
            print(f"\n[!] Error: No todo found with ID {todo_id_str}!")
            input("\nPress Enter to continue...")

    def _handle_delete_menu(self):
        """Handle deleting a todo through menu."""
        todos = self.service.get_all_todos()

        if not todos:
            print("\n[!] No todos available to delete!")
            input("\nPress Enter to continue...")
            return

        print("\n" + "=" * 60)
        print("                  DELETE TODO")
        print("=" * 60)

        todo_id_str = input("\n>> Enter todo ID to delete: ").strip()

        try:
            todo_id = int(todo_id_str)

            # Get todo before deleting
            todo = self.service.get_todo(todo_id)
            print(f"\n>> Todo to delete: {todo['description']}")

            confirm = input("[!] Are you sure? (yes/no): ").strip().lower()

            if confirm in ['yes', 'y']:
                self.service.delete_todo(todo_id)
                print(f"\n[+] Success! Todo {todo_id} deleted!")
            else:
                print("\n[-] Deletion cancelled.")

            input("\nPress Enter to continue...")

        except ValueError:
            print("\n[!] Error: Please enter a valid number for ID!")
            input("\nPress Enter to continue...")
        except KeyError:
            print(f"\n[!] Error: No todo found with ID {todo_id_str}!")
            input("\nPress Enter to continue...")

    def _parse_args(self, arg_str: str) -> List[str]:
        """
        Parse command arguments, respecting quoted strings.

        Args:
            arg_str: Raw argument string

        Returns:
            List of parsed arguments
        """
        args = []
        current_arg = ""
        in_quotes = False
        quote_char = None

        i = 0
        while i < len(arg_str):
            char = arg_str[i]

            if char in ['"', "'"] and not in_quotes:
                in_quotes = True
                quote_char = char
            elif char == quote_char and in_quotes:
                in_quotes = False
                quote_char = None
            elif char == ' ' and not in_quotes:
                if current_arg:
                    args.append(current_arg)
                    current_arg = ""
            else:
                current_arg += char

            i += 1

        if current_arg:
            args.append(current_arg)

        return args

    def _handle_add(self, args: List[str]) -> None:
        """Handle the add command."""
        if not args:
            print("Usage: add \"description text\"")
            return

        description = args[0]
        try:
            id = self.service.add_todo(description)
            print(f"Added todo: {id} - {description} (Incomplete)")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_view(self, args: List[str]) -> None:
        """Handle the view command."""
        todos = self.service.get_all_todos()

        if not todos:
            print("No todos found.")
            return

        print("Todos:")
        for todo in todos:
            status = "Complete" if todo['completed'] else "Incomplete"
            print(f"{todo['id']} - {todo['description']} ({status})")

    def _handle_update(self, args: List[str]) -> None:
        """Handle the update command."""
        if len(args) < 2:
            print("Usage: update <id> \"new description\"")
            return

        try:
            id = int(args[0])
            new_description = args[1]

            success = self.service.update_todo(id, new_description)
            if success:
                todo = self.service.get_todo(id)
                status = "Complete" if todo['completed'] else "Incomplete"
                print(f"Updated todo: {id} - {new_description} ({status})")
            else:
                print(f"Failed to update todo with ID {id}")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyError:
            print(f"Error: No todo found with ID {id}")

    def _handle_delete(self, args: List[str]) -> None:
        """Handle the delete command."""
        if len(args) < 1:
            print("Usage: delete <id>")
            return

        try:
            id = int(args[0])

            success = self.service.delete_todo(id)
            if success:
                print(f"Deleted todo: {self._get_todo_description_by_id(id)}")
            else:
                print(f"Failed to delete todo with ID {id}")
        except ValueError:
            print("Error: ID must be a number")
        except KeyError:
            print(f"Error: No todo found with ID {id}")

    def _handle_complete(self, args: List[str]) -> None:
        """Handle the complete command."""
        if len(args) < 1:
            print("Usage: complete <id>")
            return

        try:
            id = int(args[0])

            success = self.service.mark_todo_completed(id)
            if success:
                todo = self.service.get_todo(id)
                print(f"Todo {id} marked as complete: {todo['description']}")
            else:
                print(f"Failed to mark todo with ID {id} as complete")
        except ValueError:
            print("Error: ID must be a number")
        except KeyError:
            print(f"Error: No todo found with ID {id}")

    def _handle_incomplete(self, args: List[str]) -> None:
        """Handle the incomplete command."""
        if len(args) < 1:
            print("Usage: incomplete <id>")
            return

        try:
            id = int(args[0])

            success = self.service.mark_todo_incomplete(id)
            if success:
                todo = self.service.get_todo(id)
                print(f"Todo {id} marked as incomplete: {todo['description']}")
            else:
                print(f"Failed to mark todo with ID {id} as incomplete")
        except ValueError:
            print("Error: ID must be a number")
        except KeyError:
            print(f"Error: No todo found with ID {id}")

    def _handle_help(self, args: List[str]) -> None:
        """Handle the help command."""
        print("\nAvailable commands:")
        print("  add \"description\"     - Add a new todo")
        print("  view                 - View all todos")
        print("  update <id> \"desc\"   - Update a todo's description")
        print("  delete <id>          - Delete a todo")
        print("  complete <id>        - Mark a todo as complete")
        print("  incomplete <id>      - Mark a todo as incomplete")
        print("  help                 - Show this help message")
        print("  exit/quit            - Exit the application")

    def _handle_exit(self, args: List[str]) -> bool:
        """Handle the exit command."""
        print("Goodbye!")
        return False

    def _get_todo_description_by_id(self, id: int) -> str:
        """Helper method to get todo description by ID."""
        try:
            todo = self.service.get_todo(id)
            return todo['description']
        except KeyError:
            return f"(ID {id})"