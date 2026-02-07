# API Contracts: Phase I - In-Memory Python Console Todo App

**Feature**: Phase I - In-Memory Python Console Todo App
**Date**: 2026-02-07
**Branch**: 001-in-memory-todo

## Service Contracts

### TodoService Interface

#### add_todo(description: str) -> int
- **Purpose**: Add a new todo item to the list
- **Input**: description (str) - non-empty description text
- **Output**: id (int) - unique identifier for the created todo
- **Validation**:
  - description must not be empty or whitespace only
- **Errors**:
  - ValueError if description is empty
- **Side Effects**: Creates new TodoItem with unique ID

#### get_all_todos() -> List[Dict]
- **Purpose**: Retrieve all todo items
- **Input**: None
- **Output**: List of dictionaries containing id, description, completed, created_at
- **Validation**: None
- **Errors**: None
- **Side Effects**: None

#### get_todo(id: int) -> Dict
- **Purpose**: Retrieve a specific todo item by ID
- **Input**: id (int) - unique identifier
- **Output**: Dictionary containing id, description, completed, created_at
- **Validation**: ID must exist in the list
- **Errors**:
  - KeyError if ID does not exist
- **Side Effects**: None

#### update_todo(id: int, new_description: str) -> bool
- **Purpose**: Update the description of an existing todo
- **Input**: id (int) - unique identifier, new_description (str) - non-empty description
- **Output**: bool - True if successful
- **Validation**:
  - ID must exist in the list
  - new_description must not be empty
- **Errors**:
  - KeyError if ID does not exist
  - ValueError if new_description is empty
- **Side Effects**: Modifies existing TodoItem's description

#### delete_todo(id: int) -> bool
- **Purpose**: Remove a todo item from the list
- **Input**: id (int) - unique identifier
- **Output**: bool - True if successful
- **Validation**: ID must exist in the list
- **Errors**:
  - KeyError if ID does not exist
- **Side Effects**: Removes TodoItem from collection

#### mark_todo_completed(id: int) -> bool
- **Purpose**: Mark a todo as completed
- **Input**: id (int) - unique identifier
- **Output**: bool - True if successful
- **Validation**: ID must exist in the list
- **Errors**:
  - KeyError if ID does not exist
- **Side Effects**: Sets TodoItem.completed to True

#### mark_todo_incomplete(id: int) -> bool
- **Purpose**: Mark a todo as incomplete
- **Input**: id (int) - unique identifier
- **Output**: bool - True if successful
- **Validation**: ID must exist in the list
- **Errors**:
  - KeyError if ID does not exist
- **Side Effects**: Sets TodoItem.completed to False

## CLI Command Contracts

### CLI Commands

#### `add "description text"`
- **Purpose**: Add a new todo with the given description
- **Arguments**: Description text (string, enclosed in quotes if multiple words)
- **Output**: Confirmation message with the created todo's ID and details
- **Validation**: Description must not be empty
- **Error Handling**: Shows error message if validation fails

#### `view`
- **Purpose**: Display all todos with their status
- **Arguments**: None
- **Output**: Formatted list of all todos showing ID, description, and completion status
- **Validation**: None
- **Error Handling**: Shows appropriate message if no todos exist

#### `update <id> "new description"`
- **Purpose**: Update the description of an existing todo
- **Arguments**:
  - id (integer): unique identifier
  - new description (string, in quotes if multiple words)
- **Output**: Confirmation message showing updated todo details
- **Validation**:
  - ID must exist
  - Description must not be empty
- **Error Handling**: Shows error message if validation fails

#### `delete <id>`
- **Purpose**: Remove a todo from the list
- **Arguments**: id (integer): unique identifier
- **Output**: Confirmation message of deletion
- **Validation**: ID must exist
- **Error Handling**: Shows error message if ID does not exist

#### `complete <id>`
- **Purpose**: Mark a todo as completed
- **Arguments**: id (integer): unique identifier
- **Output**: Confirmation message showing updated status
- **Validation**: ID must exist
- **Error Handling**: Shows error message if ID does not exist

#### `incomplete <id>`
- **Purpose**: Mark a todo as incomplete
- **Arguments**: id (integer): unique identifier
- **Output**: Confirmation message showing updated status
- **Validation**: ID must exist
- **Error Handling**: Shows error message if ID does not exist

#### `help`
- **Purpose**: Display available commands and their usage
- **Arguments**: None
- **Output**: Help text showing all available commands
- **Validation**: None
- **Error Handling**: None