#!/usr/bin/env python3
import json
from pathlib import Path

results_path = Path("results/chaos_live_results.json")
summary_path = Path("metadata/chaos_live_summary.json")

rows = []
for line in results_path.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if line:
        rows.append(json.loads(line))

total = len(rows)
passed = 0
failed = 0
unknown = []

for i, row in enumerate(rows, 1):
    if not isinstance(row, dict):
        unknown.append((i, type(row).__name__))
        continue

    if "pass" in row and isinstance(row["pass"], bool):
        if row["pass"]:
            passed += 1
        else:
            failed += 1
    else:
        unknown.append((i, row.get("pass")))

if unknown:
    print("unknown or missing pass values found:")
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
