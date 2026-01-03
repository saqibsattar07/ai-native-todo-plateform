# CLI Contract: Todo In-Memory Python Console Application (Phase I)

**Date**: 2026-01-02
**Feature**: Todo In-Memory Python Console Application (Phase I)
**Branch**: 001-todo-console-app

## Overview

This contract defines the command-line interface for the Todo console application, specifying the expected user interactions, input formats, output formats, and error responses.

## Entry Point

### Application Start
- **Command**: `python src/todo_app/cli/main.py` or `python todo_console_app.py`
- **Response**: Displays main menu with available options
- **Expected Output**: Menu with numbered options for user to select

## User Actions and Contracts

### 1. Add Todo Item

**User Action**: Select option to add a new todo
**Input Format**: Free text description (1-500 characters)
**Validation**:
- Non-empty string
- Length between 1-500 characters
**Success Response**:
- Todo added with unique ID
- Confirmation message: "Todo added with ID: [ID]"
**Error Responses**:
- Empty input: "Error: Todo description cannot be empty"
- Too long: "Error: Todo description exceeds 500 characters"

### 2. View Todo Items

**User Action**: Select option to view all todos
**Input Format**: None required
**Success Response**:
```
ID  | Description          | Status
----|----------------------|--------
1   | Buy groceries        | Pending
2   | Walk the dog         | Completed
3   | Finish report        | Pending
```
**Empty State Response**:
```
No todos found.
```

### 3. Update Todo Item

**User Action**: Select option to update an existing todo
**Input Format**:
1. Todo ID (positive integer)
2. New description (1-500 characters)
**Validation**:
- ID must exist in current list
- Description must be non-empty
**Success Response**:
- Confirmation: "Todo [ID] updated successfully"
**Error Responses**:
- Non-existent ID: "Error: Todo with ID [ID] not found"
- Empty description: "Error: Todo description cannot be empty"

### 4. Delete Todo Item

**User Action**: Select option to delete a todo
**Input Format**: Todo ID (positive integer)
**Validation**: ID must exist in current list
**Success Response**:
- Confirmation: "Todo [ID] deleted successfully"
**Error Response**:
- Non-existent ID: "Error: Todo with ID [ID] not found"

### 5. Mark Todo as Completed

**User Action**: Select option to mark a todo as completed
**Input Format**: Todo ID (positive integer)
**Validation**: ID must exist in current list
**Success Response**:
- Confirmation: "Todo [ID] marked as completed"
**Error Response**:
- Non-existent ID: "Error: Todo with ID [ID] not found"

### 6. Exit Application

**User Action**: Select option to exit
**Response**: Clean application shutdown with no output

## Error Handling Contract

### Invalid Menu Selection
**Input**: Number or character not in menu range
**Response**: "Invalid selection. Please choose a valid option."

### Invalid ID Format
**Input**: Non-numeric ID when numeric ID expected
**Response**: "Invalid ID format. Please enter a number."

### General Error Format
All errors follow the pattern: "Error: [descriptive message]"

## Data Persistence Contract

### In-Memory Only
- All data exists only in application memory
- Data is lost when application terminates
- No file or database I/O during Phase I

## Exit Codes

- **0**: Normal exit (user chose to exit)
- **1**: Application error (should not occur in normal operation)

## Performance Expectations

- All operations should complete in under 1 second
- Menu display should be immediate (< 0.1 seconds)
- Response to user input should be immediate (< 0.1 seconds)

## User Experience Standards

### Consistency
- Menu options remain in same positions across sessions
- Error messages follow consistent format
- Success messages follow consistent format

### Feedback
- All user actions receive immediate feedback
- Confirmation messages for all modifications
- Clear error messages with actionable guidance