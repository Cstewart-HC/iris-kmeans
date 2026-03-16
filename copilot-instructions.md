# Copilot / Assistant Instructions

Purpose: Provide repository-specific guidance for GitHub Copilot, AI assistants, and contributors.

Project goal
- Explore the Iris dataset (UCI) and perform unsupervised clustering, visualization, and evaluation without using the target column during analysis.

Environment
- Python 3.10+ recommended.
- Create a virtual environment and install dependencies from `requirements.txt`.

Commands
- Create venv and install:

  python -m venv .venv
  .\.venv\Scripts\activate
  pip install -r requirements.txt

Conventions for code and PRs
- Keep exploratory work in `notebooks/` and production-ready code in `src/`.
- Write small, focused commits with descriptive messages.
- Add tests in `tests/` for any non-trivial logic.

- Code size and complexity limits:
  - **Maximum function length:** 80 lines (excluding docstrings and blank lines).
  - **Maximum cognitive complexity:** 7 per function. Use static analysis tools (e.g., `radon cc` or `flake8` plugins) to measure and enforce this limit.

Assistant policies for this repo
- When modifying files, prefer minimal, focused changes and preserve existing style.
- Add or update tests when implementing new functionality.
- Do not commit raw data files larger than a few MB — if needed, reference their source and keep them in `data/raw/`.

Suggested first tasks for contributors or assistants
- Add `notebooks/01-explore-iris.ipynb` that loads the Iris dataset and performs PCA and pairwise plots (without the target).
- Add `src/analysis/cluster.py` with a `run_kmeans()` function and a CLI or notebook-friendly API.
