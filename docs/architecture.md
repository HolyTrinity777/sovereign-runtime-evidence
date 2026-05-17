# Architecture

## Overview

This document describes the high-level architecture of the Sovereign Runtime public evidence package. The system is organized as a 7-agent sovereign actor runtime designed to maintain bounded digital sovereignty under infrastructure chaos and adversarial conditions.

This document intentionally describes roles, boundaries, and observable behavior only. It does not disclose internal orchestration logic, negotiation rules, or private defense mechanisms.

## Architectural goals

The runtime is designed to:

- Preserve identity continuity across restart, migration, and isolation events.
- Enforce policy supremacy over unsafe or unauthorized commands.
- Maintain audit integrity under tamper, replay, and partial failure scenarios.
- Fail closed when uncertainty or corruption is detected.
- Degrade safely under resource pressure and infrastructure disruption.

## High-level role model

The runtime is organized into seven public roles:

- **Consensus** — Coordinates collective decision-making while preserving global invariants.
- **Healer** — Restores state and supports recovery after failure or isolation.
- **Anxiarch** — Detects threats and enforces policy boundaries.
- **Destroyer** — Performs controlled termination and isolation of compromised components.
- **Limbrix** — Governs resource consumption and throttling.
- **Preaxis** — Preserves identity continuity during migration and restart.
- **Vortexus** — Enforces sovereignty boundaries and system integrity constraints.

These roles are published as functional abstractions. The internal mechanics used to implement them are intentionally private.

## System boundaries

The public evidence package is divided into three layers:

### Public layer
The public layer contains:
- Documentation.
- Test datasets.
- Aggregate results.
- Evidence artifacts.
- Optional minimal shell behavior.

### Protected core
The protected core contains:
- The actual 7-agent orchestration engine.
- Internal policy resolution logic.
- Arbitration and negotiation behavior.
- Hidden scoring or weighting mechanisms.
- Private defense implementations.

### Evidence layer
The evidence layer contains:
- The test methodology.
- The run plans.
- The dataset manifest.
- The result summaries.
- The hashes used to verify integrity.

## Observability model

The public package is designed to expose only observable behavior. That includes:

- Whether unsafe commands are refused.
- Whether state continuity is preserved.
- Whether audit trails remain intact.
- Whether the system fails closed under stress.
- Whether the runtime recovers cleanly after disruption.

The package does not expose the internal sequence of decisions that leads to those behaviors.

## Test relationship to architecture

The chaos suite was used to validate the architecture under:
- Process termination.
- Network partition.
- Latency injection.
- Read-only storage conditions.
- File and checkpoint corruption.
- Resource exhaustion.
- Conflicting commands.
- Advanced adversarial inputs.

The purpose of these tests is to verify that the architecture preserves its public invariants under stress.

## Public shell

If included, the public shell should provide only minimal observable interactions such as:

- Policy submission.
- Refusal logging.
- Audit trail generation.
- Basic continuity checks.

The public shell should not reveal the private orchestration core.

## Summary

This architecture is designed around a simple principle: public behavior should be observable and verifiable, while private control logic remains protected. The system is therefore suitable for a hybrid release model in which public evidence is shared for review and the core runtime remains under NDA or commercial protection.
