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
```

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
```

A compatible CSV file can also be uploaded through the Streamlit application.

## Model

The application uses a Random Forest Regressor from scikit-learn.

The dataset is split into training and testing sets using an 80/20 split. A fixed random state is used so that the results are reproducible.

The model is evaluated using:

- Mean Absolute Error (MAE)
- R² score

The trained model is then used to estimate property prices based on the information entered by the user.

## Installation

Follow these steps from the `real-estate-app` folder.

### 1. Open the project in VS Code

Open the `real-estate-app` folder in Visual Studio Code.

### 2. Open a terminal

In VS Code, select:

**Terminal → New Terminal**

Make sure the terminal is inside the `real-estate-app` folder.

You can check your current location with:

```powershell
Get-Location
```

The path should end with:

```text
real-estate-app
```

### 3. Create a virtual environment

Run:

```powershell
python -m venv .venv
```

This creates a virtual environment inside the project folder.

### 4. Activate the virtual environment

On Windows PowerShell, run:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the terminal should show something similar to:

```text
(.venv) PS C:\...\real-estate-app>
```

### 5. Install the required packages

Run:

```powershell
python -m pip install -r requirements.txt
```

The required packages include:

- Streamlit
- pandas
- scikit-learn
- pytest

## Run the Tests

The project includes automated tests for model training and prediction.

From the `real-estate-app` folder, run:

```powershell
python -m pytest -v
```

A successful test run should show the tests as:

```text
PASSED
```

The tests verify that the model can train on the real dataset and produce a valid property-price prediction.

## Run the Application

Make sure the dataset exists at:

```text
data/final.csv
```

Then start the Streamlit application with:

```powershell
python -m streamlit run app.py
```

Streamlit will start a local web server.

The application will normally open automatically in your browser at:

```text
http://localhost:8501
```

If the browser does not open automatically, copy the local URL from the terminal and open it manually.

To stop the application, return to the terminal and press:

```text
Ctrl + C
```

## How to Use

1. Start the Streamlit application.
2. The bundled Week 9 `final.csv` dataset loads automatically.
3. Review the displayed model performance metrics:
   - Test MAE
   - Test R²
   - Number of test records
4. Enter the property information in the form.
5. Provide values such as:
   - Year sold
   - Year built
   - Living area
   - Lot size
   - Bedrooms
   - Bathrooms
   - Property tax
   - Insurance
   - Basement
   - Popular area
   - Recession status
   - Property type
6. Click **Predict Price**.
7. The estimated property price will be displayed below the form.

A different compatible `final.csv` file can also be uploaded using the CSV uploader.

## Deployment

This project is designed to be deployed using Streamlit Community Cloud.

To deploy the application:

1. Publish this project to a GitHub repository.
2. Make sure the repository contains:
   - `app.py`
   - `requirements.txt`
   - `data/final.csv`
   - `src/`
   - `tests/`
   - `README.md`
3. Open Streamlit Community Cloud.
4. Connect your GitHub account.
5. Select the GitHub repository for this project.
6. Select the `main` branch.
7. Use the following file as the application entry point:

```text
app.py
```

8. Deploy the application.
9. Test the public Streamlit link to confirm that the application loads and produces predictions correctly.
