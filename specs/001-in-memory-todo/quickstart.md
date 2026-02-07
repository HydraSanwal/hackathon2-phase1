# Quickstart Guide: Phase I - In-Memory Python Console Todo App

**Feature**: Phase I - In-Memory Python Console Todo App
**Date**: 2026-02-07
**Branch**: 001-in-memory-todo

## Project Setup

### Prerequisites
- Python 3.13 or higher
- pip package manager
- uv package installer (optional but recommended)

### Installation

1. Clone or navigate to the project directory
2. Install dependencies (if any are added later):
   ```bash
   pip install -e .
   ```
   or if using uv:
   ```bash
   uv sync
   ```

### Running the Application

To run the console application:
```bash
python -m src.todo_app.main
```

Or if installed as a module:
```bash
python -c "from src.todo_app.main import main; main()"
```

## Available Commands

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

## Architecture Overview

The application follows a three-layer architecture:

1. **CLI Layer** (`src/todo_app/cli/`): Handles user input and command parsing
2. **Service Layer** (`src/todo_app/services/`): Contains the business logic for todo operations
3. **Model Layer** (`src/todo_app/models/`): Defines the data structures (TodoItem)

## Example Usage Session

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

## Development

### Running Tests
```bash
pytest tests/
```

### Project Structure
- `src/todo_app/` - Main application source code
- `src/todo_app/models/` - Data models (TodoItem)
- `src/todo_app/services/` - Business logic (TodoService)
- `src/todo_app/cli/` - Command-line interface
- `tests/` - Unit and integration tests