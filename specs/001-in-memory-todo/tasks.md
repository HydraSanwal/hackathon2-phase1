---
description: "Task list for Phase I - In-Memory Python Console Todo App implementation"
---

# Tasks: Phase I - In-Memory Python Console Todo App

**Input**: Design documents from `/specs/001-in-memory-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are included as requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths follow the structure from plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/todo_app/
- [X] T002 Initialize Python 3.13+ project with pyproject.toml
- [X] T003 [P] Create __init__.py files for packages: src/todo_app/__init__.py, src/todo_app/models/__init__.py, src/todo_app/services/__init__.py, src/todo_app/cli/__init__.py
- [X] T004 Create main.py file in src/todo_app/main.py

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 [P] Create TodoItem model in src/todo_app/models/todo_item.py
- [X] T006 [P] Create TodoList data structure in src/todo_app/models/todo_list.py
- [X] T007 Create TodoService in src/todo_app/services/todo_service.py
- [X] T008 Create CLI interface in src/todo_app/cli/todo_cli.py
- [X] T009 Create basic application structure in src/todo_app/main.py
- [X] T010 Configure basic error handling and validation in src/todo_app/services/todo_service.py
- [X] T011 [P] Set up basic test structure with tests/unit/ and tests/integration/ directories

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Todo Item (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items to their list through a command-line interface

**Independent Test**: Run the add command with a task description and verify it appears in the list

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T012 [P] [US1] Unit test for TodoService.add_todo in tests/unit/test_todo_service.py
- [X] T013 [P] [US1] Unit test for TodoItem creation in tests/unit/test_todo_item.py

### Implementation for User Story 1

- [X] T014 [US1] Implement TodoItem model with id, description, completed, created_at fields in src/todo_app/models/todo_item.py
- [X] T015 [US1] Implement TodoList.add_item functionality in src/todo_app/models/todo_list.py
- [X] T016 [US1] Implement TodoService.add_todo method in src/todo_app/services/todo_service.py
- [X] T017 [US1] Implement CLI add command in src/todo_app/cli/todo_cli.py
- [X] T018 [US1] Connect CLI add command to service layer in src/todo_app/cli/todo_cli.py
- [X] T019 [US1] Add validation for empty descriptions in src/todo_app/services/todo_service.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Todo Items (Priority: P1)

**Goal**: Allow users to view all their todo items in the console to see what tasks they have planned

**Independent Test**: Add one or more todos and then view them, ensuring all todos are displayed with their status

### Tests for User Story 2 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T020 [P] [US2] Unit test for TodoService.get_all_todos in tests/unit/test_todo_service.py
- [X] T021 [P] [US2] Integration test for add and view workflow in tests/integration/test_todo_operations.py

### Implementation for User Story 2

- [X] T022 [US2] Implement TodoList.get_all_items functionality in src/todo_app/models/todo_list.py
- [X] T023 [US2] Implement TodoService.get_all_todos method in src/todo_app/services/todo_service.py
- [X] T024 [US2] Implement CLI view command in src/todo_app/cli/todo_cli.py
- [X] T025 [US2] Connect CLI view command to service layer in src/todo_app/cli/todo_cli.py
- [X] T026 [US2] Format output to show ID, description, and completion status in src/todo_app/cli/todo_cli.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Todo as Complete/Incomplete (Priority: P2)

**Goal**: Enable users to mark todo items as complete or incomplete to track progress and manage tasks effectively

**Independent Test**: Add a todo, mark it as complete/incomplete, and verify the status change is reflected

### Tests for User Story 3 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T027 [P] [US3] Unit test for TodoService.mark_todo_completed in tests/unit/test_todo_service.py
- [X] T028 [P] [US3] Unit test for TodoService.mark_todo_incomplete in tests/unit/test_todo_service.py

### Implementation for User Story 3

- [X] T029 [US3] Implement TodoList.mark_complete functionality in src/todo_app/models/todo_list.py
- [X] T030 [US3] Implement TodoList.mark_incomplete functionality in src/todo_app/models/todo_list.py
- [X] T031 [US3] Implement TodoService.mark_todo_completed method in src/todo_app/services/todo_service.py
- [X] T032 [US3] Implement TodoService.mark_todo_incomplete method in src/todo_app/services/todo_service.py
- [X] T033 [US3] Implement CLI complete command in src/todo_app/cli/todo_cli.py
- [X] T034 [US3] Implement CLI incomplete command in src/todo_app/cli/todo_cli.py
- [X] T035 [US3] Connect CLI mark commands to service layer in src/todo_app/cli/todo_cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Update Todo Description (Priority: P3)

**Goal**: Allow users to update the description of existing todo items to refine or correct task descriptions

**Independent Test**: Add a todo, update its description, and verify the change is reflected when viewing

### Tests for User Story 4 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T036 [P] [US4] Unit test for TodoService.update_todo in tests/unit/test_todo_service.py
- [X] T037 [P] [US4] Integration test for update workflow in tests/integration/test_todo_operations.py

### Implementation for User Story 4

- [X] T038 [US4] Implement TodoList.update_item functionality in src/todo_app/models/todo_list.py
- [X] T039 [US4] Implement TodoService.update_todo method in src/todo_app/services/todo_service.py
- [X] T040 [US4] Implement CLI update command in src/todo_app/cli/todo_cli.py
- [X] T041 [US4] Connect CLI update command to service layer in src/todo_app/cli/todo_cli.py
- [X] T042 [US4] Add validation for empty new descriptions in src/todo_app/services/todo_service.py

**Checkpoint**: At this point, User Stories 1, 2, 3, and 4 should all work independently

---

## Phase 7: User Story 5 - Delete Todo Items (Priority: P3)

**Goal**: Allow users to delete todo items they no longer need to keep their list clean and focused

**Independent Test**: Add a todo, delete it, and verify it no longer appears in the list when viewing

### Tests for User Story 5 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T043 [P] [US5] Unit test for TodoService.delete_todo in tests/unit/test_todo_service.py
- [X] T044 [P] [US5] Integration test for delete workflow in tests/integration/test_todo_operations.py

### Implementation for User Story 5

- [X] T045 [US5] Implement TodoList.delete_item functionality in src/todo_app/models/todo_list.py
- [X] T046 [US5] Implement TodoService.delete_todo method in src/todo_app/services/todo_service.py
- [X] T047 [US5] Implement CLI delete command in src/todo_app/cli/todo_cli.py
- [X] T048 [US5] Connect CLI delete command to service layer in src/todo_app/cli/todo_cli.py
- [X] T049 [US5] Add proper error handling for invalid IDs in src/todo_app/services/todo_service.py

**Checkpoint**: All five user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T050 [P] Create README.md with setup and usage instructions
- [X] T051 [P] Add help command to CLI in src/todo_app/cli/todo_cli.py
- [X] T052 [P] Improve error messages for better UX in src/todo_app/services/todo_service.py
- [X] T053 [P] Add input validation for all CLI commands in src/todo_app/cli/todo_cli.py
- [X] T054 [P] Add comprehensive logging for all operations in src/todo_app/services/todo_service.py
- [X] T055 [P] Add integration tests for all CLI commands in tests/integration/test_cli_integration.py
- [X] T056 [P] Update main.py to properly initialize and run the application in src/todo_app/main.py
- [X] T057 Run quickstart.md validation to ensure all functionality works as expected

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
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints/CLI
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test for TodoService.add_todo in tests/unit/test_todo_service.py"
Task: "Unit test for TodoItem creation in tests/unit/test_todo_item.py"

# Launch all models for User Story 1 together:
Task: "Create TodoItem model in src/todo_app/models/todo_item.py"
Task: "Create TodoList.add_item functionality in src/todo_app/models/todo_list.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

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
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence