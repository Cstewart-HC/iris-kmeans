# K-Means K Selection on Iris: Instructor Guide

## Teaching Goal
Help students understand that K selection is a policy choice under uncertainty, not a single-metric rule.

Primary notebook: notebooks/01-explore-iris.ipynb

## Lesson Plan (40 to 50 minutes)
1. Framing and objectives: 5 min
2. Silhouette-only baseline: 7 min
3. Multi-metric consensus: 12 min
4. Stability and structure checks: 8 min
5. Final fit and interpretation: 8 to 15 min

## Instructor Walkthrough by Notebook Cell Number
1. Cells 1 to 7
- Setup, loading, and preprocessing.

2. Cell 8 (core teaching cell)
- Show silhouette-only K.
- Show consensus K.
- Show elbow K and tied set.
- Walk through the metrics table.

3. Cell 9
- Explain visual evidence:
  - inertia elbow
  - silhouette curve
  - Calinski-Harabasz and cluster balance
  - Davies-Bouldin
  - seed stability diagnostic

4. Cell 10
- PCA projection without labels.

5. Cell 11
- Fit final model with consensus K.

6. Cells 12 to 13
- Visualize clusters and show post-hoc diagnostics.

7. Cell 14
- Recap policy and limitations.

## Suggested Script (Use Verbatim if Helpful)
First, we apply the common method: choose K from silhouette. On Iris, that often gives K equals 2. This is not wrong. It reflects a strong coarse separation pattern.

Second, we broaden the evidence. We add Calinski-Harabasz, Davies-Bouldin, elbow structure, and cluster-balance entropy. We rank each metric, combine ranks, and pick a consensus K.

Now we often get K equals 3, which aligns with the classic three-group interpretation in Iris. We are not forcing a target answer. We are using a richer unsupervised decision policy.

Most important, we keep silhouette-only output visible to stay transparent.

## Key Concepts to Emphasize
1. Metric disagreement is expected.
2. Every metric has assumptions and blind spots.
3. Transparency is part of scientific quality.
4. Post-hoc label metrics are for evaluation, not unsupervised selection.

## In-Class Exercise (10 minutes)
Have students test one policy change each:
1. Remove cluster-balance from rank sum.
2. Double Davies-Bouldin rank weight.
3. Change tie-break from elbow-first to smallest-K or largest-K.

Debrief prompts:
- Did final K change?
- Which policy is most defensible scientifically?
- Which policy is easiest to communicate to non-technical stakeholders?

## Discussion Questions
1. Why can silhouette prefer K equals 2 on Iris?
2. Which metrics most strongly support K equals 3 and why?
3. Should stability be hard-gated or diagnostic only?
4. What tie-break policy should your team standardize on?

## Assessment Prompt
Using only unsupervised evidence, justify your final K for Iris in 5 to 8 sentences.
Require:
- at least three metrics
- one caveat
- one tie-break explanation

## Grading Rubric (Quick)
- Evidence quality: 40%
- Correct metric interpretation: 30%
- Decision transparency: 20%
- Clarity and structure: 10%
