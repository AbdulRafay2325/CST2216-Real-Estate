import pandas as pd


FEATURES = [
    "year_sold",
    "property_tax",
    "insurance",
    "beds",
    "baths",
    "sqft",
    "year_built",
    "lot_size",
    "basement",
    "popular",
    "recession",
    "property_age",
    "property_type_Condo",
]

TARGET = "price"


def validate_data(
    frame: pd.DataFrame,
    require_target: bool = True
) -> pd.DataFrame:

    required = FEATURES + ([TARGET] if require_target else [])

    missing = sorted(set(required) - set(frame.columns))

    if missing:
        raise ValueError(
            f"Missing required columns: {', '.join(missing)}"
        )

    result = frame[required].copy()

    for column in required:
        result[column] = pd.to_numeric(
            result[column],
            errors="coerce"
        )

    if result.isna().any().any():
        raise ValueError(
            "Required values must be numeric and non-empty."
        )

    if require_target and len(result) < 30:
        raise ValueError(
            "At least 30 rows are required for training."
        )

    if (result["sqft"] <= 0).any():
        raise ValueError(
            "Square footage must be greater than 0."
        )

    if (result["lot_size"] < 0).any():
        raise ValueError(
            "Lot size cannot be negative."
        )

    if (result["beds"] <= 0).any():
        raise ValueError(
            "Bedrooms must be greater than 0."
        )

    if (result["baths"] <= 0).any():
        raise ValueError(
            "Bathrooms must be greater than 0."
        )

    binary_columns = [
        "basement",
        "popular",
        "recession",
        "property_type_Condo",
    ]

    for column in binary_columns:
        if not result[column].isin([0, 1]).all():
            raise ValueError(
                f"{column} must contain only 0 or 1."
            )

    return result