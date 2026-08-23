# State and Observability Boundary Design — 2026-08-24

Status: `DESIGN_CANDIDATE`
Implementation: `NOT_IMPLEMENTED`
Validation: `DOCUMENT_REVIEW_ONLY`

## Problem

Agent architecture discussions frequently collapse several independent surfaces into one word such as `state`, `memory`, or `success`. August 2026 research and current primary standards show that this hides important boundaries.

This design records a reusable reference decomposition without claiming an implemented runtime.

## Reference architecture

### 1. Interaction identity

A future agent runtime SHOULD distinguish:

- `conversation/session identity`
- `task/work identity`
- `protocol context identity`
- `execution/attempt identity`
- `artifact/output identity`

A2A v1.0 provides explicit Task and optional Context identities. Google ADK separately models Session, State, and cross-session Memory.

### 2. State scopes

Do not use one unqualified `memory` bucket.

Reference scopes:

- ephemeral turn data
- current-session state
- task lifecycle state
- durable cross-session memory
- external authoritative state
- derived/cache state

Every persistence or continuity claim should identify which scope is being discussed and who owns it.

### 3. Observability surfaces

A future runtime SHOULD distinguish:

- input/configuration record
- trajectory/trace
- tool and handoff spans
- state mutations
- final outcome/postcondition
- evaluator/grader result
- reviewer decision

OpenAI Agents SDK tracing is a concrete example of hierarchical trace/span evidence. Anthropic's agent-evaluation guidance is a concrete example of separating transcript/trajectory, outcome, graders, and harness.

### 4. Evidence relation

`TRACE_PRESENT` does not imply `OUTCOME_CORRECT`.

`OUTCOME_CORRECT` does not imply every intermediate decision was acceptable.

`GRADER_PASS` does not imply complete coverage.

A strong release claim may combine these evidence types, but it keeps them individually addressable.

### 5. Protocol boundary

MCP 2026-07-28 and A2A v1.0 illustrate different protocol scopes:

- MCP: model/tool/data interaction protocol surface with a stateless 2026-07-28 core
- A2A: agent-to-agent interoperability with stateful Task lifecycle and Agent Card discovery

This repository treats those as external architecture references, not a requirement to combine them and not evidence of local implementation.

## Mapping to verified core

- AF-ARCH-001: full configured system is the evaluated object
- AF-ARCH-004: evaluators create evidence, not truth
- AF-ARCH-007: state scope must be explicit
- AF-ARCH-008: trajectory and outcome are complementary evidence
- SOURCES_2026_08_24 S33–S37: current primary-source anchors

## Non-goals

This design does not:

- add a runtime
- add MCP or A2A endpoints
- add ADK/OpenAI SDK dependencies
- change Jules Daily/Weekly/Monthly tasks
- add CI, gates, workflows, or deployment
- claim safety, convergence, determinism, or interoperability

## Promotion criteria

Promotion beyond `DESIGN_CANDIDATE` requires an executable artifact, explicit schema/contracts, repository tests, failure cases, and a separate reviewed implementation decision.
