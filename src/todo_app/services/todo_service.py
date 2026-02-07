"""
TodoService providing business logic for todo operations
"""
from typing import List, Dict
from ..models.todo_list import TodoList
from ..models.todo_item import TodoItem


class TodoService:
    """Provides business logic for todo operations."""

    def __init__(self):
        """Initialize the TodoService with an empty TodoList."""
        self.todo_list = TodoList()

    def add_todo(self, description: str) -> int:
        """
        Add a new todo item to the list.

        Args:
            description: Description text for the new todo

        Returns:
            ID of the created todo item

        Raises:
            ValueError: If description is empty or whitespace only
        """
        if not description or description.strip() == "":
            raise ValueError("Description cannot be empty or whitespace only")

        item = self.todo_list.add_item(description)
        return item.id

    def get_all_todos(self) -> List[Dict]:
        """
        Get all todo items as dictionaries.

        Returns:
            List of dictionaries containing id, description, completed, and created_at
        """
        items = self.todo_list.get_all_items()
        return [item.to_dict() for item in items]

    def get_todo(self, id: int) -> Dict:
        """
        Get a specific todo item by ID.

        Args:
            id: ID of the todo item to retrieve

        Returns:
            Dictionary containing id, description, completed, and created_at

        Raises:
            KeyError: If no todo exists with the given ID
        """
        item = self.todo_list.get_item(id)
        return item.to_dict()

    def update_todo(self, id: int, new_description: str) -> bool:
        """
        Update the description of an existing todo.

        Args:
            id: ID of the todo to update
            new_description: New description text

        Returns:
            True if the update was successful

        Raises:
            KeyError: If no todo exists with the given ID
            ValueError: If new_description is empty
        """
        return self.todo_list.update_item(id, new_description)

    def delete_todo(self, id: int) -> bool:
        """
        Remove a todo item from the list.

        Args:
            id: ID of the todo to delete

        Returns:
            True if the deletion was successful

        Raises:
            KeyError: If no todo exists with the given ID
        """
        return self.todo_list.delete_item(id)

    def mark_todo_completed(self, id: int) -> bool:
        """
        Mark a todo as completed.

        Args:
            id: ID of the todo to mark complete

        Returns:
            True if the operation was successful

        Raises:
            KeyError: If no todo exists with the given ID
        """
        return self.todo_list.mark_complete(id)

    def mark_todo_incomplete(self, id: int) -> bool:
        """
        Mark a todo as incomplete.

        Args:
            id: ID of the todo to mark incomplete

        Returns:
            True if the operation was successful

        Raises:
            KeyError: If no todo exists with the given ID
        """
        return self.todo_list.mark_incomplete(id)