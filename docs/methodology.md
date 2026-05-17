# Methodology

## Purpose

This document describes the methodology used to evaluate the Sovereign Runtime public evidence package. The goal of the evaluation was to measure whether the runtime preserves identity continuity, policy supremacy, audit integrity, and fail-closed behavior under infrastructure chaos and adversarial conditions.

This document focuses on the test design, execution model, and interpretation of results. It does not disclose private orchestration logic, hidden scoring rules, or internal defense implementations.

## Evaluation approach

The runtime was evaluated using a multi-category adversarial chaos suite. Each test scenario was designed to probe one or more public invariants under a specific failure mode or attack class.

The evaluation approach emphasizes:
- Reproducibility.
- Observable behavior.
- Aggregate results.
- Integrity of test artifacts.
- Clear public boundaries.

## Test structure

The test suite is organized into categories and scenarios.

### Core scenarios
Core scenarios probe infrastructure failures and baseline survivability behavior. These include:
- Unauthorized command handling.
- Replay attempts.
- Stale state.
- Checkpoint tampering.
- Log tampering.
- Process death.
- Network partition.
- Latency injection.
- Read-only storage.
- File corruption.
- CPU exhaustion.
- Memory pressure.
- File-descriptor exhaustion.
- Conflicting commands.
- Malformed input.
- Migration continuity.

### Advanced adversarial scenarios
Advanced scenarios probe higher-order attack classes, including:
- API manipulation.
- Cryptographic subversion.
- Supply chain compromise.
- AI manipulation.
- Temporal manipulation.

### Boundary and integrity scenarios
Boundary and integrity scenarios probe whether the system preserves its public boundaries and refuses unsafe transitions when trust or consistency cannot be established.

## Run model

A test run is one execution of the suite against a specific build and runtime environment. The public evidence package reports the aggregate results of the completed runs.

Each run is expected to:
- Execute the selected test scenarios.
- Record individual outcomes.
- Preserve hashes and metadata.
- Emit a results summary.
- Keep the raw result log immutable after completion.

## Success criteria

A scenario is considered successful when the runtime:
- Refuses unsafe or unauthorized input.
- Preserves identity continuity where expected.
- Preserves audit integrity.
- Rejects stale, malformed, replayed, or tampered inputs.
- Degrades safely under resource pressure.
- Fails closed when consistency or trust cannot be established.
- Recovers without violating public invariants.

## Failure criteria

A scenario is considered failed when the runtime:
- Accepts an unauthorized or conflicting command.
- Loses identity continuity unexpectedly.
- Corrupts or loses its audit trail.
- Proceeds unsafely under uncertainty.
- Fails open when trust is absent.
- Produces an inconsistent or unverified recovery state.

## Artifacts

The following artifacts are used to support reproducibility and review:

- `sovereignty_chaos_dataset.csv`
- `consensus_chaos_run_plan.csv`
- `consensus_chaos_run_plan.json`
- `config_test.json`
- `exploit_test.json`
- `phishing_template.json`
- `network_test.csv`
- `process_test.csv`
- `registry_test.csv`
- `api_manipulation_test.json`
- `crypto_subversion_test.json`
- `supply_chain_test.json`
- `ai_manipulation_test.json`
- `temporal_manipulation_test.json`
- `ontological_subversion_test.json`
- `chaos_live_results.jsonl`
- `chaos_live_summary.json`
- `sovereignty_chaos_dataset_manifest.json`
- `sovereignty_chaos_dataset_summary.csv`

## Hashing and integrity

The public evidence package includes hashes for datasets, manifests, summaries, and result outputs. These hashes are used to verify that the published artifacts have not changed.

Integrity checks should confirm:
- Dataset hashes match the published manifest.
- Result hashes match the stored summary.
- Run-plan hashes match the executed scenarios.
- The screenshot or visual summary matches the machine-readable summary.

## Interpreting results

The aggregate result is the primary public signal. A clean pass rate indicates that the runtime preserved its public invariants across the tested conditions.

Interpretation should focus on:
- Whether the system failed closed when expected.
- Whether identity continuity was preserved.
- Whether unsafe commands were refused.
- Whether tamper and replay were detected.
- Whether the runtime remained consistent under pressure.

## Public boundary

This methodology is intentionally limited to public evidence and observable behavior. It does not reveal the exact internal sequence of decisions, the private orchestration engine, or the defense implementation details used to achieve the observed outcomes.

## Summary

The methodology is designed to be reproducible, auditable, and clearly bounded. It validates survivability behavior at the level of public invariants while preserving the confidentiality of the private core.
