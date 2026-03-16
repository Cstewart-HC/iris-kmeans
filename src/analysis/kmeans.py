"""KMeans fitting and scoring helpers."""

from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List
from typing import Sequence
from typing import Tuple

import numpy as np
from scipy.optimize import linear_sum_assignment
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics import calinski_harabasz_score
from sklearn.metrics import classification_report
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import normalized_mutual_info_score
from sklearn.metrics import silhouette_score
from sklearn.metrics import v_measure_score


def fit_kmeans(
    features: np.ndarray,
    n_clusters: int,
    random_state: int = 42,
    n_init: int = 20,
) -> KMeans:
    """Fit and return a deterministic KMeans model."""
    model = KMeans(
        n_clusters=n_clusters,
        random_state=random_state,
        n_init=n_init,
    )
    model.fit(features)
    return model


def score_kmeans(
    features: np.ndarray,
    labels: Sequence[int],
) -> Dict[str, float]:
    """Compute unsupervised clustering quality metrics."""
    labels_array = np.asarray(labels)
    unique_labels = np.unique(labels_array)
    if unique_labels.size < 2:
        msg = "At least two clusters are required to compute scores."
        raise ValueError(msg)

    return {
        "silhouette": float(silhouette_score(features, labels_array)),
        "calinski_harabasz": float(
            calinski_harabasz_score(features, labels_array)
        ),
        "davies_bouldin": float(davies_bouldin_score(features, labels_array)),
    }


def _build_cost_matrix(
    y_true: np.ndarray,
    cluster_labels: np.ndarray,
) -> Tuple[np.ndarray, List[int], List[int]]:
    classes = np.unique(y_true)
    clusters = np.unique(cluster_labels)
    cost = np.zeros((clusters.size, classes.size), dtype=int)

    for i, cluster in enumerate(clusters):
        for j, cls in enumerate(classes):
            matches = (cluster_labels == cluster) & (y_true == cls)
            cost[i, j] = -int(np.sum(matches))

    return cost, clusters.tolist(), classes.tolist()


def map_clusters_to_labels(
    y_true: Sequence[int],
    cluster_labels: Sequence[int],
) -> np.ndarray:
    """Map cluster ids to class labels using Hungarian assignment."""
    y_true_array = np.asarray(y_true)
    cluster_array = np.asarray(cluster_labels)
    cost, clusters, classes = _build_cost_matrix(y_true_array, cluster_array)
    row_ind, col_ind = linear_sum_assignment(cost)
    mapping = {clusters[r]: classes[c] for r, c in zip(row_ind, col_ind)}
    default_label = classes[0]
    mapped = [mapping.get(label, default_label) for label in cluster_array]
    return np.array(mapped)


def posthoc_label_metrics(
    y_true: Sequence[int],
    cluster_labels: Sequence[int],
    digits: int = 3,
) -> Dict[str, Any]:
    """Compute post-hoc target-aware clustering metrics.

    These metrics are for evaluation only and must not be used to tune model
    parameters during fitting.
    """
    y_true_array = np.asarray(y_true)
    cluster_array = np.asarray(cluster_labels)
    aligned_labels = map_clusters_to_labels(y_true_array, cluster_array)

    report = classification_report(
        y_true_array,
        aligned_labels,
        output_dict=True,
        digits=digits,
        zero_division=0,
    )
    return {
        "adjusted_rand_index": float(
            adjusted_rand_score(y_true_array, cluster_array)
        ),
        "normalized_mutual_info": float(
            normalized_mutual_info_score(y_true_array, cluster_array)
        ),
        "v_measure": float(v_measure_score(y_true_array, cluster_array)),
        "mapped_accuracy": float(report["accuracy"]),
        "mapped_macro_precision": float(report["macro avg"]["precision"]),
        "mapped_macro_recall": float(report["macro avg"]["recall"]),
        "mapped_macro_f1": float(report["macro avg"]["f1-score"]),
        "mapped_classification_report": report,
    }
