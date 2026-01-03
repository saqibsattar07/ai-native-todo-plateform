"""
Todo Console Application - CLI Interface

This module provides the command-line interface for the Todo application.
It implements a menu-driven system for users to interact with their todo items.
"""

from typing import Optional
import sys
from ..services.todo_service import TodoService
from ..models.todo import Todo
from ..services.validation import validate_add_todo, validate_todo_exists
from ..utils.errors import handle_empty_description_error, handle_nonexistent_todo_error


class TodoCLI:
    """
    Command-line interface class for the Todo application.
    Provides methods for displaying menus and handling user input.
    """

    def __init__(self):
        """
        Initialize the CLI with a TodoService instance.
        """
        self.service = TodoService()

    def display_menu(self) -> None:
        """
        Display the main menu options to the user.
        """
        print("\n" + "="*50)
        print("TODO CONSOLE APPLICATION")
        print("="*50)
        print("1. Add a new todo")
        print("2. View all todos")
        print("3. Mark a todo as completed")
        print("4. Update a todo description")
        print("5. Delete a todo")
        print("6. Exit")
        print("="*50)

    def get_user_choice(self) -> str:
        """
        Get and validate user menu choice.

        Returns:
            str: The user's menu choice
        """
        while True:
            try:
                choice = input("Enter your choice (1-6): ").strip()
                if choice in ['1', '2', '3', '4', '5', '6']:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            except (EOFError, KeyboardInterrupt):
                print("\nExiting application...")
                sys.exit(0)

    def handle_add_todo(self) -> None:
        """
        Handle the add todo functionality.
        """
        try:
            description = input("Enter todo description: ").strip()

            # Validate the description
            is_valid, error_msg = validate_add_todo(description)
            if not is_valid:
                print(handle_empty_description_error())
                return

            todo = self.service.add_todo(description)
            print(f"Successfully added todo: {todo}")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_view_todos(self) -> None:
        """
        Handle the view todos functionality.
        """
        todos = self.service.get_all_todos()

        if not todos:
            print("\nNo todos found.")
            return

        print("\n" + "-"*50)
        print(f"{'ID':<5} | {'Description':<30} | {'Status':<10}")
        print("-"*50)

        for todo in todos:
            status = "Completed" if todo.completed else "Pending"
            print(f"{todo.id:<5} | {todo.description:<30} | {status:<10}")

        print("-"*50)
        print(f"Total todos: {len(todos)}")

    def handle_mark_completed(self) -> None:
        """
        Handle marking a todo as completed.
        """
        try:
            self.handle_view_todos()
            if not self.service.get_all_todos():
                return

            todo_id_str = input("Enter the ID of the todo to mark as completed: ").strip()
            todo_id = int(todo_id_str)

            # Validate that the todo exists
            is_valid, error_msg = validate_todo_exists(todo_id, self.service)
            if not is_valid:
                print(handle_nonexistent_todo_error(todo_id))
                return

            if self.service.mark_completed(todo_id):
                print(f"Todo {todo_id} marked as completed.")
            else:
                print(f"Error: Todo with ID {todo_id} not found.")
        except ValueError:
            print("Error: Please enter a valid number for the todo ID.")

    def handle_update_todo(self) -> None:
        """
        Handle updating a todo description.
        """
        try:
            self.handle_view_todos()
            if not self.service.get_all_todos():
                return

            todo_id_str = input("Enter the ID of the todo to update: ").strip()
            todo_id = int(todo_id_str)

            # Validate that the todo exists
            is_valid, error_msg = validate_todo_exists(todo_id, self.service)
            if not is_valid:
                print(handle_nonexistent_todo_error(todo_id))
                return

            new_description = input("Enter the new description: ").strip()

            # Validate the new description
            is_desc_valid, desc_error = validate_todo_description(new_description)
            if not is_desc_valid:
                print(handle_empty_description_error())
                return

            if self.service.update_todo(todo_id, new_description):
                updated_todo = self.service.get_todo_by_id(todo_id)
                if updated_todo:
                    print(f"Todo {todo_id} updated: {updated_todo}")
            else:
                print(f"Error: Todo with ID {todo_id} not found.")
        except ValueError as e:
            if "invalid literal" in str(e):
                print("Error: Please enter a valid number for the todo ID.")
            else:
                print(f"Error: {e}")

    def handle_delete_todo(self) -> None:
        """
        Handle deleting a todo.
        """
        try:
            self.handle_view_todos()
            if not self.service.get_all_todos():
                return

            todo_id_str = input("Enter the ID of the todo to delete: ").strip()
            todo_id = int(todo_id_str)

            # Validate that the todo exists
            is_valid, error_msg = validate_todo_exists(todo_id, self.service)
            if not is_valid:
                print(handle_nonexistent_todo_error(todo_id))
                return

            if self.service.delete_todo(todo_id):
                print(f"Todo {todo_id} deleted successfully.")
            else:
                print(f"Error: Todo with ID {todo_id} not found.")
        except ValueError:
            print("Error: Please enter a valid number for the todo ID.")

    def run(self) -> None:
        """
        Run the main application loop.
        """
        print("Welcome to the Todo Console Application!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == '1':
                self.handle_add_todo()
            elif choice == '2':
                self.handle_view_todos()
            elif choice == '3':
                self.handle_mark_completed()
            elif choice == '4':
                self.handle_update_todo()
            elif choice == '5':
                self.handle_delete_todo()
            elif choice == '6':
                print("Thank you for using the Todo Console Application. Goodbye!")
                sys.exit(0)


def main() -> None:
    """
    Main entry point for the CLI application.
    """
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()