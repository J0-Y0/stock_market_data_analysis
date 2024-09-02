import pandas as pd


class StockAnalyzer:

    def load_normalize(self, path):
        data = pd.read_csv(path)
        # Convert timestamps to datetime and normalize
        data["date"] = pd.to_datetime(data["data"]).dt.normalize()
        return data

    def load_normalize(self, data):
        # Convert timestamps to datetime and normalize
        data["date"] = pd.to_datetime(data["data"]).dt.normalize()
        return data
