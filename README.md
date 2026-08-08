# Real Estate Price Prediction

This project is a modularized version of the Week 9 Real Estate machine-learning notebook for the CST2216 Individual Term Project.

The application uses Streamlit to provide an interactive interface for training a Random Forest regression model and predicting real-estate prices.

## Features

- Loads the Week 9 `final.csv` dataset
- Validates required columns and input values
- Trains a Random Forest regression model
- Uses a reproducible train/test split
- Reports Mean Absolute Error (MAE)
- Reports R² score
- Accepts user property information
- Predicts estimated property prices
- Supports uploading another compatible CSV dataset
- Includes logging and error handling
- Includes automated model tests

## Project Structure

```text
real-estate-app/
│
├── data/
│   └── final.csv
│
├── src/
│   ├── __init__.py
│   ├── data.py
│   └── model.py
│
├── tests/
│   └── test_model.py
│
├── .gitignore
├── app.py
├── README.md
└── requirements.txt

## Dataset

The application uses the Week 9 Real Estate `final.csv` dataset.

The target variable is:

- `price`

The model uses the following features:

- `year_sold`
- `property_tax`
- `insurance`
- `beds`
- `baths`
- `sqft`
- `year_built`
- `lot_size`
- `basement`
- `popular`
- `recession`
- `property_age`
- `property_type_Condo`

The dataset is stored at:

```text
data/final.csv