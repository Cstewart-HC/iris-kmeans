# Python Best Practices — tailored for IRIS Clustering project

This repository is a small analysis project (see `README.md`) focused on exploring the Iris dataset. The following recommended standards are intentionally simple and tool-agnostic so they work across environments.

Standards applied here

- PEP 8 style for Python formatting.
- Maximum line length: 80 characters for function bodies and module-level code.
- Cognitive complexity: aim for <= 7 per function. Prefactor by refactoring large functions into smaller helpers.

Quick guidance

- Keep functions short and focused: single responsibility makes testing and reasoning easier.
- Add concise docstrings to public functions and modules using the one-line summary + optional details format.
- Use explicit imports and avoid wildcard imports.
- Prefer typed function signatures (type hints) for public APIs and non-trivial helpers.
- Prefer pure functions where reasonable; isolate side-effects (I/O, plotting) behind small adapter functions.
- Add unit tests for key data transformations and clustering behavior.

Tools and how to run checks

- Formatting: `black .` (configured to 80 chars in `pyproject.toml`).
- Import sorting: `isort .` (profile "black" set in `pyproject.toml`).
- Linting: `flake8 .` (configuration in `.flake8` — includes complexity thresholds if plugins installed).
- Cognitive complexity: use `radon` or `lizard` to inspect function complexity. Example:

```
pip install radon
radon cc -s -a src
```

`radon cc` reports cyclomatic complexity; for cognitive complexity you can use `lizard` or the `radon` cognitive-complexity plugin if available. Aim to refactor functions with reported complexity above 7.

Suggested workflow

1. Run `scripts/quality_check.sh` (or run tools individually) before committing.
2. Fix formatting errors via `black` and `isort`.
3. Address flake8 and complexity warnings next (refactor large functions into smaller ones).

Notes

- These files provide guidance and automation helpers but do not enforce installations. Add CI or pre-commit hooks later to automate checks.
