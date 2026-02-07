"""
Unit tests for TodoService
"""
import pytest
from src.todo_app.services.todo_service import TodoService
from src.todo_app.models.todo_item import TodoItem


class TestTodoService:
    """Test suite for TodoService functionality."""

    def test_add_todo_success(self):
        """Test adding a new todo successfully."""
        service = TodoService()

        # Add a new todo
        id = service.add_todo("Test description")

        # Verify the ID is assigned correctly
        assert id == 1

        # Verify the todo exists
        todos = service.get_all_todos()
        assert len(todos) == 1
        assert todos[0]['id'] == 1
        assert todos[0]['description'] == "Test description"
        assert todos[0]['completed'] is False

    def test_add_todo_empty_description_fails(self):
        """Test that adding a todo with empty description raises ValueError."""
        service = TodoService()

        with pytest.raises(ValueError, match="Description cannot be empty"):
            service.add_todo("")

    def test_add_todo_whitespace_only_fails(self):
        """Test that adding a todo with whitespace-only description raises ValueError."""
        service = TodoService()

        with pytest.raises(ValueError, match="Description cannot be empty"):
            service.add_todo("   ")

    def test_get_all_todos_empty(self):
        """Test getting all todos when list is empty."""
        service = TodoService()

        todos = service.get_all_todos()
        assert len(todos) == 0

    def test_get_todo_success(self):
        """Test getting a specific todo by ID."""
        service = TodoService()
        added_id = service.add_todo("Test todo")

        todo = service.get_todo(added_id)
        assert todo['id'] == added_id
        assert todo['description'] == "Test todo"
        assert todo['completed'] is False

    def test_get_todo_nonexistent_fails(self):
        """Test that getting a non-existent todo raises KeyError."""
        service = TodoService()

        with pytest.raises(KeyError):
            service.get_todo(999)

    def test_update_todo_success(self):
        """Test updating a todo's description."""
        service = TodoService()
        id = service.add_todo("Original description")

        success = service.update_todo(id, "Updated description")
        assert success is True

        # Verify the update
        updated_todo = service.get_todo(id)
        assert updated_todo['description'] == "Updated description"

    def test_update_todo_empty_description_fails(self):
        """Test that updating to empty description raises ValueError."""
        service = TodoService()
        id = service.add_todo("Original description")

        with pytest.raises(ValueError, match="Description cannot be empty"):
            service.update_todo(id, "")

    def test_update_todo_nonexistent_fails(self):
        """Test that updating non-existent todo raises KeyError."""
        service = TodoService()

        with pytest.raises(KeyError):
            service.update_todo(999, "New description")

    def test_delete_todo_success(self):
        """Test deleting a todo."""
        service = TodoService()
        id = service.add_todo("Test todo to delete")

        success = service.delete_todo(id)
        assert success is True

        # Verify it's deleted
        todos = service.get_all_todos()
        assert len(todos) == 0

        # Verify getting it raises error
        with pytest.raises(KeyError):
            service.get_todo(id)

    def test_delete_todo_nonexistent_fails(self):
        """Test that deleting non-existent todo raises KeyError."""
        service = TodoService()

        with pytest.raises(KeyError):
            service.delete_todo(999)

    def test_mark_todo_completed(self):
        """Test marking a todo as completed."""
        service = TodoService()
        id = service.add_todo("Test todo")

        # Verify initial state
        todo = service.get_todo(id)
        assert todo['completed'] is False

        # Mark as completed
        success = service.mark_todo_completed(id)
        assert success is True

        # Verify completion
        todo = service.get_todo(id)
        assert todo['completed'] is True

    def test_mark_todo_incomplete(self):
        """Test marking a todo as incomplete."""
        service = TodoService()
        id = service.add_todo("Test todo")

        # Mark as completed first
        service.mark_todo_completed(id)
        todo = service.get_todo(id)
        assert todo['completed'] is True

        # Mark as incomplete
        success = service.mark_todo_incomplete(id)
        assert success is True

        # Verify incompletion
        todo = service.get_todo(id)
        assert todo['completed'] is False

    def test_multiple_todos_different_ids(self):
        """Test that multiple todos get different IDs."""
        service = TodoService()

        id1 = service.add_todo("First todo")
        id2 = service.add_todo("Second todo")
        id3 = service.add_todo("Third todo")

        assert id1 == 1
        assert id2 == 2
        assert id3 == 3

        todos = service.get_all_todos()
        assert len(todos) == 3