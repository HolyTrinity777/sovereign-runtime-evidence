# Public Shell

This directory contains the minimal public shell for the Sovereign Runtime evidence package.

The shell is intentionally narrow. It is designed to demonstrate only observable behaviors such as:
- policy submission,
- refusal logging,
- audit trail output,
- and basic continuity checks.

It does not expose the private sovereign runtime core, internal orchestration logic, or protected defense mechanisms.

## Purpose

The purpose of the public shell is to provide a small, verifiable interface that supports:
- reproducibility,
- transparency,
- and public review of observable behavior.

## Expected behavior

A valid public shell should:

- Accept a limited configuration file.
- Expose a small command surface.
- Refuse unsafe or unauthorized actions.
- Emit audit-friendly output.
- Preserve continuity checks across simple runs.

## Example usage

```bash
./sovereign test chaos --level=public
