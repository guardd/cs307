import pandas as pd
import numpy as np
import yfinance as yf
import tensorflow as tf
from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt
import datetime
import plotly_express as px
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import Dense

symbol = input("Enter Symbol: ")
NUM_DAYS = 1000
INTERVAL = "1d"
start = (datetime.date.today() - datetime.timedelta( NUM_DAYS ) )
end = datetime.datetime.today()
data = yf.download(symbol, start=start, end=end, interval=INTERVAL)
data.to_csv(symbol + '.csv')
data_set = pd.read_csv(symbol + '.csv')
training = data_set.iloc[:,1:2].values
training_scaled = MinMaxScaler(feature_range = (0,1)).fit_transform(training)
X_train = []
Y_train = []
