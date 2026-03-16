"""Tests for dataset loading utilities."""

from src.utils.data import load_iris_features


def test_load_iris_features_shape_and_columns() -> None:
    """Loader should return separate feature and target structures."""
    features, target = load_iris_features()

    assert features.shape == (150, 4)
    assert target.shape == (150,)
    assert list(features.columns) == [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ]
    assert target.name == "target"
