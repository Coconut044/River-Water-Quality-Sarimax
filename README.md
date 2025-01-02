# Ganga River Water Quality Monitoring

This project aims to monitor the water quality across 13 locations along the course of the Ganga River. The objective is to analyze and forecast key water quality parameters to understand the river's health and assist in decision-making for its protection.

## Table of Contents
- [Overview](#overview)
- [Data](#data)
- [Installation](#installation)
- [Modeling](#modeling)
- [Results](#results)
- [Contributors](#contributors)

## Overview

This project utilizes data collected from **13 locations** along the Ganga River to track water quality parameters. The key parameters include:
- Biochemical Oxygen Demand (BOD)
- Conductivity
- Turbidity
- Dissolved Oxygen (DO)
- Fecal Coliform
- Fecal Streptococci
- Nitrate
- pH
- Total Coliform

The data spans the **past 4 years** (from **01/01/2020** to **07/12/2024**), with the water quality data sourced from **GEMStat** and weather data from **CPCB** and **Meteo Stat**. The project involves time-series analysis and forecasting to predict future trends in water quality across the river.

## Data

The dataset consists of the following:
- **Water Quality Data:** Sourced from GEMStat, it includes parameters such as BOD, conductivity, turbidity, dissolved oxygen, and more.
- **Weather Data:** Sourced from CPCB and Meteo Stat, including weather variables such as temperature and rainfall, which can influence water quality.

The data is organized by date and location and is stored in CSV files within the repository.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ganga-river-water-quality-monitoring.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ganga-river-water-quality-monitoring
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure that you have Python 3.x installed.

## Modeling

This project leverages the **SARIMAX** (Seasonal AutoRegressive Integrated Moving Average with Exogenous Variables) model to forecast water quality parameters. The model is trained using historical data for each parameter, incorporating weather data as exogenous variables to improve prediction accuracy.

### Key Model Components:
- **ARIMA:** The model captures time-series patterns and dependencies, considering past values of the target parameter.
- **Exogenous Variables:** Weather data (e.g., temperature, rainfall) is used as additional input to forecast future water quality.
- **Forecasting:** The model predicts each water quality parameter for up to **5 days ahead**, based on historical trends and exogenous variables.

## Results

The project generates visualizations and predictions for each water quality parameter at the 13 monitoring locations. By analyzing historical trends and making forecasts, the project aims to provide insights into the river's health and predict potential water quality changes over time.

## Contributors

- Nitya Pillai (https://github.com/Coconut044)

Feel free to contribute to the project by submitting pull requests, opening issues, or providing suggestions.
