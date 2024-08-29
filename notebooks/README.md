# Exploratory Data Analysis (EDA) for benin-malanville.csv

## Overview
This notebook performs an Exploratory Data Analysis (EDA) on the `benin-malanville.csv` dataset. The dataset contains various meteorological and environmental measurements collected over time. The goal of this analysis is to clean the data, understand its structure, and visualize key patterns and relationships.

## Description
The dataset includes the following columns:

## Steps in the Analysis

1. **Import Required Packages**
   - Libraries: `pandas`, `numpy`, `matplotlib.pyplot`, `seaborn`, `scipy.stats`.

2. **Load the Dataset**
   - Read the CSV file and display the first few rows.

3. **Data Shape and Statistical Summary**
   - Analyze the dataset shape and provide statistical descriptions of numerical columns.

4. **Data Quality Check**
   - **Missing Values**: Identify columns with missing values.
   - **Negative Values**: Check for and handle negative values in columns where only positive values are expected.

5. **Data Cleaning**
   - Handle missing values and incorrect entries.
   - Convert 'Timestamp' to datetime and set as index.

6. **Data Visualization**
   - **Histograms**: Display histograms for numeric features.
   - **Correlation Matrix**: Visualize correlations between numerical variables.
   - **Area Plot**: Plot GHI, DNI, DHI, and Tamb over time.
   - **Impact of Cleaning**: Analyze the effect of cleaning on sensor readings.
   - **Correlation Heatmap**: Explore correlations between solar radiation and temperature measurements.
   - **Polar Plot**: Visualize wind speed in relation to wind direction.
   - **Scatter Plots**: Examine relationships between GHI and TModA, WS and GHI.
   - **Z-scores**: Calculate Z-scores to identify outliers.

## Dependencies
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scipy`

## Running the Notebook
1. Ensure you have all the dependencies installed. You can install them using:
    ```bash
    pip install pandas numpy matplotlib seaborn scipy
    ```
2. Open the notebook using JupyterLab or Jupyter Notebook:
    ```bash
    jupyter lab
    ```
3. Run the notebook cells sequentially to execute the analysis.

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

