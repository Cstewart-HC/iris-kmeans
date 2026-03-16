"""Tests for KMeans analysis helpers."""

import numpy as np
from sklearn.preprocessing import StandardScaler

from src.analysis.kmeans import fit_kmeans
from src.analysis.kmeans import posthoc_label_metrics
from src.analysis.kmeans import score_kmeans
from src.utils.data import load_iris_features


def _scaled_iris() -> tuple[np.ndarray, np.ndarray]:
    features, target = load_iris_features()
    scaled = StandardScaler().fit_transform(features)
    return scaled, target.to_numpy()


def test_fit_kmeans_is_deterministic() -> None:
    """Repeated fits with same random state should produce same labels."""
    features, _ = _scaled_iris()

    model_one = fit_kmeans(features, n_clusters=3, random_state=7)
    model_two = fit_kmeans(features, n_clusters=3, random_state=7)

    assert np.array_equal(model_one.labels_, model_two.labels_)


def test_score_kmeans_returns_expected_keys_and_types() -> None:
    """Unsupervised scores should be floats with expected names."""
    features, _ = _scaled_iris()
    labels = fit_kmeans(features, n_clusters=3, random_state=7).labels_
    scores = score_kmeans(features, labels)

    assert set(scores.keys()) == {
        "silhouette",
        "calinski_harabasz",
        "davies_bouldin",
    }
    assert all(isinstance(value, float) for value in scores.values())


def test_posthoc_metrics_contains_main_metrics() -> None:
    """Post-hoc metrics should include both clustering and mapped metrics."""
    features, y_true = _scaled_iris()
    labels = fit_kmeans(features, n_clusters=3, random_state=7).labels_
    metrics = posthoc_label_metrics(y_true=y_true, cluster_labels=labels)

    assert {
        "adjusted_rand_index",
        "normalized_mutual_info",
        "v_measure",
        "mapped_accuracy",
    }.issubset(metrics.keys())
    assert isinstance(metrics["mapped_classification_report"], dict)
