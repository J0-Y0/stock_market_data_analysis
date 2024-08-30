# Financial News and Stock Price Integration Dataset (FNSPID) - EDA

## Overview

This project performs Exploratory Data Analysis (EDA) on the Financial News and Stock Price Integration Dataset (FNSPID). The dataset is designed to enhance stock market predictions by combining quantitative and qualitative data, including news headlines, publishers, publication dates, and stock ticker symbols.

## Main Project Structure

```bash
stock_market_data_analysis/
├── .gitignore                     # Git ignore file
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── notebooks/
│   ├── __init__.py
│   ├── descriptive_analysis.ipynb         # descriptive analysis
│   ├── publisher_analysis.ipynb           # publisher analysis
│   ├── text_analysis.ipynb                # text analysis
│   ├── time_series_analysis.ipynb         # time series analysis
│   └── README.md                  # Additional Insights on the EDA Performed
```
# Data
The dataset includes the following columns:

- **headline:** The title of the news article, which often includes key financial actions like stocks hitting highs, price target changes, or company earnings.
url: The direct link to the full news article.
- **publisher:** The author or creator of the article.
- **date:** The publication date and time, including timezone information (UTC-4).
- **stock:** The stock ticker symbol, a unique series of letters assigned to a publicly traded company (e.g., AAPL for Apple).

Further details about the analysis can be found in the [README.md](/notebooks/README.md)  within the `notebooks/` folder.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your system.
### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/J0-Y0/stock_market_data_analysis.git
   cd stock_market_data_analysis
2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
4. **Get the EDA  under the `notebooks/` directory:**


## License
This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.

