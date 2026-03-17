# IRIS Clustering

> **📋 Teaching Repository** — This repo supports an in-class lesson on scaffolding a Python analysis project and coding with AI agents (GitHub Copilot). It demonstrates both K-means clustering fundamentals and project organization best practices.

**[📖 View Interactive Pages](pages/index.html)** — Browse documentation, project plan, and student handout as web pages.

---

From UCI

This is perhaps the best known database to be found in the pattern recognition literature. Fisher's paper is a classic in the field and is referenced frequently to this day. (See Duda & Hart, for example.) The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other.

Predicted attribute: class of iris plant.

Attribute Information:

1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:

0 -- Iris Setosa

1 -- Iris Versicolour

2 -- Iris Virginica

## Challenge

Import the Iris dataset and explore the data for structure without using the species (target) column.

## Development

This repository includes optional development tooling to help keep code style and complexity within project standards. See `BEST_PRACTICES.md` for more detail.

Setup (recommended):

1. Create and activate a virtual environment.
2. Install runtime dependencies:

```powershell
pip install -r requirements.txt
```

1. Install development dependencies:

```powershell
pip install -r requirements-dev.txt
```

Run quality checks:

- On Windows PowerShell:

```powershell
./scripts/quality_check.ps1
```

- On macOS / Linux:

```bash
./scripts/quality_check.sh
```

Formatting and linting (individual commands):

```bash
isort .
black .
flake8 .
```

Running tests:

```bash
pytest
```

See `BEST_PRACTICES.md` for coding standards and complexity targets.
