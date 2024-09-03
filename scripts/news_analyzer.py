import pandas as pd
import talib as ta
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# nltk.download("vader_lexicon")


class NewsAnalyzer:
    def sentiment(self, data):

        sia = SentimentIntensityAnalyzer()
        # Apply sentiment analysis
        data["Sentiment Scores"] = data["headline"].apply(sia.polarity_scores)
        data["Sentiment"] = data["Sentiment Scores"].apply(
            lambda score: (
                "positive"
                if score["compound"] > 0.05
                else ("negative" if score["compound"] < -0.05 else "neutral")
            )
        )
        data["Compound Score"] = data["Sentiment Scores"].apply(lambda x: x["compound"])

        return data

    def sentiment_plot(self, data):
        sentiment_distribution = data["Sentiment"].value_counts()
        print("Sentiment Distribution:")
        print(sentiment_distribution)

        # Plot sentiment distribution
        sentiment_distribution.plot(
            kind="bar", title="Sentiment Distribution of Headlines"
        )
        plt.xlabel("Sentiment")
        plt.ylabel("Number of Headlines")
        plt.show()
