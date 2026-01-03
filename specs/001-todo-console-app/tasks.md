---
description: "Task list for Todo In-Memory Python Console Application"
---

# Tasks: Todo In-Memory Python Console Application (Phase I)

**Input**: Design documents from `/specs/001-todo-console-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/
- [X] T002 [P] Create directory structure: src/todo_app/, src/todo_app/models/, src/todo_app/services/, src/todo_app/cli/
- [X] T003 [P] Initialize __init__.py files in all directories
- [X] T004 Create requirements.txt with Python 3.13+ compatibility
- [X] T005 Create main application entry point todo_console_app.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T006 Create Todo data model in src/todo_app/models/todo.py based on data-model.md
- [X] T007 [P] Create TodoService in src/todo_app/services/todo_service.py with basic in-memory storage
- [X] T008 Create menu-driven CLI interface framework in src/todo_app/cli/main.py
- [X] T009 Create input validation functions in src/todo_app/services/validation.py
- [X] T010 Create error handling utilities in src/todo_app/utils/errors.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo Item (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items with unique identifiers and pending completion status

**Independent Test**: Can be fully tested by running the application and adding a new todo item, then verifying it appears in the list. Delivers the core value of task tracking.

### Implementation for User Story 1

- [X] T011 [P] [US1] Implement add_todo method in TodoService in src/todo_app/services/todo_service.py
- [X] T012 [P] [US1] Implement input validation for add todo in src/todo_app/services/validation.py
- [X] T013 [US1] Create CLI handler for adding todos in src/todo_app/cli/main.py
- [X] T014 [US1] Add menu option for adding todos in src/todo_app/cli/main.py
- [X] T015 [US1] Add error handling for empty descriptions in src/todo_app/utils/errors.py
- [X] T016 [US1] Test add functionality by adding a todo and viewing the list

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todo Items (Priority: P2)

**Goal**: Enable users to view all todo items with their unique identifiers and completion status

**Independent Test**: Can be fully tested by adding several todo items and then viewing the complete list. Delivers visibility of all tasks.

### Implementation for User Story 2

- [X] T017 [P] [US2] Implement view_todos method in TodoService in src/todo_app/services/todo_service.py
- [X] T018 [P] [US2] Create CLI handler for viewing todos in src/todo_app/cli/main.py
- [X] T019 [US2] Add menu option for viewing todos in src/todo_app/cli/main.py
- [X] T020 [US2] Implement proper display formatting following contract in src/todo_app/cli/main.py
- [X] T021 [US2] Handle empty list case per contract in src/todo_app/cli/main.py
- [X] T022 [US2] Test view functionality with both populated and empty lists

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Todo as Completed (Priority: P3)

**Goal**: Enable users to mark a todo item as completed using its unique identifier

**Independent Test**: Can be fully tested by adding a todo item, marking it as completed, and verifying its status changes. Delivers task status management capability.

### Implementation for User Story 3

- [X] T023 [P] [US3] Implement mark_completed method in TodoService in src/todo_app/services/todo_service.py
- [X] T024 [P] [US3] Create CLI handler for marking todos as completed in src/todo_app/cli/main.py
- [X] T025 [US3] Add menu option for marking completed in src/todo_app/cli/main.py
- [X] T026 [US3] Add validation for existing ID in src/todo_app/services/validation.py
- [X] T027 [US3] Add error handling for non-existent IDs in src/todo_app/utils/errors.py
- [X] T028 [US3] Test mark completed functionality with valid and invalid IDs

**Checkpoint**: User Stories 1, 2, and 3 should all work independently

---

## Phase 6: User Story 4 - Update Todo Item (Priority: P4)

**Goal**: Enable users to update the description of existing todo items using their unique identifiers

**Independent Test**: Can be fully tested by adding a todo item, updating its description, and verifying the change persists. Delivers task modification capability.

### Implementation for User Story 4

- [X] T029 [P] [US4] Implement update_todo method in TodoService in src/todo_app/services/todo_service.py
- [X] T030 [P] [US4] Create CLI handler for updating todos in src/todo_app/cli/main.py
- [X] T031 [US4] Add menu option for updating todos in src/todo_app/cli/main.py
- [X] T032 [US4] Add validation for existing ID and non-empty description in src/todo_app/services/validation.py
- [X] T033 [US4] Add error handling for invalid inputs in src/todo_app/utils/errors.py
- [X] T034 [US4] Test update functionality with valid and invalid inputs

**Checkpoint**: User Stories 1, 2, 3, and 4 should all work independently

---

## Phase 7: User Story 5 - Delete Todo Item (Priority: P5)

**Goal**: Enable users to delete existing todo items using their unique identifiers

**Independent Test**: Can be fully tested by adding a todo item, deleting it, and verifying it no longer appears in the list. Delivers task removal capability.

### Implementation for User Story 5

- [X] T035 [P] [US5] Implement delete_todo method in TodoService in src/todo_app/services/todo_service.py
- [X] T036 [P] [US5] Create CLI handler for deleting todos in src/todo_app/cli/main.py
- [X] T037 [US5] Add menu option for deleting todos in src/todo_app/cli/main.py
- [X] T038 [US5] Add validation for existing ID in src/todo_app/services/validation.py
- [X] T039 [US5] Add error handling for non-existent IDs in src/todo_app/utils/errors.py
- [X] T040 [US5] Test delete functionality with valid and invalid IDs

**Checkpoint**: All user stories should now be independently functional

---

[Add more user stories as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T041 [P] Add proper error messages per contract in src/todo_app/utils/errors.py
- [X] T042 [P] Add type hints to all functions following Python best practices
- [X] T043 Add comprehensive documentation to all modules
- [X] T044 [P] Implement consistent formatting per contract specifications
- [X] T045 Add performance validation to ensure operations complete under 1 second
- [X] T046 Run complete application test with all features
- [X] T047 Create README.md with setup and usage instructions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Models before services (if applicable)
- Services before CLI handlers
- Core implementation before integration
- Story complete before moving to next priority
- Validation and error handling integrated throughout

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members
- Tasks within each user story that are marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch all parallel tasks for User Story 1 together:
T011: Implement add_todo method in TodoService in src/todo_app/services/todo_service.py
T012: Implement input validation for add todo in src/todo_app/services/validation.py
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Run application to verify add functionality works
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [US1], [US2], etc. label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify functionality works after each task or logical group
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence