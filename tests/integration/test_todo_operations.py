"""
Integration tests for todo operations
"""
import pytest
from src.todo_app.services.todo_service import TodoService
from src.todo_app.cli.todo_cli import TodoCLI
from io import StringIO
import sys


class TestTodoOperationsIntegration:
    """Test suite for integration of todo operations."""

    def test_add_and_view_workflow(self):
        """Test adding todos and viewing them."""
        service = TodoService()

        # Add some todos
        id1 = service.add_todo("First todo")
        id2 = service.add_todo("Second todo")

        # Get all todos
        todos = service.get_all_todos()

        # Verify we have both todos
        assert len(todos) == 2
        todo_ids = [todo['id'] for todo in todos]
        assert id1 in todo_ids
        assert id2 in todo_ids

        # Verify descriptions are correct
        descriptions = [todo['description'] for todo in todos]
        assert "First todo" in descriptions
        assert "Second todo" in descriptions

    def test_add_update_view_workflow(self):
        """Test adding, updating, and viewing a todo."""
        service = TodoService()

        # Add a todo
        id = service.add_todo("Original description")

        # Update it
        service.update_todo(id, "Updated description")

        # Get all todos
        todos = service.get_all_todos()
        assert len(todos) == 1
        assert todos[0]['id'] == id
        assert todos[0]['description'] == "Updated description"

    def test_add_complete_view_workflow(self):
        """Test adding, completing, and viewing a todo."""
        service = TodoService()

        # Add a todo
        id = service.add_todo("Test todo")

        # Verify it's initially incomplete
        todo = service.get_todo(id)
        assert todo['completed'] is False

        # Mark it as complete
        service.mark_todo_completed(id)

        # Verify it's complete
        todo = service.get_todo(id)
        assert todo['completed'] is True

    def test_add_delete_view_workflow(self):
        """Test adding, deleting, and attempting to view a deleted todo."""
        service = TodoService()

        # Add a todo
        id = service.add_todo("Test todo to delete")

        # Verify it exists
        todo = service.get_todo(id)
        assert todo['description'] == "Test todo to delete"

        # Delete it
        result = service.delete_todo(id)
        assert result is True

        # Verify it no longer exists
        with pytest.raises(KeyError):
            service.get_todo(id)

    def test_multiple_operations_workflow(self):
        """Test a sequence of different operations."""
        service = TodoService()

        # Add several todos
        id1 = service.add_todo("First todo")
        id2 = service.add_todo("Second todo")
        id3 = service.add_todo("Third todo")

        # Initially all should be incomplete
        todos = service.get_all_todos()
        assert len(todos) == 3
        for todo in todos:
            assert todo['completed'] is False

        # Mark one as complete
        service.mark_todo_completed(id2)

        # Update one description
        service.update_todo(id1, "Updated first todo")

        # Get all and verify changes
        todos = service.get_all_todos()
        assert len(todos) == 3

        # Find the updated item
        updated_item = next(todo for todo in todos if todo['id'] == id1)
        assert updated_item['description'] == "Updated first todo"

        # Find the completed item
        completed_item = next(todo for todo in todos if todo['id'] == id2)
        assert completed_item['completed'] is True

        # Delete one
        service.delete_todo(id3)

        # Verify only 2 remain
        todos = service.get_all_todos()
        assert len(todos) == 2
        todo_ids = [todo['id'] for todo in todos]
        assert id3 not in todo_ids
        assert id1 in todo_ids
        assert id2 in todo_ids