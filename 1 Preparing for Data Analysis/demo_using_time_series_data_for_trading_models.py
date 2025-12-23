import os
import sys

# sys.path.append()
import func_lib

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


path = '1 Preparing for Data Analysis/data/apple_historical_data_200101-240901.csv'
data = func_lib.load_csv_25format(path)

print(data)
print(data.info())
# drow rows with NaN values
data.dropna(inplace=True)
print(data.info())

des = data.describe()

print(des)

# 1. resample data to weekly and monthly frequency
data_weekly = data['Close'].resample('W').last()
data_monthly = data['Close'].resample('ME').last()

print(data_weekly)
print(data_monthly)

#2 cakcydate daukt and log returns
data['Daily_Return'] = data['Close'].pct_change()
data['Log_Return'] = np.log(data['Close'] / data['Close'].shift(1))

print(data)
data.dropna(inplace=True)
print(data)


# 3. moving averages as features
data['SMA_20'] = data['Close'].rolling(window=20).mean()



data['SMA_50'] = data['Close'].rolling(window=50).mean()

print(data)


# 4.Volatility as a feature
data['Volatility'] = data['Daily_Return'].rolling(window=20).std()

data.dropna(inplace=True)
print(data)

data.to_csv('1 Preparing for Data Analysis/data/apple_historical_data_200101-240901_with_features.csv')
