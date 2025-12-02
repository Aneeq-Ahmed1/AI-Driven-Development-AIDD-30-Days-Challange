# Tasks: Simple Calculator

**Input**: Design documents from `/specs/001-calculator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Tests are included as requested by the plan's testability principle.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create `src/` directory at repository root
- [ ] T002 Create `tests/unit/` directory at repository root
- [ ] T003 Initialize Python project with `streamlit` and `pytest` dependencies (e.g., `pip install streamlit pytest`)

---

## Phase 2: Foundational (Core Logic & Error Handling)

**Purpose**: Core logic and basic error handling that MUST be complete before the UI can be fully integrated.

**⚠️ CRITICAL**: No UI work can effectively begin until this phase is complete.

- [ ] T004 Create `src/calculator.py` for core calculation logic
- [ ] T005 [P] Implement addition function in `src/calculator.py`
- [ ] T006 [P] Implement subtraction function in `src/calculator.py`
- [ ] T007 [P] Implement multiplication function in `src/calculator.py`
- [ ] T008 [P] Implement division function in `src/calculator.py`
- [ ] T009 Implement expression parsing logic in `src/calculator.py`
- [ ] T010 Implement expression evaluation logic in `src/calculator.py`
- [ ] T011 Implement error handling for division by zero in `src/calculator.py`
- [ ] T012 Implement error handling for invalid input in `src/calculator.py`

**Checkpoint**: Core calculator logic with parsing, evaluation, and basic error handling should be functional and testable independently.

---

## Phase 3: User Story 1 - Perform Basic Calculation (Priority: P1) 🎯 MVP

**Goal**: Enable users to input a mathematical expression and receive the calculated numeric result via a Streamlit UI.

**Independent Test**: Can be fully tested by running the Streamlit app, providing various string expressions (valid and invalid), and verifying the numeric output or error messages.

### Tests for User Story 1 (Test-First Approach)

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T013 [P] [US1] Write unit tests for addition in `tests/unit/calculator_test.py` (e.g., test_add_two_numbers)
- [ ] T014 [P] [US1] Write unit tests for subtraction in `tests/unit/calculator_test.py` (e.g., test_subtract_two_numbers)
- [ ] T015 [P] [US1] Write unit tests for multiplication in `tests/unit/calculator_test.py` (e.g., test_multiply_two_numbers)
- [ ] T016 [P] [US1] Write unit tests for division in `tests/unit/calculator_test.py` (e.g., test_divide_two_numbers)
- [ ] T017 [US1] Write unit tests for division by zero handling in `tests/unit/calculator_test.py` (e.g., test_divide_by_zero)
- [ ] T018 [US1] Write unit tests for invalid input handling in `tests/unit/calculator_test.py` (e.g., test_invalid_expression)
- [ ] T019 [US1] Write unit tests for expression parsing and evaluation in `tests/unit/calculator_test.py`

### Implementation for User Story 1

- [ ] T020 [US1] Create `src/app.py` for the Streamlit UI
- [ ] T021 [US1] Implement basic Streamlit layout in `src/app.py` (input text box, button, result display)
- [ ] T022 [US1] Integrate `calculator.py` functions into `src/app.py` for processing user input
- [ ] T023 [US1] Display results from `calculator.py` in the Streamlit UI
- [ ] T024 [US1] Display error messages from `calculator.py` (e.g., division by zero, invalid input) gracefully in the Streamlit UI

**Checkpoint**: At this point, User Story 1 (basic calculation via Streamlit UI with error handling) should be fully functional and testable independently.

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Minor improvements that affect overall usability.

- [ ] T025 Code cleanup and refactoring in `src/calculator.py` and `src/app.py`
- [ ] T026 Update `README.md` with instructions on how to run the calculator

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

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Core logic before UI integration
- Story complete before moving to next priority

### Parallel Opportunities

- Tasks marked [P] can run in parallel (different files, no dependencies)
- Once Foundational phase completes, User Story 1 can begin.
- Within User Story 1, unit tests (T013-T016) can be written in parallel.

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Write unit tests for addition in tests/unit/calculator_test.py"
Task: "Write unit tests for subtraction in tests/unit/calculator_test.py"
Task: "Write unit tests for multiplication in tests/unit/calculator_test.py"
Task: "Write unit tests for division in tests/unit/calculator_test.py"
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

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
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
