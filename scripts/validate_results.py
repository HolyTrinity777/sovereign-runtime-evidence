#!/usr/bin/env python3
import json
from pathlib import Path
import sys

summary_path = Path("metadata/chaos_live_summary.json")
results_path = Path("results/chaos_live_results.jsonl")

lines = results_path.read_text(encoding="utf-8").splitlines()
parsed = [json.loads(line) for line in lines if line.strip()]

total = len(parsed)
passed = sum(1 for x in parsed if x.get("status") == "passed")
failed = sum(1 for x in parsed if x.get("status") == "failed")

if total == 0:
    print("no results found")
    raise SystemExit(1)

if passed + failed != total:
    print("pass/fail totals do not add up")
    raise SystemExit(1)

if summary_path.exists():
    summary = json.loads(summary_path.read_text(encoding="utf-8") or "{}")
    s_total = summary.get("total", total)
    s_passed = summary.get("passed", passed)
    s_failed = summary.get("failed", failed)

    if (s_total, s_passed, s_failed) != (total, passed, failed):
        print(f"summary mismatch: summary={s_total}/{s_passed}/{s_failed} results={total}/{passed}/{failed}")
        raise SystemExit(1)

print("results validated")
raise SystemExit(0)
