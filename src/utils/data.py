"""Data-loading utilities for the Iris clustering project."""

from __future__ import annotations

from typing import Tuple

import pandas as pd
from sklearn.datasets import load_iris


def load_iris_features() -> Tuple[pd.DataFrame, pd.Series]:
    """Return Iris features and target as separate objects.

    Returns:
        A tuple where the first value is a feature DataFrame and the second
        value is a target Series.
    """
    dataset = load_iris(as_frame=True)
    frame = dataset.frame.copy()
    target_name = dataset.target.name

    if target_name not in frame.columns:
        msg = "Iris target column was not found in the loaded frame."
        raise ValueError(msg)

    features = frame.drop(columns=[target_name])
    target = frame[target_name].copy()
    return features, target
