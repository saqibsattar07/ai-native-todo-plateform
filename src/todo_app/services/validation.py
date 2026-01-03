"""
Input Validation Module

This module provides validation functions for the Todo application.
It includes functions to validate user input before processing.
"""

from typing import Optional


def validate_todo_description(description: str) -> tuple[bool, Optional[str]]:
    """
    Validate a todo description.

    Args:
        description (str): The description to validate

    Returns:
        tuple[bool, Optional[str]]: A tuple containing a boolean indicating
        if the description is valid and an optional error message
    """
    if not description or not description.strip():
        return False, "Todo description cannot be empty"

    if len(description.strip()) > 255:
        return False, "Todo description cannot exceed 255 characters"

    return True, None


def validate_todo_id(todo_id: int) -> tuple[bool, Optional[str]]:
    """
    Validate a todo ID.

    Args:
        todo_id (int): The ID to validate

    Returns:
        tuple[bool, Optional[str]]: A tuple containing a boolean indicating
        if the ID is valid and an optional error message
    """
    if not isinstance(todo_id, int):
        return False, "Todo ID must be an integer"

    if todo_id <= 0:
        return False, "Todo ID must be a positive integer"

    return True, None


def validate_todo_update(todo_id: int, new_description: str) -> tuple[bool, Optional[str]]:
    """
    Validate todo update parameters.

    Args:
        todo_id (int): The ID of the todo to update
        new_description (str): The new description

    Returns:
        tuple[bool, Optional[str]]: A tuple containing a boolean indicating
        if the parameters are valid and an optional error message
    """
    # Validate the ID
    is_id_valid, id_error = validate_todo_id(todo_id)
    if not is_id_valid:
        return False, id_error

    # Validate the description
    is_desc_valid, desc_error = validate_todo_description(new_description)
    if not is_desc_valid:
        return False, desc_error

    return True, None


def validate_add_todo(description: str) -> tuple[bool, Optional[str]]:
    """
    Validate parameters for adding a new todo.

    Args:
        description (str): The description of the new todo

    Returns:
        tuple[bool, Optional[str]]: A tuple containing a boolean indicating
        if the parameters are valid and an optional error message
    """
    return validate_todo_description(description)


def validate_todo_exists(todo_id: int, service) -> tuple[bool, Optional[str]]:
    """
    Validate that a todo with the given ID exists.

    Args:
        todo_id (int): The ID of the todo to check
        service: The TodoService instance to check against

    Returns:
        tuple[bool, Optional[str]]: A tuple containing a boolean indicating
        if the todo exists and an optional error message
    """
    todo = service.get_todo_by_id(todo_id)
    if todo is None:
        return False, f"Todo with ID {todo_id} does not exist"

    return True, None