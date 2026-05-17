# Sovereign Runtime — Public Evidence Package v0.1

![Version](https://img.shields.io/badge/version-v0.1-blue)
![Status](https://img.shields.io/badge/status-public_evidence_package-success)
![Pass Rate](https://img.shields.io/badge/pass_rate-581%2F581%20(100%25)-brightgreen)
![Scope](https://img.shields.io/badge/scope-7%20agents%20%7C%2021%20fault%20categories%20%7C%20581%20runs-informational)

This repository contains the public evidence package for a 7-agent sovereign actor runtime designed for bounded digital sovereignty. It documents high-level architecture, test methodology, aggregate results, and reproducible public artifacts without disclosing private orchestration internals.

## Contents

- `result.json` — Aggregated results and metadata.
- `tests_dataset.csv` — Tabular test dataset.
- `tests_dataset.json` — Structured JSON test dataset.
- `screenshot.png` — Visual summary of the completed run.
- `CHAOS_SUITE.md` — Test categories, methodology, and success criteria.

## System Overview

The runtime is organized around seven public roles:

- **Consensus** — Coordinates collective decision-making while preserving system invariants.
- **Healer** — Handles recovery and state restoration.
- **Anxiarch** — Oversees threat detection and policy enforcement.
- **Destroyer** — Performs controlled termination and isolation of compromised components.
- **Limbrix** — Manages resource governance and self-throttling.
- **Preaxis** — Maintains identity continuity across migration and restart events.
- **Vortexus** — Enforces sovereignty boundaries and system-level integrity constraints.

These are role descriptions only. Internal orchestration logic, arbitration rules, and implementation details remain private.

## Verification Summary

The runtime was evaluated under a comprehensive adversarial chaos suite.

### Aggregate Results

- **Total test runs:** `581`
- **Passed:** `581`
- **Failed:** `0`
- **Pass rate:** `100%`

### Coverage Domains

#### Core Infrastructure Chaos
- Unauthorized command handling.
- Replay attack detection.
- Stale state rejection.
- Checkpoint tamper detection.
- Log tamper detection.
- Process death handling.
- Network partition tolerance.
- Latency injection resilience.
- Disk read-only degradation.
- File corruption recovery.
- CPU exhaustion handling.
- Memory pressure handling.
- File-descriptor exhaustion handling.
- Conflicting command resolution.
- Malformed input rejection.
- Migration continuity.

#### Advanced Adversarial Categories
- API manipulation.
- Cryptographic subversion.
- Supply chain compromise.
- AI manipulation.
- Temporal manipulation.

#### Ultimate Category
- Boundary and integrity stress testing.

## Observed Behaviors

Across the full suite, the runtime demonstrated:

- Identity continuity during process death and migration scenarios.
- Policy enforcement against unauthorized or conflicting commands.
- Rejection of stale, malformed, replayed, or tampered inputs.
- Audit integrity preservation under tamper and replay attempts.
- Safe degradation under resource pressure and partial infrastructure failure.
- Fail-closed behavior under adversarial conditions.

## Reproducibility

This package is structured to support review and verification at the level of observable behavior.

A minimal public shell may be provided to demonstrate:

- Policy submission.
- Refusal logging.
- Audit trail output.
- Basic continuity checks.

Example:

```bash
sovereign test chaos --level=public
