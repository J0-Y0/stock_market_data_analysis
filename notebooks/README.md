# Analysis Performed

## 1. Descriptive Statistics
- **Headline Length**: Calculated basic statistics for the length of news headlines, including mean, median, and standard deviation.
- **Publisher Activity**: Counted the number of articles per publisher to identify which publishers are most active in the dataset.
- **Publication Date Trends**: Analyzed publication dates to identify trends over time, such as increased news frequency on specific days or during significant market events.

## 2. Text Analysis
- **Sentiment Analysis**: Analyzed the sentiment of headlines using VADER sentiment analysis to gauge whether the tone of the news is positive, negative, or neutral.
- **Topic Modeling**: Used natural language processing (NLP) techniques to identify common keywords or phrases in the headlines, potentially extracting topics or significant events that frequently occur.

## 3. Time Series Analysis
- **Publication Frequency**: Examined how the frequency of publication varies over time, identifying any spikes that may relate to specific market events or economic conditions.
- **Publishing Times**: Analyzed publishing times to determine if there’s a specific time of day when most news is released, which could impact market reactions.

## 4. Publisher Analysis
- **Active Publishers**: Identified which publishers contribute the most to the news feed, allowing for an understanding of the sources of information.
- **Publisher Type**: Compared the type and tone of news reported by different publishers, examining whether certain publishers are more likely to publish positive, negative, or neutral news.

## 5. Financial and Sentiment Data Integration
- **Date Normalization**: Aligned dates in the news and stock datasets to ensure that news items correspond accurately to the respective trading days.
- **Stock Identifier Addition**: Added an extra "Stock" column to each stock data file, identifying the ticker symbol for better analytics.
- **Data Merging**: Merged the stock data and news data based on their common **Stock** and **Date** columns, facilitating a combined analysis of sentiment and stock performance.

## 6. Correlation Analysis
- **Aggregate Sentiments**: Computed the average daily sentiment scores for each stock when multiple articles appeared on the same day.
- **Daily Returns Calculation**: Calculated the daily percentage changes in stock prices, representing the daily return for each stock.
- **Correlation Between Sentiment and Daily Returns**:
    - **Overall Correlation**: Calculated the Pearson correlation coefficient between average daily sentiment scores and daily stock returns, finding a correlation of **0.19** for all stocks combined.
    - **Stock-Specific Correlations**:
        - AAPL: **0.088856**
        - AMZN: **0.162847**
        - GOOG: **0.186945**
        - NVDA: **0.213399**
        - TSLA: **0.162896**

These correlations indicate the relationship between news sentiment and stock performance, with variations across different stocks. This analysis provides insight into how market sentiment, as expressed in news headlines, correlates with actual market behavior.
