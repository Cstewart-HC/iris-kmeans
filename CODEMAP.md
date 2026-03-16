# IRIS Clustering — Code Map

This file maps the main files and folders in this project and explains their purpose.

- `README.md`: Project overview and challenge description.
- `CODEMAP.md`: This file — maps files and responsibilities.
- `STRUCTURE.md`: Human-readable directory tree and intended contents.
- `copilot-instructions.md`: Repository-specific instructions for AI assistants and contributors.
- `requirements.txt`: Minimal Python dependencies to get started.
- `.gitignore`: Common Python ignores.
- `data/`: Dataset storage (raw and processed).
- `notebooks/`: Exploration and analysis Jupyter notebooks.
- `src/`: Python package containing analysis and helper modules.
- `tests/`: Unit and integration tests.

Additional files added for project standards and quality checks:

- `BEST_PRACTICES.md`: Repository-specific Python best-practices and how-to checks.
- `.editorconfig`: Editor settings (UTF-8, 4 spaces, max line length 80).
- `.flake8`: Flake8 configuration (80-char limit and complexity hints).
- `pyproject.toml`: Black and isort configuration for 80-char formatting.
- `scripts/quality_check.sh`: Convenience script to run linters and complexity checks.

Suggested next tasks:
- Add an exploratory notebook in `notebooks/` that imports the Iris dataset.
- Implement a simple clustering script in `src/` and add a runnable entrypoint.
- Add CI configuration to run tests and linting.
