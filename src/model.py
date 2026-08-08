import logging

import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

from .data import FEATURES, TARGET, validate_data


LOGGER = logging.getLogger(__name__)


def train(frame: pd.DataFrame):

    clean = validate_data(frame)

    x = clean[FEATURES]
    y = clean[TARGET]

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.20,
        random_state=2216,
        stratify=clean["property_type_Condo"],
    )

    model = RandomForestRegressor(
        n_estimators=250,
        min_samples_leaf=2,
        random_state=2216,
        n_jobs=-1,
    )

    model.fit(x_train, y_train)

    predicted = model.predict(x_test)

    metrics = {
        "mae": float(
            mean_absolute_error(y_test, predicted)
        ),
        "r2": float(
            r2_score(y_test, predicted)
        ),
        "test_rows": len(x_test),
    }

    LOGGER.info(
        "Trained real-estate model: MAE=%.2f, R2=%.3f",
        metrics["mae"],
        metrics["r2"],
    )

    return model, metrics


def predict(model, property_values: dict) -> float:

    row = pd.DataFrame([property_values])

    clean = validate_data(
        row,
        require_target=False
    )

    prediction = model.predict(clean)

    return float(prediction[0])