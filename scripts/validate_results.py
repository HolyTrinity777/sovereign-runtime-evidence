#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def main():
    summary_path = Path("metadata/chaos_live_summary.json")
    results_path = Path("results/chaos_live_results.jsonl")

    summary = json.loads(summary_path.read_text(encoding="utf-8"))

    total = summary.get("total", 0)
    passed = summary.get("passed", 0)
    failed = summary.get("failed", 0)

    lines = results_path.read_text(encoding="utf-8").splitlines()
    parsed = [json.loads(line) for line in lines if line.strip()]

    if len(parsed) != total:
        print(f"count mismatch: summary={total} results={len(parsed)}")
        raise SystemExit(1)

    if passed + failed != total:
        print("pass/fail totals do not add up")
        raise SystemExit(1)

    actual_passed = sum(1 for x in parsed if x.get("status") == "passed")
    actual_failed = sum(1 for x in parsed if x.get("status") == "failed")

    if actual_passed != passed or actual_failed != failed:
        print("status counts do not match summary")
        raise SystemExit(1)

    print("results validated")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
