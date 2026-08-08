from pathlib import Path

import pandas as pd

from src.model import predict, train


PROJECT_ROOT = (
    Path(__file__).resolve().parents[1]
)

DATA_PATH = (
    PROJECT_ROOT / "data" / "final.csv"
)


def test_model_trains_on_real_dataset():

    data = pd.read_csv(DATA_PATH)

    model, metrics = train(data)

    assert model is not None

    assert metrics["mae"] >= 0

    assert 0 <= metrics["r2"] <= 1

    assert metrics["test_rows"] > 0


def test_model_predicts_positive_price():

    data = pd.read_csv(DATA_PATH)

    model, _ = train(data)

    row = data.drop(
        columns=["price"]
    ).iloc[0].to_dict()

    value = predict(
        model,
        row
    )

    assert value > 0
