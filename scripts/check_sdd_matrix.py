#!/usr/bin/env python
from pathlib import Path
import sys

REQUIRED = [
    'docs/sdd/templates/04_requirements.md',
    'docs/sdd/templates/05_spec_sources.md',
    'docs/sdd/templates/08_adr.md',
    'docs/sdd/templates/11_test_strategy.md',
    'docs/sdd/templates/12_operations.md',
    'docs/sdd/templates/13_release_change_management.md',
]


def main() -> int:
    root = Path('.').resolve()
    missing = [p for p in REQUIRED if not (root / p).exists()]
    if missing:
        print('Missing required SDD docs:')
        for m in missing:
            print(f'- {m}')
        return 1
    print('SDD doc matrix baseline check: OK')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
