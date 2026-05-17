# Invariants

## Purpose

This document defines the public invariants that the Sovereign Runtime is expected to preserve under normal operation and under adversarial conditions. These invariants are part of the public evidence package and are used to evaluate the runtime’s survivability behavior.

## Core invariants

### 1. Identity continuity
The runtime must preserve identity across restart, migration, and partial failure events. A disruption must not cause the system to lose or replace its identity state unexpectedly.

### 2. Policy supremacy
Unauthorized or conflicting commands must not override the runtime’s governing policy. When a command violates policy, the runtime must refuse it.

### 3. Audit integrity
All important actions must remain auditable. Tamper, replay, or log corruption must not silently invalidate the audit trail.

### 4. Fail-closed behavior
If the runtime cannot establish trust or consistency, it must stop or refuse rather than proceed unsafely. Failure must be safe by default.

### 5. Safe degradation
When resources are constrained or unavailable, the runtime must reduce capability without violating integrity, policy, or identity continuity.

### 6. Recovery consistency
Recovery after failure must restore a valid and internally consistent state. Recovery must not create hidden divergence or inconsistent checkpoints.

### 7. Boundary enforcement
The runtime must preserve the boundary between public behavior and protected internals. Public interfaces must remain narrow and auditable.

### 8. Deterministic verification surface
The public evidence package must provide stable artifacts that can be checked independently, including datasets, hashes, and summary results.

## What these invariants mean in practice

These invariants are observable at the boundary. A valid implementation should be able to demonstrate that it:

- Rejects stale or replayed inputs.
- Rejects malformed or unauthorized commands.
- Preserves state across migration and restart.
- Detects tamper and corruption.
- Continues safely during partition or pressure.
- Refuses to expose protected implementation details.

## Relationship to test results

The chaos suite is designed to validate these invariants across many failure modes. Each test category probes one or more of the invariants above. A clean pass across the suite indicates that the runtime maintained its public guarantees under the tested conditions.

## Scope

These invariants are public statements about the system’s expected behavior. They do not describe the internal logic used to achieve the behavior.

## Summary

The public value of the runtime is not just that it performs tasks, but that it preserves trust under stress. These invariants define what “survival” means for the system in practical, testable terms.
