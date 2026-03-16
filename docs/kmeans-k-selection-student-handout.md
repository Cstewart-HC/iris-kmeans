# K-Means K Selection on Iris: Student Handout

## What You Should Learn
By the end of this lesson, you should be able to:
1. Explain why choosing K in K-means is model selection, not a fixed rule.
2. Interpret multiple unsupervised metrics for K selection.
3. Explain why different metrics can suggest different K values.
4. Defend a final K with transparent evidence.

## Big Idea
There is no universally correct K.
A strong workflow compares multiple unsupervised signals and documents the choice.

On Iris, two outcomes can both be reasonable:
- silhouette-only can suggest K=2
- multi-metric consensus can suggest K=3

## Metrics You Need to Know

### 1) Inertia (Elbow)
- Measures within-cluster squared distance.
- Lower is better.
- Since inertia always decreases as K increases, use elbow shape, not minimum value.

### 2) Silhouette
- Measures cohesion and separation.
- Higher is better.
- Can prefer coarse splits such as one-vs-rest structure.

### 3) Calinski-Harabasz
- Ratio of between-cluster to within-cluster dispersion.
- Higher is better.

### 4) Davies-Bouldin
- Similarity of each cluster with the most similar other cluster.
- Lower is better.

### 5) Cluster-Balance Entropy
- Measures whether cluster sizes are balanced.
- Higher is better.
- Helps avoid trivial lopsided splits.

### 6) Seed Stability (diagnostic)
- Measures sensitivity to random initialization.
- Lower standard deviation is better.
- Used as evidence, not as the only decision rule.

## Decision Policy Used in Class
1. Evaluate K from 2 to 8.
2. Keep silhouette-only best K as baseline.
3. Rank each metric with proper direction.
4. Sum metric ranks.
5. Take the K values with best rank sum.
6. Use elbow as tie-break when possible.
7. Report both baseline K and final consensus K.

## Why This Matters
A single metric can miss structure.
A multi-metric decision is usually more robust and easier to defend.

## Common Mistakes
1. Treating one metric as absolute truth.
2. Using wrong metric direction (higher vs lower).
3. Hiding baseline results after using advanced methods.
4. Using label-based metrics to choose K during unsupervised training.

## Reflection Questions
1. Why might silhouette prefer K=2 on Iris?
2. Which metric in class most strongly supported K=3?
3. If metrics disagree, what tie-break rule is most defensible?
4. How would your policy change for imbalanced real-world data?

## Exit Ticket Prompt
Using only unsupervised evidence, justify your chosen K for Iris in 5 to 8 sentences.
Include:
- at least three metrics
- one caveat
- one tie-break rationale
