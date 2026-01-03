"""
Todo Service

This module provides the business logic for todo operations.
It implements the core functionality for adding, viewing, updating,
deleting, and marking todo items as completed.
"""

from typing import List, Optional
from ..models.todo import Todo
from ..services.validation import validate_todo_description


class TodoService:
    """
    Service class for managing todo items with in-memory storage.
    Provides methods for all core todo operations.
    """

    def __init__(self):
        """
        Initialize the TodoService with an empty list to store todos
        and a counter for generating unique IDs.
        """
        self.todos: List[Todo] = []
        self._next_id: int = 1

    def add_todo(self, description: str) -> Todo:
        """
        Add a new todo item with a unique ID and pending completion status.

        Args:
            description (str): The task description

        Returns:
            Todo: The newly created Todo object

        Raises:
            ValueError: If description is invalid
        """
        is_valid, error_msg = validate_todo_description(description)
        if not is_valid:
            raise ValueError(error_msg)

        todo = Todo(
            id=self._next_id,
            description=description.strip(),
            completed=False
        )
        self.todos.append(todo)
        self._next_id += 1
        return todo

    def get_all_todos(self) -> List[Todo]:
        """
        Retrieve all todo items.

        Returns:
            List[Todo]: List of all todo items
        """
        return self.todos.copy()

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Find a todo item by its ID.

        Args:
            todo_id (int): The ID of the todo to find

        Returns:
            Optional[Todo]: The found todo item or None if not found
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo(self, todo_id: int, new_description: str) -> bool:
        """
        Update the description of an existing todo item.

        Args:
            todo_id (int): The ID of the todo to update
            new_description (str): The new description

        Returns:
            bool: True if the todo was updated, False if not found

        Raises:
            ValueError: If new_description is invalid
        """
        is_valid, error_msg = validate_todo_description(new_description)
        if not is_valid:
            raise ValueError(error_msg)

        for todo in self.todos:
            if todo.id == todo_id:
                todo.description = new_description.strip()
                return True
        return False

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo item by its ID.

        Args:
            todo_id (int): The ID of the todo to delete

        Returns:
            bool: True if the todo was deleted, False if not found
        """
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                del self.todos[i]
                return True
        return False

    def mark_completed(self, todo_id: int) -> bool:
        """
        Mark a todo item as completed by its ID.

        Args:
            todo_id (int): The ID of the todo to mark as completed

        Returns:
            bool: True if the todo was marked completed, False if not found
        """
        for todo in self.todos:
            if todo.id == todo_id:
                todo.completed = True
                return True
        return False

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new todo.

        Returns:
            int: The next ID that will be used
        """
        return self._next_id