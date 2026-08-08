import logging
from pathlib import Path

import pandas as pd
import streamlit as st

from src.model import predict, train


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

LOGGER = logging.getLogger(__name__)


st.set_page_config(
    page_title="Real Estate Price",
    page_icon="🏠",
)


st.title("Real Estate Price Prediction")

st.write(
    "This application uses the Week 9 real-estate dataset "
    "to train a Random Forest regression model and predict "
    "property prices."
)


PROJECT_ROOT = Path(__file__).resolve().parent

DEFAULT_DATA = PROJECT_ROOT / "data" / "final.csv"


upload = st.file_uploader(
    "Optional: upload another compatible final.csv",
    type="csv",
)


try:

    if upload is not None:

        data = pd.read_csv(upload)

        st.info(
            "Using uploaded dataset."
        )

    else:

        if not DEFAULT_DATA.exists():
            raise FileNotFoundError(
                "data/final.csv was not found. "
                "Place the Week 9 final.csv inside "
                "real-estate-app/data/."
            )

        data = pd.read_csv(DEFAULT_DATA)

        st.info(
            "Using the bundled Week 9 final.csv dataset."
        )


    model, metrics = train(data)


    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Test MAE",
        f"${metrics['mae']:,.0f}"
    )

    col2.metric(
        "Test R²",
        f"{metrics['r2']:.3f}"
    )

    col3.metric(
        "Test Records",
        metrics["test_rows"]
    )


    st.subheader(
        "Property Information"
    )


    with st.form("property"):

        c1, c2 = st.columns(2)


        year_sold = c1.number_input(
            "Year sold",
            min_value=1990,
            max_value=2030,
            value=2013,
        )


        year_built = c2.number_input(
            "Year built",
            min_value=1800,
            max_value=2030,
            value=2000,
        )


        sqft = c1.number_input(
            "Living area (sq ft)",
            min_value=100,
            max_value=20000,
            value=1800,
        )


        lot_size = c2.number_input(
            "Lot size (sq ft)",
            min_value=0,
            max_value=500000,
            value=5000,
        )


        beds = c1.number_input(
            "Bedrooms",
            min_value=1,
            max_value=20,
            value=3,
        )


        baths = c2.number_input(
            "Bathrooms",
            min_value=1,
            max_value=20,
            value=2,
        )


        property_tax = c1.number_input(
            "Property tax",
            min_value=0,
            max_value=10000,
            value=400,
        )


        insurance = c2.number_input(
            "Insurance",
            min_value=0,
            max_value=5000,
            value=120,
        )


        basement = c1.selectbox(
            "Basement",
            options=[0, 1],
            format_func=lambda x: "Yes" if x else "No",
        )


        popular = c2.selectbox(
            "Popular area",
            options=[0, 1],
            format_func=lambda x: "Yes" if x else "No",
        )


        recession = c1.selectbox(
            "Sold during recession",
            options=[0, 1],
            format_func=lambda x: "Yes" if x else "No",
        )


        property_type_condo = c2.selectbox(
            "Property type",
            options=[0, 1],
            format_func=lambda x:
                "Condo" if x else "House",
        )


        submitted = st.form_submit_button(
            "Predict Price"
        )


    if submitted:

        if year_built > year_sold:

            st.error(
                "Year built cannot be later than year sold."
            )

        else:

            property_age = (
                year_sold - year_built
            )


            values = {

                "year_sold": year_sold,

                "property_tax": property_tax,

                "insurance": insurance,

                "beds": beds,

                "baths": baths,

                "sqft": sqft,

                "year_built": year_built,

                "lot_size": lot_size,

                "basement": basement,

                "popular": popular,

                "recession": recession,

                "property_age": property_age,

                "property_type_Condo":
                    property_type_condo,
            }


            estimated_price = predict(
                model,
                values
            )


            st.success(
                f"Estimated price: "
                f"${estimated_price:,.0f}"
            )


except Exception as exc:

    LOGGER.exception(
        "Real-estate application failed"
    )

    st.error(
        f"Could not process the data: {exc}"
    )