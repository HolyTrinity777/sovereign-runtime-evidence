#!/usr/bin/env python3
import json
from pathlib import Path

results_path = Path("results/chaos_live_results.json")
summary_path = Path("metadata/chaos_live_summary.json")

data = json.loads(results_path.read_text(encoding="utf-8"))

if isinstance(data, dict):
    rows = data.get("results", [])
    summary = data.get("summary", {})
elif isinstance(data, list):
    rows = data
    summary = {}
else:
    raise SystemExit("unsupported JSON structure")

total = len(rows)
passed = 0
failed = 0
unknown = []

for i, row in enumerate(rows, 1):
    if isinstance(row, dict):
        status = str(row.get("status", "")).strip().lower()
        if status in {"passed", "pass", "ok", "success"}:
            passed += 1
        elif status in {"failed", "fail", "error", "rejected"}:
            failed += 1
        else:
            unknown.append((i, row.get("status")))
    else:
        unknown.append((i, type(row).__name__))

if unknown:
    print("unknown result values found:")
    for line_no, value in unknown[:10]:
        print(f"  item {line_no}: {value!r}")
    raise SystemExit(1)

if passed + failed != total:
    print("pass/fail totals do not add up")
    print(f"total={total} passed={passed} failed={failed}")
    raise SystemExit(1)

if summary_path.exists():
    meta = json.loads(summary_path.read_text(encoding="utf-8") or "{}")
    if meta.get("total") not in {None, total}:
        print(f"summary mismatch: summary total={meta.get('total')} results total={total}")
        raise SystemExit(1)

print("results validated")
