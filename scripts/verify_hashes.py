#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="metadata/sovereignty_chaos_dataset_manifest.json")
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    files = manifest.get("files", [])
    all_ok = True

    for item in files:
        rel = item["path"]
        expected = item["sha256"]
        actual = sha256_file(Path(rel))
        ok = actual == expected
        print(f"{rel}: {'OK' if ok else 'MISMATCH'}")
        if not ok:
            print(f"  expected: {expected}")
            print(f"  actual:   {actual}")
            all_ok = False

    raise SystemExit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
