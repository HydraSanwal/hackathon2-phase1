"""
Unit tests for TodoItem
"""
import pytest
from src.todo_app.models.todo_item import TodoItem
from datetime import datetime


class TestTodoItem:
    """Test suite for TodoItem functionality."""

    def test_create_todo_item_success(self):
        """Test creating a TodoItem successfully."""
        item = TodoItem(id=1, description="Test description")

        assert item.id == 1
        assert item.description == "Test description"
        assert item.completed is False
        assert isinstance(item.created_at, datetime)

    def test_create_todo_item_with_completion_status(self):
        """Test creating a TodoItem with completion status."""
        item = TodoItem(id=1, description="Test description", completed=True)

        assert item.id == 1
        assert item.description == "Test description"
        assert item.completed is True
        assert isinstance(item.created_at, datetime)

    def test_create_todo_item_empty_description_fails(self):
        """Test that creating a TodoItem with empty description raises ValueError."""
        with pytest.raises(ValueError, match="Description cannot be empty"):
            TodoItem(id=1, description="")

    def test_create_todo_item_whitespace_only_description_fails(self):
        """Test that creating a TodoItem with whitespace-only description raises ValueError."""
        with pytest.raises(ValueError, match="Description cannot be empty"):
            TodoItem(id=1, description="   ")

    def test_create_todo_item_tabs_newlines_whitespace_fails(self):
        """Test that creating a TodoItem with tabs/newlines whitespace fails."""
        with pytest.raises(ValueError, match="Description cannot be empty"):
            TodoItem(id=1, description=" \t \n ")

    def test_to_dict_method(self):
        """Test converting TodoItem to dictionary."""
        item = TodoItem(id=1, description="Test description")

        dict_repr = item.to_dict()

        assert dict_repr['id'] == 1
        assert dict_repr['description'] == "Test description"
        assert dict_repr['completed'] is False
        assert dict_repr['created_at'] == item.created_at

    def test_string_representation(self):
        """Test the string representation of TodoItem."""
        item = TodoItem(id=1, description="Test description")

        str_repr = str(item)
        assert "1 - Test description (Incomplete)" in str_repr

        # Test with completed status
        completed_item = TodoItem(id=1, description="Test description", completed=True)
        str_repr_completed = str(completed_item)
        assert "1 - Test description (Complete)" in str_repr_completed

    def test_repr_method(self):
        """Test the repr representation of TodoItem."""
        item = TodoItem(id=1, description="Test description", completed=True)

        repr_str = repr(item)
        assert "TodoItem(id=1, description='Test description', completed=True)" in repr_str

    def test_description_stripped_of_whitespace(self):
        """Test that descriptions are stripped of leading/trailing whitespace."""
        item = TodoItem(id=1, description="  description with spaces  ")

        assert item.description == "description with spaces"