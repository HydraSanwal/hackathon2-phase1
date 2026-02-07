# Todo App

A command-line todo application with in-memory storage that supports add, view, update, delete, and mark complete/incomplete operations.

## Features

- Add new todo items
- View all todo items
- Update existing todo descriptions
- Delete todo items
- Mark items as complete/incomplete
- In-memory storage (no persistent data)

## Requirements

- Python 3.13 or higher

## Installation

1. Clone or download the repository
2. Navigate to the project directory

## Usage

Run the application with:
```bash
python -m src.todo_app.main
```

Once the application is running, you can use the following commands:

### Adding Todos
```bash
add "Buy groceries"
add "Complete project proposal"
```

### Viewing Todos
```bash
view
```
This displays all todos with their ID, description, and completion status.

### Updating Todos
```bash
update 1 "Buy groceries and household items"
```
This updates the description of the todo with ID 1.

### Deleting Todos
```bash
delete 2
```
This removes the todo with ID 2 from the list.

### Marking as Complete/Incomplete
```bash
complete 1    # Mark todo with ID 1 as complete
incomplete 1  # Mark todo with ID 1 as incomplete
```

### Getting Help
```bash
help
```
Displays available commands and their usage.

## Example Session

```
> add "Learn Python"
Added todo: 1 - Learn Python (Incomplete)
> add "Build a CLI app"
Added todo: 2 - Build a CLI app (Incomplete)
> view
Todos:
1 - Learn Python (Incomplete)
2 - Build a CLI app (Incomplete)
> complete 1
Todo 1 marked as complete: Learn Python
> view
Todos:
1 - Learn Python (Complete)
2 - Build a CLI app (Incomplete)
> update 2 "Build a Python CLI app"
Updated todo: 2 - Build a Python CLI app (Incomplete)
> delete 2
Deleted todo: Build a Python CLI app
```

## Architecture

The application follows a three-layer architecture:

1. **CLI Layer** (`src/todo_app/cli/`): Handles user input and command parsing
2. **Service Layer** (`src/todo_app/services/`): Contains the business logic for todo operations
3. **Model Layer** (`src/todo_app/models/`): Defines the data structures (TodoItem)

## Testing

To run the tests:
```bash
pip install pytest
pytest tests/
```