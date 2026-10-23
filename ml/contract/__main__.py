"""`python3 -m ml.contract` — regenerate the JSON Schema exports."""
from __future__ import annotations

from ml.contract import export_schemas

if __name__ == "__main__":
    path = export_schemas()
    print(f"wrote ML contract schemas to {path}")
