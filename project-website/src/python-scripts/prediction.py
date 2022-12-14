import pandas as pd
import numpy as np
import yfinance as yf
import tensorflow as tf
from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt
import datetime
import plotly_express as px
import warnings
import seaborn as sns
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from pandas.plotting import lag_plot

warnings.filterwarnings('ignore')

symbol = input("Enter Symbol: ")
NUM_DAYS = 1000
INTERVAL = "1d"
start = (datetime.date.today() - datetime.timedelta( NUM_DAYS ) )
end = datetime.datetime.today()
data = yf.download(symbol, start=start, end=end, interval=INTERVAL)
data.to_csv(symbol + '.csv')
data_set = pd.read_csv(symbol + '.csv')
data_set[['Close']].plot()
plt.title(symbol)
plt.show()

cumulative_return = data_set.cumsum()
cumulative_return.plot()
plt.title(symbol + " Cumulative Returns")
plt.show()
plt.figure(figsize=(10,10))
lag_plot(data_set['Open'], lag=5)
plt.title(symbol + ' Autocorrelation plot')
plt.show()


print(data_set.shape)
size = int(len(data_set)*0.8)
train_data, test_data = data_set[0:size], data_set[size:]
plt.figure(figsize=(12,7))
plt.title(symbol + ' Prices')
plt.xlabel('Dates')
plt.ylabel('Prices')
plt.plot(data_set['Open'], 'blue', label='Training Data')
plt.plot(test_data['Open'], 'green', label='Testing Data')
plt.xticks(np.arange(0,691, 120), data_set['Date'][0:691:120])
plt.legend()
plt.show()

train = train_data['Open'].values
test = test_data['Open'].values
hist = [x for x in train]
prediction = list()
for t in range(len(test)):
    model = ARIMA(hist, order=(5,1,0))
    model_fit = model.fit(disp=0)
    out = model_fit.forecast()
    prediction.append(out[0])
    ob = test[t]
    hist.append(ob)
error = mean_squared_error(test, prediction)
print('Testing Mean Squared Error: %.3f' % error)
plt.figure(figsize=(12,7))
plt.plot(data_set['Open'], 'green', color='blue', label='Training Data')
plt.plot(test_data.index, prediction, color='green', marker='o', linestyle='dashed', 
         label='Predicted Price')
plt.plot(test_data.index, test_data['Open'], color='red', label='Actual Price')
plt.title(symbol + ' Prices Prediction')
plt.xlabel('Dates')
plt.ylabel('Prices')
plt.xticks(np.arange(0,691, 120), data_set['Date'][0:691:120])
plt.legend()
plt.show()


plt.figure(figsize=(12,7))
plt.plot(test_data.index, prediction, color='green', marker='o', linestyle='dashed', 
         label='Predicted Price')
plt.plot(test_data.index, test_data['Open'], color='red', label='Actual Price')
plt.title(symbol + ' Prices Prediction')
plt.xlabel('Dates')
plt.ylabel('Prices')
plt.xticks(np.arange(500,691, 60), data_set['Date'][500:691:60])
plt.legend()
plt.show()
