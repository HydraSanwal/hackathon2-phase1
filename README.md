# Todo App

A user-friendly command-line todo application with an interactive menu-driven interface and in-memory storage.

## Features

- ✅ **Add new todo items** - Create tasks with descriptions
- 📋 **View all todos** - See your complete todo list with details
- ✏️ **Update existing todos** - Modify task descriptions
- 🗑️ **Delete todo items** - Remove completed or unwanted tasks
- ✓ **Mark items as complete/incomplete** - Track your progress
- 💾 **In-memory storage** - No persistent data (resets on exit)
- 🎨 **Interactive menu interface** - Easy-to-use numbered menu system

## Requirements

- Python 3.13 or higher

## Installation

1. Clone or download the repository
2. Navigate to the project directory

## Usage

Run the application with:
```bash
cd src
python -m todo_app.main
```

Or from the repository root:
```bash
python -m src.todo_app.main
```

### Interactive Menu

Once the application starts, you'll see an interactive menu with your current todos displayed at the top:

```
============================================================
                    TODO APP
============================================================

>> Your Todo List: (Empty)
------------------------------------------------------------
   No todos yet. Add one to get started!
------------------------------------------------------------
                      MAIN MENU
------------------------------------------------------------
   1. Add a new todo
   2. View all todos
   3. Update a todo
   4. Mark todo as complete
   5. Mark todo as incomplete
   6. Delete a todo
   7. Exit
------------------------------------------------------------

>> Enter your choice (1-7):
```

Simply enter the number corresponding to the action you want to perform.

### Menu Options

#### 1. Add a New Todo
- Select option `1`
- Enter your todo description when prompted
- The todo will be added with a unique ID

#### 2. View All Todos
- Select option `2`
- See a detailed view of all your todos including:
  - Todo ID
  - Description
  - Completion status
  - Creation timestamp

#### 3. Update a Todo
- Select option `3`
- Enter the ID of the todo you want to update
- Enter the new description
- The todo will be updated while preserving its completion status

#### 4. Mark Todo as Complete
- Select option `4`
- Enter the ID of the todo to mark as complete
- The todo status will change to "Complete"

#### 5. Mark Todo as Incomplete
- Select option `5`
- Enter the ID of the todo to mark as incomplete
- The todo status will change to "Incomplete"

#### 6. Delete a Todo
- Select option `6`
- Enter the ID of the todo to delete
- Confirm the deletion when prompted
- The todo will be permanently removed

#### 7. Exit
- Select option `7` to exit the application
- All todos will be lost (in-memory storage only)

## Example Session

```
============================================================
                    TODO APP
============================================================

>> Your Todo List: (Empty)
------------------------------------------------------------
   No todos yet. Add one to get started!
------------------------------------------------------------

>> Enter your choice (1-7): 1

============================================================
                  ADD NEW TODO
============================================================

>> Enter todo description: Learn Python basics

[+] Success! Todo added with ID: 1
    Description: Learn Python basics

Press Enter to continue...

============================================================
                    TODO APP
============================================================

>> Your Todo List: (1 items)
------------------------------------------------------------
   [ ] [1] Learn Python basics
       Status: Incomplete

------------------------------------------------------------

>> Enter your choice (1-7): 4

============================================================
                MARK TODO AS COMPLETE
============================================================

>> Enter todo ID to mark as complete: 1

[+] Success! Todo 1 marked as complete!
    Description: Learn Python basics

Press Enter to continue...

============================================================
                    TODO APP
============================================================

>> Your Todo List: (1 items)
------------------------------------------------------------
   [X] [1] Learn Python basics
       Status: Complete

------------------------------------------------------------
```

## Status Indicators

- `[ ]` - Incomplete todo
- `[X]` - Complete todo

## Architecture

The application follows a clean three-layer architecture:

1. **CLI Layer** (`src/todo_app/cli/`): Handles user interaction through an interactive menu interface
2. **Service Layer** (`src/todo_app/services/`): Contains the business logic for todo operations
3. **Model Layer** (`src/todo_app/models/`): Defines the data structures (TodoItem and TodoList)

### Key Design Principles

- **Separation of Concerns**: Clear boundaries between UI, business logic, and data
- **In-Memory Storage**: All data stored in Python data structures (lists, dictionaries)
- **Deterministic Behavior**: Consistent and predictable operations
- **User-Friendly Interface**: Menu-driven design eliminates need to memorize commands

## Testing

The application includes comprehensive test coverage:

- **Unit Tests**: Test individual components (models, services)
- **Integration Tests**: Test complete workflows

To run the tests:
```bash
pip install pytest
pytest tests/
```

Test results: **28/28 tests passing** (100% pass rate)

## Project Structure

```
src/
├── todo_app/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── models/
│   │   ├── __init__.py
│   │   ├── todo_item.py     # TodoItem model
│   │   └── todo_list.py     # TodoList data structure
│   ├── services/
│   │   ├── __init__.py
│   │   └── todo_service.py  # Business logic
│   └── cli/
│       ├── __init__.py
│       └── todo_cli.py      # Interactive menu interface
tests/
├── unit/
│   ├── test_todo_item.py
│   └── test_todo_service.py
└── integration/
    └── test_todo_operations.py
```

## Notes

- **Data Persistence**: This is an in-memory application. All todos are lost when you exit.
- **Python Version**: Requires Python 3.13+ for optimal compatibility
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Future Enhancements (Phase II+)

This is Phase I of a multi-phase project. Future phases will include:
- Phase II: Web application with persistent storage (Next.js + FastAPI)
- Phase III: AI-powered todo chatbot
- Phase IV: Kubernetes deployment
- Phase V: Cloud-native architecture with advanced features