import pandas as pd
import talib as ta
import matplotlib.pyplot as plt


class FinancialAnalyzer:

    def load_data(self, ticker, isPath=False):

        df = []
        if isPath:
            df = pd.read_csv(ticker)
            df.rename(columns={"date": "Date", "stock": "Stock"}, inplace=True)

            df["Date"] = pd.to_datetime(df["Date"], format="ISO8601").dt.normalize()
            df["Date"] = df["Date"].dt.date

        else:
            df = pd.read_csv(f"datasets\yfinance_data\{ticker}_historical_data.csv")
            df["Date"] = pd.to_datetime(df["Date"]).dt.normalize()

        df.set_index("Date", inplace=True)
        return df

    def load_datas(self, tickers):
        all_data = []
        for ticker in tickers:
            data = self.load_data(ticker)
            if data is not None:
                data["Stock"] = ticker  # Add a 'stock' column with the ticker symbol
                all_data.append(data)  # Append the DataFrame to the list

        # Concatenate all the DataFrames in the list
        combined_data = pd.concat(all_data)
        return combined_data

    def market_signals(self, data, sma, ema1, ema2, rsi):
        # Calculate SMA simple moving average
        data[f"SMA"] = ta.SMA(data["Close"], timeperiod=sma)
        # Calculate EMA (Exponential Moving Average)
        data[f"EMA_1"] = ta.EMA(data["Close"], timeperiod=ema1)
        data[f"EMA_2"] = ta.EMA(data["Close"], timeperiod=ema2)
        # Calculate RSI
        data["RSI"] = ta.RSI(data["Close"], timeperiod=rsi)

        data["MACD_Line"], data["MACD_Signal"], data["MACD_Histogram"] = ta.MACD(
            data["Close"], fastperiod=12, slowperiod=26, signalperiod=9
        )
        return data

    def sma_plot(self, data):
        plt.figure(figsize=(10, 5))
        plt.plot(data["Close"], label="Close Price", color="blue", alpha=0.7)
        plt.plot(data["SMA"], label="100-day SMA", color="orange", alpha=0.7)
        plt.title("Close Price and 100-day Simple Moving Average")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.grid(True)
        plt.show()

    def ema_plot(self, data):
        plt.figure(figsize=(14, 7))

        # Plot Closing Price
        plt.plot(data["Close"], label="Close Price", color="black", alpha=0.5)

        # Plot EMA
        plt.plot(data["EMA_1"], label="EMA 12", color="blue", alpha=0.7)
        plt.plot(data["EMA_2"], label="EMA 26", color="red", alpha=0.7)

        # Customize the plot
        plt.title("Close Price and EMA")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)
        plt.show()

    def rsi_plot(self, data):
        plt.figure(figsize=(14, 7))
        plt.plot(
            data.index,
            data["RSI"],
            label="RSI",
            color="purple",
            alpha=0.7,
        )
        plt.axhline(y=70, color="gray", linestyle="--", label="Overbought (70)")
        plt.axhline(y=30, color="gray", linestyle="--", label="Oversold (30)")
        plt.title("Relative Strength Index (RSI)")
        plt.xlabel("Date")
        plt.ylabel("RSI")
        plt.legend()
        plt.grid(True)
        plt.show()

    def macd_plot(self, data):
        # Plot MACD and MACD Signal
        plt.figure(figsize=(14, 10))
        plt.subplot(3, 1, 3)
        plt.plot(data["MACD_Line"], label="MACD Line", color="blue", alpha=0.7)
        plt.plot(
            data["MACD_Signal"],
            label="MACD Signal Line",
            color="red",
            alpha=0.7,
        )
        plt.bar(
            data.index,
            data["MACD_Histogram"],
            color=["green" if x >= 0 else "red" for x in data["MACD_Histogram"]],
            label="MACD Histogram",
            alpha=0.7,
        )
        plt.title("MACD Line, MACD Signal Line, and MACD Histogram")
        plt.xlabel("Date")
        plt.ylabel("MACD")
        plt.legend()
        plt.grid(True)
        plt.show()
