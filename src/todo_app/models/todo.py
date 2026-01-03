"""
Todo Data Model

This module defines the Todo data structure based on the data-model.md specification.
Each Todo item contains a unique identifier, task description, and completion status.
"""

from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class Todo:
    """
    Represents a single todo item with an ID, description, and completion status.

    Attributes:
        id (int): Unique identifier for the todo item
        description (str): The task description provided by the user
        completed (bool): Status indicating whether the task is completed (default: False)
    """
    id: int
    description: str
    completed: bool = False

    def __str__(self) -> str:
        """
        String representation of the Todo item.

        Returns:
            str: Formatted string showing the todo's ID, description, and status
        """
        status = "Completed" if self.completed else "Pending"
        return f"{self.id:3d} | {self.description:<30} | {status}"

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Todo object to a dictionary representation.

        Returns:
            Dict[str, Any]: Dictionary with id, description, and completed status
        """
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Todo':
        """
        Create a Todo object from a dictionary representation.

        Args:
            data (Dict[str, Any]): Dictionary with id, description, and completed status

        Returns:
            Todo: New Todo instance created from the data
        """
        return cls(
            id=data["id"],
            description=data["description"],
            completed=data.get("completed", False)
        )