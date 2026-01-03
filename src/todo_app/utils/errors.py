"""
Error Handling Utilities

This module provides custom exception classes and error handling utilities
for the Todo application.
"""


class TodoError(Exception):
    """
    Base exception class for todo-related errors.
    """
    pass


class TodoNotFoundError(TodoError):
    """
    Exception raised when a todo item is not found.
    """
    def __init__(self, todo_id: int):
        self.todo_id = todo_id
        super().__init__(f"Todo with ID {todo_id} not found")


class InvalidTodoDescriptionError(TodoError):
    """
    Exception raised when a todo description is invalid.
    """
    def __init__(self, message: str = "Invalid todo description"):
        super().__init__(message)


class InvalidTodoIdError(TodoError):
    """
    Exception raised when a todo ID is invalid.
    """
    def __init__(self, message: str = "Invalid todo ID"):
        super().__init__(message)


def format_error_message(error: Exception) -> str:
    """
    Format an error message for display to the user.

    Args:
        error (Exception): The error to format

    Returns:
        str: A user-friendly error message
    """
    if isinstance(error, TodoNotFoundError):
        return str(error)
    elif isinstance(error, InvalidTodoDescriptionError):
        return f"Description Error: {error}"
    elif isinstance(error, InvalidTodoIdError):
        return f"ID Error: {error}"
    else:
        return f"An unexpected error occurred: {error}"


def handle_error(error: Exception, default_message: str = "An error occurred") -> str:
    """
    Handle an error and return an appropriate message.

    Args:
        error (Exception): The error to handle
        default_message (str): Default message if error type is not recognized

    Returns:
        str: A user-friendly error message
    """
    try:
        return format_error_message(error)
    except Exception:
        return default_message


def handle_empty_description_error() -> str:
    """
    Handle the specific case of an empty description error.

    Returns:
        str: A user-friendly error message for empty descriptions
    """
    return "Error: Todo description cannot be empty. Please provide a valid description."


def handle_nonexistent_todo_error(todo_id: int) -> str:
    """
    Handle the specific case of a non-existent todo error.

    Args:
        todo_id (int): The ID of the todo that doesn't exist

    Returns:
        str: A user-friendly error message for non-existent todos
    """
    return f"Error: Todo with ID {todo_id} does not exist. Please enter a valid todo ID."


def handle_invalid_input_error(input_type: str = "input") -> str:
    """
    Handle the specific case of invalid input error.

    Args:
        input_type (str): The type of input that is invalid

    Returns:
        str: A user-friendly error message for invalid inputs
    """
    return f"Error: Invalid {input_type} provided. Please enter a valid value."