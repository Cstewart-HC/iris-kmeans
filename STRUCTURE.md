# Project Structure

Top-level layout (intended):

- README.md — project overview
- CODEMAP.md — mapping of files and purposes
- STRUCTURE.md — this file
- copilot-instructions.md — contributor/assistant guidance
- requirements.txt — python dependencies
- .gitignore
- data/
  - raw/ — original dataset files (CSV, ZIP)
  - processed/ — cleaned/feature-engineered data
- notebooks/
  - 01-explore-iris.ipynb — exploratory analysis (starter)
- src/
  - __init__.py
  - analysis/ — modules for clustering and evaluation
  - utils/ — data loading and helper functions
- tests/ — unit tests

Notes:
- Place raw downloads in `data/raw/` and keep processed artifacts in `data/processed/`.
- Use notebooks for exploration; production code should live in `src/`.
