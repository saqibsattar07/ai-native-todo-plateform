---
id: 1
title: Update-Project-Constitution
stage: constitution
date: 2026-01-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: user
command: /sp.constitution
labels: [constitution,ai-native-todo-platform]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 -
---
## Prompt

```text
Project: AI-Native Todo Platform (Console → Web → Agentic AI → Kubernetes → Cloud)

Vision:
Build an end-to-end AI-native Todo platform that evolves from a simple in-memory console app
into a production-grade, agent-driven, cloud-native system using modern AI, web, and DevOps stacks.

The project must demonstrate:
- Progressive system design maturity
- Agentic AI integration using official SDKs
- Production-ready deployment practices
- Clear separation of concerns across phases

--------------------------------------------------
Core Principles:
- Incremental Evolution: Each phase must build logically on the previous phase
- Simplicity First: Prefer clear, minimal solutions before optimization
- AI-Native Design: AI components are first-class citizens, not add-ons
- Reproducibility: Every phase must be runnable and verifiable
- Observability & Reliability: Systems should be debuggable and measurable
- Security by Design: Secrets, auth, and data access handled properly

--------------------------------------------------
Phase Standards:

Phase I – In-Memory Python Console App
- Technology: Python, Claude Code, Spec-Kit Plus
- Rules:
  - No external database or persistence
  - Pure in-memory data structures
  - Clear domain models (Todo, User, State)
  - Focus on correctness and clean logic
- Success Output:
  - Fully functional CLI Todo app
  - Well-documented commands and flows

--------------------------------------------------
Phase II – Full-Stack Web Application
- Technology: Next.js, FastAPI, SQLModel, Neon DB
- Rules:
  - Frontend and backend must be fully decoupled
  - API contracts must be explicit and versioned
  - SQLModel used for schema + validation
  - Neon DB used as the single source of truth
- Success Output:
  - Deployed frontend and backend
  - CRUD Todo operations via REST API
  - Persistent data with migrations

--------------------------------------------------
Phase III – AI-Powered Todo Chatbot
- Technology: OpenAI ChatKit, Agents SDK, Official MCP SDK
- Rules:
  - AI must interact via tools/functions, not hardcoded logic
  - Agent must understand intent, context, and task state
  - MCP used for structured capability exposure
  - No hallucinated actions allowed
- Success Output:
  - Chat-based Todo management
  - Agent can create, update, prioritize, and explain Todos
  - Tool calls are auditable and traceable

--------------------------------------------------
Phase IV – Local Kubernetes Deployment
- Technology: Docker, Minikube, Helm, kubectl-ai, kagent
- Rules:
  - Each service must have its own container
  - Helm charts must be reproducible
  - kubectl-ai used for cluster interaction
  - kagent used for operational intelligence
- Success Output:
  - Fully running system on local Kubernetes
  - Scalable services with proper configs
  - Clear deployment documentation

--------------------------------------------------
Phase V – Advanced Cloud Deployment
- Technology: Kafka, Dapr, DigitalOcean DOKS
- Rules:
  - Event-driven architecture using Kafka
  - Dapr used for service invocation and state management
  - Cloud deployment must be production-ready
  - Horizontal scalability must be demonstrated
- Success Output:
  - Deployed on DigitalOcean Kubernetes (DOKS)
  - Async Todo events (create/update/delete)
  - Resilient, scalable architecture

--------------------------------------------------
Quality Standards:
- Code Quality:
  - Clear folder structure
  - Meaningful naming
  - No dead or unused code
- Documentation:
  - README per phase
  - Architecture diagrams where applicable
- Testing:
  - Unit tests for core logic
  - API tests for backend
- AI Safety:
  - Guardrails for agent actions
  - Explicit tool permissions

--------------------------------------------------
Constraints:
- Each phase must be independently runnable
- No skipping phases
- No vendor lock-in beyond stated stack
- Secrets must never be hardcoded
- Logs and errors must be human-readable

--------------------------------------------------
Success Criteria:
- All phases completed and documented
- System evolves cleanly without rewrites
- AI agent performs reliable task execution
- Kubernetes and cloud deployments are stable
- Project demonstrates real-world AI-native engineering skills

--------------------------------------------------
Definition of Done:
- Code passes linting and tests
- Deployments succeed without manual intervention
- AI actions are explainable and traceable
- Project is portfolio-ready and interview-ready
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

Follow this execution flow:

1. Load the existing constitution template at `.specify/memory/constitution.md`.
   - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
   **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

2. Collect/derive values for placeholders:
   - If user input (conversation) supplies a value, use it.
   - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
   - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If version bump type ambiguous, propose reasoning before finalizing.

3. Draft the updated constitution content:
   - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
   - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
   - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
   - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert prior checklist into active validations):
   - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
   - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
   - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - Follow-up TODOs if any placeholders intentionally deferred.

6. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches report.
   - Dates ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

8. Output a final summary to the user with:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

Formatting & Style Requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.
```

## Response snapshot

## Final Summary

I have successfully updated the project constitution with the following details:

**New Version**: 1.0.0 (initial version based on detailed requirements provided)
**Bump Rationale**: This is the initial version of the constitution, incorporating the comprehensive requirements for the AI-Native Todo Platform project as specified in the user input.

**Changes Made**:
- Filled all placeholder tokens with concrete values derived from the user input
- Added 6 core principles aligned with the project vision
- Added Quality Standards and Development Workflow sections
- Added Governance section with success criteria
- Included a Sync Impact Report at the top of the file

**Files Updated**:
- `.specify/memory/constitution.md` - Updated with the complete constitution

**Follow-up Items**:
- `[RATIFICATION_DATE]` is marked as TODO and needs to be determined later
- No other files require manual updates as the templates automatically reference the constitution

**Suggested Commit Message**: `docs: add constitution for AI-Native Todo Platform v1.0.0`

The constitution now fully reflects the project requirements for the AI-Native Todo Platform, covering all phases from the in-memory console app through to cloud deployment, with clear principles and governance guidelines.

## Outcome

- ✅ Impact: Updated project constitution with comprehensive principles and guidelines for AI-Native Todo Platform
- 🧪 Tests: No tests required for this documentation update
- 📁 Files: Updated .specify/memory/constitution.md with version 1.0.0
- 🔁 Next prompts: Project can now proceed with spec, plan, and task creation based on new constitution
- 🧠 Reflection: Constitution successfully captures all project phases and principles from user requirements

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A