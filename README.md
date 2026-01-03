# Todo Console Application

A simple, in-memory todo list application with a command-line interface.

## Features

- Add new todo items
- View all todo items
- Mark todo items as completed
- Update todo item descriptions
- Delete todo items
- In-memory storage (no database required)

## Requirements

- Python 3.13 or higher

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. No additional dependencies required - the application uses only Python standard library

## Usage

Run the application:

```bash
python todo_console_app.py
```

The application will present a menu with the following options:

1. Add a new todo
2. View all todos
3. Mark a todo as completed
4. Update a todo description
5. Delete a todo
6. Exit

## Architecture

The application follows a clean architecture pattern with separation of concerns:

- **Models**: Define the data structures (Todo)
- **Services**: Handle business logic (TodoService)
- **CLI**: Handle user interface (TodoCLI)
- **Validation**: Handle input validation (validation.py)
- **Utils**: Handle error utilities (errors.py)

## Data Model

Each todo item has:
- `id`: Unique identifier (integer)
- `description`: Task description (string)
- `completed`: Completion status (boolean, default: False)