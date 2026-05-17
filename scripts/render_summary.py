#!/usr/bin/env python3
import json
from pathlib import Path


def main():
    summary_path = Path("metadata/chaos_live_summary.json")
    summary = json.loads(summary_path.read_text(encoding="utf-8"))

    total = summary.get("total", 0)
    passed = summary.get("passed", 0)
    failed = summary.get("failed", 0)
    rate = (passed / total * 100) if total else 0

    md = f"""# Chaos Summary

- Total: {total}
- Passed: {passed}
- Failed: {failed}
- Pass rate: {rate:.2f}%
"""

    out = Path("results/summary.md")
    out.write_text(md, encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
