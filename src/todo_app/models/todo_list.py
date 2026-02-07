"""
TodoList model representing a collection of todo items
"""
from typing import List, Optional
from .todo_item import TodoItem


class TodoList:
    """Represents a collection of TodoItems with operations to manage them."""

    def __init__(self):
        """Initialize an empty TodoList with next_id counter."""
        self.items: List[TodoItem] = []
        self.next_id = 1

    def add_item(self, description: str) -> TodoItem:
        """
        Add a new todo item to the list.

        Args:
            description: Description text for the new todo item

        Returns:
            Created TodoItem with unique ID
        """
        if not description or description.strip() == "":
            raise ValueError("Description cannot be empty or whitespace only")

        item = TodoItem(id=self.next_id, description=description)
        self.items.append(item)
        self.next_id += 1
        return item

    def get_all_items(self) -> List[TodoItem]:
        """
        Get all items in the list.

        Returns:
            List of all TodoItems
        """
        return self.items.copy()

    def get_item(self, id: int) -> TodoItem:
        """
        Get a specific item by ID.

        Args:
            id: ID of the todo item to retrieve

        Returns:
            TodoItem with the specified ID

        Raises:
            KeyError: If no item exists with the given ID
        """
        for item in self.items:
            if item.id == id:
                return item
        raise KeyError(f"No todo item found with ID {id}")

    def update_item(self, id: int, new_description: str) -> bool:
        """
        Update the description of an existing item.

        Args:
            id: ID of the item to update
            new_description: New description text

        Returns:
            True if the update was successful

        Raises:
            KeyError: If no item exists with the given ID
            ValueError: If new_description is empty
        """
        if not new_description or new_description.strip() == "":
            raise ValueError("Description cannot be empty or whitespace only")

        for item in self.items:
            if item.id == id:
                item.description = new_description.strip()
                return True
        raise KeyError(f"No todo item found with ID {id}")

    def delete_item(self, id: int) -> bool:
        """
        Remove an item from the list.

        Args:
            id: ID of the item to delete

        Returns:
            True if the deletion was successful

        Raises:
            KeyError: If no item exists with the given ID
        """
        for i, item in enumerate(self.items):
            if item.id == id:
                del self.items[i]
                return True
        raise KeyError(f"No todo item found with ID {id}")

    def mark_complete(self, id: int) -> bool:
        """
        Mark an item as complete.

        Args:
            id: ID of the item to mark complete

        Returns:
            True if the operation was successful

        Raises:
            KeyError: If no item exists with the given ID
        """
        item = self.get_item(id)
        item.completed = True
        return True

    def mark_incomplete(self, id: int) -> bool:
        """
        Mark an item as incomplete.

        Args:
            id: ID of the item to mark incomplete

        Returns:
            True if the operation was successful

        Raises:
            KeyError: If no item exists with the given ID
        """
        item = self.get_item(id)
        item.completed = False
        return True