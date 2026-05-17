# Sovereign Runtime — Public Evidence Package v0.1

![Version](https://img.shields.io/badge/version-v0.1-blue)
![Status](https://img.shields.io/badge/status-public_evidence_package-success)
![Pass Rate](https://img.shields.io/badge/pass_rate-581%2F581%20(100%25)-brightgreen)
![Scope](https://img.shields.io/badge/scope-7%20agents%20%7C%2021%20fault%20categories%20%7C%20581%20runs-informational)

This repository contains the public evidence package for a 7-agent sovereign actor runtime designed for bounded digital sovereignty. It documents high-level architecture, test methodology, aggregate results, and reproducible public artifacts without disclosing private orchestration internals.

---

## Purpose

This repository provides a public evidence package for review, verification, and transparency. It is intended to document observable behavior, test structure, and aggregate results while keeping private implementation details excluded.

---

## Contents

- `result.json` — Aggregated results and metadata.
- `tests_dataset.csv` — Tabular test dataset.
- `tests_dataset.json` — Structured JSON test dataset.
- `screenshot-1.png` — Terminal output of the completed run, part 1.
- `screenshot-2.png` — Terminal output of the completed run, part 2.
- `CHAOS_SUITE.md` — Test categories, methodology, and success criteria.
- `public-shell/` — Minimal observable-behavior shell for independent verification.
- `scripts/` — Hash verification, result validation, and summary rendering tools.
- `metadata/` — Manifest and integrity hashes for published artifacts.

---

## System Overview

The runtime is organized around seven public roles that support coordination, recovery, safety, and continuity:

- **Consensus** — Supports coordinated decision-making.
- **Healer** — Supports recovery and restoration.
- **Anxiarch** — Supports detection and policy oversight.
- **Destroyer** — Supports isolation of compromised components.
- **Limbrix** — Supports resource management and restraint.
- **Preaxis** — Supports continuity across restart and migration events.
- **Vortexus** — Supports boundary and integrity protection.

*These descriptions are intentionally high level. The internal implementation, decision rules, and operational details are not disclosed in this repository.*

---

## Verification Summary

The runtime was evaluated under a comprehensive adversarial chaos suite covering 21 distinct fault categories across all 7 agents.

### Aggregate Results

| Metric | Value |
|---|---|
| Total test runs | 581 |
| Passed | 581 |
| Failed | 0 |
| Pass rate | 100% |

### Coverage Domains

**Core Infrastructure Chaos**
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

**Advanced Adversarial Categories**
- API manipulation.
- Cryptographic subversion.
- Supply chain compromise.
- AI manipulation.
- Temporal manipulation.

**Ultimate Category**
- Boundary and integrity stress testing.

---

## Observed Behaviors

Across the full suite, the runtime consistently demonstrated:

- Identity continuity during process death and migration scenarios.
- Policy enforcement against unauthorized or conflicting commands.
- Rejection of stale, malformed, replayed, or tampered inputs.
- Audit integrity preservation under tamper and replay attempts.
- Safe degradation under resource pressure and partial infrastructure failure.
- Fail-closed behavior under adversarial conditions.

---

## Limitations

- This repository publishes the public evidence layer only.
- Internal orchestration logic, arbitration rules, and private implementation details are intentionally excluded.
- The public artifacts support verification of observable behavior, not full system reproduction.
- The reported results reflect the defined test scope and the controlled conditions under which the suite was executed.
- Single-node execution model; distributed deployment behavior is not covered in this release.

---

## Reproducibility

The public evidence package is structured to support independent review and verification at the level of observable behavior.

A minimal public shell is included in the `/public-shell` directory. It exposes only the observable surface of the runtime:
- Policy submission.
- Refusal logging.
- Audit trail output.
- Basic continuity checks.

To verify the published artifacts:

```bash
python scripts/verify_hashes.py
python scripts/validate_results.py
python scripts/render_summary.py
```

**All artifact hashes are documented in  metadata/ . Reviewers should verify file integrity independently before analysis.**

## License and Access

*This repository is governed by the Sovereign Runtime Public Evidence Package License, Version 1.2.*

The materials are released solely for independent verification of observable behavior under controlled fault-injection conditions. This is not an open-source release. No rights are granted beyond those explicitly stated in the license. Commercial use, redistribution, AI/ML training use, or any access beyond the stated public rights requires prior written permission from the Copyright Holder.
**See  LICENSE  for full terms.**

## Private Access and NDA

The private sovereign runtime core is not included in this repository. It is maintained separately. Access to private materials, internal architecture, implementation details, or commercial review is available only under NDA or separate written agreement.
For inquiries, contact the Copyright Holder directly.
