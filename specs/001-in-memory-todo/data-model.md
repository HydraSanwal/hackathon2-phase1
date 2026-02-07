# Data Model: Phase I - In-Memory Python Console Todo App

**Feature**: Phase I - In-Memory Python Console Todo App
**Date**: 2026-02-07
**Branch**: 001-in-memory-todo

## Entity: TodoItem

### Fields:
- `id`: int (unique identifier, auto-generated)
- `description`: str (task description text, non-empty)
- `completed`: bool (completion status, default False)
- `created_at`: datetime (timestamp when created, auto-generated)

### Validation Rules:
- `description` must not be empty or consist only of whitespace
- `id` must be unique within the todo list
- `completed` is a boolean value (True/False)
- `created_at` is an immutable timestamp

### State Transitions:
- New TodoItem: `completed = False`
- Mark Complete: `completed = True`
- Mark Incomplete: `completed = False`

## Entity: TodoList

### Fields:
- `items`: List[TodoItem] (collection of todo items)
- `next_id`: int (next available unique ID, auto-managed)

### Operations:
- `add_item(description: str)`: Creates new TodoItem with unique ID
- `get_all_items()`: Returns all items in the list
- `get_item(id: int)`: Returns specific item by ID or raises exception
- `update_item(id: int, new_description: str)`: Updates item description
- `delete_item(id: int)`: Removes item from list
- `mark_complete(id: int)`: Sets item's completed status to True
- `mark_incomplete(id: int)`: Sets item's completed status to False

### Validation Rules:
- IDs must be unique within the list
- Operations with invalid IDs must raise appropriate exceptions
- Descriptions must not be empty
- Item retrieval operations must validate ID existence before access

### Relationships:
- TodoList contains multiple TodoItem instances
- Each TodoItem belongs to exactly one TodoList
- TodoList manages the lifecycle of its TodoItems