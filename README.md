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
│   ├── news_and_stock_reation.ipynb       # Analysis of news and stock data integration
│   ├── yfinance_analysis.ipynb            # Analysis using yfinance
│   ├── descriptive_analysis.ipynb         # Descriptive statistics of the dataset
│   ├── publisher_analysis.ipynb           # Analysis of publisher activity
│   ├── text_analysis.ipynb                # Text analysis including sentiment analysis
│   ├── time_series_analysis.ipynb         # Time series analysis of publication trends
│   └── README.md                  # Additional Insights on the EDA Performed
├── scripts/
│   ├── financial_analyzer.py              # Financial analysis utility and plotting functions
│   ├── news_and_stock_reation.py          # Utility for news and stock data integration
```
## Data
The dataset includes the following columns:

- `headline`: The title of the news article, often including key financial actions like stocks hitting highs, price target changes, or company earnings.
- `url`: The direct link to the full news article.
- `publisher`: The author or creator of the article.
- `date`: The publication date and time, including timezone information (UTC-4).
- `stock`: The stock ticker symbol, a unique series of letters assigned to a publicly traded company (e.g., AAPL for Apple).

Further details about the analysis can be found in the [README.md](/notebooks/README.md) within the notebooks/ folder.


## Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your system.
I recommend using `Python 3.10`, as it works well with the `TA-lib `library.

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

    3.1. **TA-Lib Library Installation:**
    1. Download the precompiled TA-Lib wheel from the new repository release.
    2. Visit the [TA-Lib-build release page](https://github.com/cgohlke/talib-build/releases/).
    3. Select the TA-Lib wheel that matches your system's architecture (32-bit or 64-bit).
    4. Install the selected TA-Lib wheel. For example, for a 64-bit Windows architecture (`win_amd64`), use the following command:
        ```bash
        pip install https://github.com/cgohlke/talib-build/releases/download/v0.4.32/TA_Lib-0.4.32-cp310-cp310-win_amd64.whl
        ```

    3.2. **Install Other Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Get the EDA  under the `notebooks/` directory:**
    ``` bash
        stock_market_data_analysis/
        ├── notebooks/
        │   ├── news_and_stock_reation.ipynb       # Analysis of news and stock data integration
        │   ├── yfinance_analysis.ipynb            # Analysis using yfinance
        │   ├── time_series_analysis.ipynb         # Time series analysis of publication trends

## License
This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.