import os
import sys

# print(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
import yfinance as yf
import ta
import matplotlib.pyplot as plt

ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2024-09-01'

# data = yf.download(ticker, start=start_date, end=end_date)
# data.to_csv('1 Preparing for Data Analysis/data/apple_historical_data_20-24.csv')
# data = pd.read_csv('1 Preparing for Data Analysis/data/apple_historical_data_20-24.csv')
def load_csv(file_path):
  data = pd.read_csv(file_path)
  # 删除第2,3行
  data = data.drop(index=[0,1])
  data.rename(columns={'Price': 'Date'}, inplace=True)
  data['Date'] = pd.to_datetime(data['Date'])
  data.set_index('Date', inplace=True)
  print(data)
  return data


def add_features(data):

  data['RSI'] = ta.momentum.rsi(data['Close'])
  '''
  The relative strength index (RSI) is a momentum indicator used in technical analysis. 
  RSI measures the speed and magnitude of a security's recent price changes to detect overvalued or undervalued conditions in the price of that security.

  An asset is usually considered overbought when the RSI is above 70 and oversold when it is below 30.

  The RSI line crossing below the overbought line or above the oversold line can be seen by traders as a signal to buy or sell.
  '''

  plt.figure(figsize=(14, 5))
  plt.plot(data['RSI'], label='RSI', color='purple')
  plt.axhline(70, linestyle='--', alpha=0.5, color='red', label='Overbought (70)')
  plt.axhline(30, linestyle='--', alpha=0.5, color='green', label='Oversold (30)')
  plt.title(f'{ticker} Relative Strength Index (RSI)')
  plt.xlabel('Date')
  plt.ylabel('RSI')
  plt.legend()
  plt.grid()
  plt.show()

  # 2. Moving Average Convergence Divergence (MACD)
  data['MACD'] = ta.trend.macd_diff(data['Close'])
  data['MACD_Signal'] = ta.trend.macd_signal(data['Close']) # exp MA of MACD
  """
  Moving average convergence/divergence (MACD) is a technical indicator to help investors identify price trends, measure trend momentum, and identify entry points for buying or selling. Moving average convergence/divergence (MACD) is a trend-following momentum indicator that shows the relationship between two exponential moving averages (EMAs) of a security's price. (Source: Investopedia)

  The MACD line is calculated by subtracting the 26-period exponential moving average (EMA) from the 12-period EMA.

  The signal line is a nine-period EMA of the MACD line.

  Traders may buy the security when the MACD line crosses above the signal line and sell—or short—the security when the MACD line crosses below the signal line. (Source: Investopedia)
  """
  # 绘图 MACD
  plt.figure(figsize=(14, 5))
  plt.plot(data['MACD'], label='MACD', color='blue')
  plt.plot(data['MACD_Signal'], label='MACD_Signal', color='red', linestyle='--')
  plt.title(f"{ticker} MACD")
  plt.xlabel('Date')
  plt.ylabel('MACD')
  plt.legend()
  plt.grid()
  plt.show()

  # 3. Bollinger Bands
  data['Bollinger_High'] = data['Close'].rolling(window=20).mean() + (data['Close'].rolling(window=20).std() * 2)
  data['Bollinger_Low'] = data['Close'].rolling(window=20).mean() - (data['Close'].rolling(window=20).std() * 2)
  """
  Bollinger Bands is a technical analysis tool used to determine where prices are high and low relative to each other.

  These bands are composed of three lines: a simple moving average (the middle band) and an upper and lower band. 
  The upper and lower bands are typically two standard deviations above or below a 20-period simple moving average (SMA).

  The bands widen and narrow as the volatility of the underlying asset changes.

  Option traders and investors use Bollinger Bands to assess market volatility and identify potential entry and exit points. 
  Narrow bands indicate less volatility, which means a significant price move could be imminent. 
  This is known as a "squeeze".
  (Source: Investopedia)
  """
  # 绘制布林带图表
  plt.figure(figsize=(14, 7))
  plt.plot(data['Close'], label='Close Price', color='blue', alpha=0.5)
  plt.plot(data['Bollinger_High'], label='Bollinger High', color='red', linestyle='--')
  plt.plot(data['Bollinger_Low'], label='Bollinger Low', color='green', linestyle='--')
  plt.fill_between(data.index, data['Bollinger_Low'], data['Bollinger_High'], color='lightgrey', alpha=0.5)
  plt.title(f"{ticker} Bollinger Bands")
  plt.xlabel('Date')
  plt.ylabel('Price')
  plt.legend()
  plt.grid()
  plt.show()

  data.dropna(inplace=True)  # ?
  # 保存数据到CSV文件
  data.to_csv("AAPL_trading_features.csv")

if __name__ == '__main__':
    load_csv('1 Preparing for Data Analysis/data/apple_historical_data_20-24.csv')