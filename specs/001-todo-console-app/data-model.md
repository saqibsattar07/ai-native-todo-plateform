# Data Model: Todo In-Memory Python Console Application (Phase I)

**Date**: 2026-01-02
**Feature**: Todo In-Memory Python Console Application (Phase I)
**Branch**: 001-todo-console-app

## Entity: Todo Item

### Fields
- **id** (integer): Unique identifier for the todo item, auto-generated using incremental counter
- **description** (string): The task description provided by the user
- **completed** (boolean): Status indicating whether the task is completed (default: False)

### Example Representation
```python
{
    "id": 1,
    "description": "Buy groceries",
    "completed": False
}
```

### Validation Rules
- **id**: Must be a positive integer, unique within the application session
- **description**: Must be a non-empty string (1-500 characters)
- **completed**: Must be a boolean value (True or False)

### State Transitions
- **Initial State**: `completed = False` when todo is created
- **Completed State**: `completed = True` when user marks as completed
- **State cannot revert**: Once completed, a todo remains completed (simplification for Phase I)

## Data Storage Structure

### In-Memory Storage
- **Type**: List of dictionaries
- **Access Pattern**: Sequential iteration for most operations
- **Lookup**: Linear search by ID (acceptable for small datasets in Phase I)

### Example Data Structure
```python
[
    {"id": 1, "description": "Buy groceries", "completed": False},
    {"id": 2, "description": "Walk the dog", "completed": True},
    {"id": 3, "description": "Finish report", "completed": False}
]
```

## Operations on Todo Items

### Create
- Generate next available ID (incremental counter)
- Set description from user input
- Set completed status to False by default

### Read (View All)
- Return all todo items in the storage
- Display ID, description, and completion status

### Update
- Modify the description of an existing todo item
- ID and completion status remain unchanged (unless specifically marked complete)

### Delete
- Remove the todo item from the storage list
- Maintain list integrity after removal

### Mark Complete
- Update the completion status of a todo item to True
- ID and description remain unchanged

## Constraints
- **No Persistence**: Data exists only in memory during application session
- **Single User**: Designed for single-user interaction
- **Session Bound**: All data is lost when application terminates
- **Size Limitation**: Designed for small datasets (tens of items, not thousands)