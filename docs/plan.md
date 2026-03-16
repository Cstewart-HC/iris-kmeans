## Plan: Bootstrap Iris KMeans Project

Last updated: 2026-03-16

Create the missing project scaffolding and a first exploration notebook that loads Iris via scikit-learn, performs unsupervised clustering (no target leakage), and reports both unsupervised metrics and clearly-post-hoc target-based metrics.

**Steps**
1. Repo sanity check: confirm Python version target (3.10+), confirm tooling configs (.editorconfig/.flake8/pyproject.toml) align with 80-char formatting and complexity limits.
2. Create intended folders (empty placeholders ok): data/raw, data/processed, notebooks, src/analysis, src/utils, tests.
3. Notebook 01: data load + EDA (no target)
   - Load features with sklearn.datasets.load_iris(as_frame=True); keep target separate.
   - Basic EDA: shape, missingness, summary stats, pairplot without hue, correlation heatmap.
4. Notebook 01: preprocessing and dimensionality reduction
   - Standardize features (e.g., StandardScaler).
   - PCA for visualization; plot PC1/PC2 scatter WITHOUT using target; optionally color by cluster labels.
   - Persist any derived artifacts only if needed (prefer ephemeral in notebook initially).
5. Notebook 01: clustering (no target leakage)
   - Fit KMeans across a small K range; choose K via elbow + silhouette.
   - Keep fitting strictly on feature matrix only.
6. Metrics/reporting
   - Unsupervised: silhouette score, Calinski–Harabasz, Davies–Bouldin.
   - Post-hoc (explicitly after fitting): ARI, NMI/V-measure; if “accuracy/precision” desired, map cluster ids to true labels via optimal assignment (Hungarian) then compute classification report.
   - Clearly label post-hoc metrics as evaluation-only; never use target to select preprocessing params.
7. Production code extraction (after notebook proves approach)
   - Add src/utils/data.py (load_iris_features()), src/analysis/kmeans.py (fit_kmeans(), score_kmeans()), and keep notebook calling these helpers.
   - Add a small CLI entrypoint (optional) once functions stabilize.
8. Tests (minimal but meaningful)
   - Test loader returns expected shape/columns.
   - Test clustering functions are deterministic given random_state and return expected types.
9. Verification
   - Run scripts/quality_check.ps1 (Windows) and pytest; ensure flake8 cognitive complexity stays <= 7 per function.

**Relevant files**
- README.md — keep as-is; optionally add a short “How to run notebook” section.
- STRUCTURE.md / CODEMAP.md — update only if folder/file names diverge.
- requirements.txt / requirements-dev.txt — validate versions; adjust if installation issues.
- scripts/quality_check.ps1 / scripts/quality_check.sh — already good; use for verification.
- src/__init__.py — fine; add package exports only if useful later.

**Verification**
1. Create venv; install requirements and requirements-dev.
2. Launch Jupyter and run notebooks/01-explore-iris.ipynb end-to-end.
3. Run scripts/quality_check.ps1 and pytest.

**Decisions**
- Data source: scikit-learn load_iris (no raw file commits).
- Metrics: include unsupervised + post-hoc target-based metrics; emphasize label mapping for “accuracy/precision” style reporting.
- No target leakage: target never used in fitting, scaling, PCA fitting, or K selection; only in post-hoc reporting.

**Further Considerations**
1. KMeans reproducibility: set random_state and n_init explicitly.
2. Notebook output policy: decide whether to commit executed notebooks or keep them clean (no outputs).
