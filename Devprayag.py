import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Load dataset
data = pd.read_csv(r"Devprayag.csv", parse_dates=['Date'], index_col='Date')

# Ensure the data index is datetime and sort it
data = data.sort_index()

# Define the function to forecast and plot
def forecast_and_plot(data, target, exog_vars, forecast_days=5, history_days=10):
    # Ensure target and exogenous variables are numeric
    data[target] = pd.to_numeric(data[target], errors='coerce')
    data[exog_vars] = data[exog_vars].apply(pd.to_numeric, errors='coerce')

    # Drop rows with missing values in the required columns
    data = data.dropna(subset=[target] + exog_vars)

    # Use the last 'history_days' for training
    train_data = data.iloc[-(history_days + forecast_days):-forecast_days]

    # Prepare exogenous variables for training and forecasting
    exog_train = train_data[exog_vars]
    exog_forecast = data[exog_vars].iloc[-forecast_days:]

    # Fit SARIMAX model (1, 1, 1) for simplicity; tune for better results
    model = SARIMAX(train_data[target],
                    exog=exog_train,
                    order=(1, 1, 1),
                    seasonal_order=(0, 0, 0, 0))  # No seasonality
    results = model.fit(disp=False)

    # Forecast the next 'forecast_days'
    forecast = results.get_forecast(steps=forecast_days, exog=exog_forecast)
    forecast_values = forecast.predicted_mean

    # Plot the data
    plt.figure(figsize=(12, 6))
    plt.plot(train_data[target], label="Last 10 Days", color="red", linewidth=2)
    plt.plot(forecast_values.index, forecast_values, label="Forecast (5 Days)", color="blue", linewidth=2)
    plt.title(f"Forecast for {target}")
    plt.legend()
    plt.xlabel("Date")
    plt.ylabel(target)
    plt.grid()
    plt.show()

# Exogenous variables
exog_vars = ["Temperature", "Rainfall"]

# Forecast each parameter
parameters = ["Biochemical Oxygen Demand", "Conductivity", "Turbidity",
              "Dissolved Oxygen", "Fecal Coliform", "Fecal Streptococci",
              "Nitrate", "pH", "Total Coliform"]

# Predict 5 days ahead from the last date in the dataset
for parameter in parameters:
    print(f"Processing {parameter}...")
    forecast_and_plot(data, parameter, exog_vars, forecast_days=5, history_days=10)
