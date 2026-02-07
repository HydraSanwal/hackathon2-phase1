"""
TodoItem model representing a single todo item
"""
from datetime import datetime
from typing import Dict


class TodoItem:
    """Represents a single todo item with id, description, completion status, and creation timestamp."""

    def __init__(self, id: int, description: str, completed: bool = False):
        """
        Initialize a TodoItem.

        Args:
            id: Unique identifier for the todo item
            description: Description text of the todo
            completed: Whether the todo is completed (default: False)
        """
        if not description or description.strip() == "":
            raise ValueError("Description cannot be empty or whitespace only")

        self.id = id
        self.description = description.strip()
        self.completed = completed
        self.created_at = datetime.now()

    def to_dict(self) -> Dict:
        """
        Convert the TodoItem to a dictionary representation.

        Returns:
            Dictionary with id, description, completed, and created_at
        """
        return {
            'id': self.id,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at
        }

    def __str__(self) -> str:
        """String representation of the TodoItem."""
        status = "Complete" if self.completed else "Incomplete"
        return f"{self.id} - {self.description} ({status})"

    def __repr__(self) -> str:
        """Detailed string representation of the TodoItem."""
        return f"TodoItem(id={self.id}, description='{self.description}', completed={self.completed})"