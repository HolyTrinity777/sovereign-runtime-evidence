#!/usr/bin/env python3
import json
from pathlib import Path

results_path = Path("results/chaos_live_results.jsonl")
summary_path = Path("metadata/chaos_live_summary.json")

lines = results_path.read_text(encoding="utf-8").splitlines()
parsed = [json.loads(line) for line in lines if line.strip()]

total = len(parsed)
passed = 0
failed = 0
unknown = []

for i, row in enumerate(parsed, 1):
    status = str(row.get("status", "")).strip().lower()
    if status in {"passed", "pass", "ok", "success"}:
        passed += 1
    elif status in {"failed", "fail", "error", "rejected"}:
        failed += 1
    else:
        unknown.append((i, row.get("status")))

if unknown:
    print("unknown status values found:")
    for line_no, value in unknown[:10]:
        print(f"  line {line_no}: {value!r}")
    raise SystemExit(1)

if passed + failed != total:
    print("pass/fail totals do not add up")
    print(f"total={total} passed={passed} failed={failed}")
    raise SystemExit(1)

if summary_path.exists():
    summary = json.loads(summary_path.read_text(encoding="utf-8") or "{}")
    if summary.get("total") not in {None, total}:
        print(f"summary mismatch: summary total={summary.get('total')} results total={total}")
        raise SystemExit(1)

print("results validated")
