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
#from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
from pandas.plotting import lag_plot

warnings.filterwarnings('ignore')

def find_prediction(symbol):
    warnings.filterwarnings('ignore')
    NUM_DAYS = 1000
    INTERVAL = "1d"
    start = (datetime.date.today() - datetime.timedelta( NUM_DAYS ) )
    end = datetime.datetime.today()
    data = yf.download(symbol, start=start, end=end, interval=INTERVAL)
    data.to_csv(symbol + '.csv')
    data_set = pd.read_csv(symbol + '.csv')
    '''
    data_set[['Close']].plot()
    plt.title(symbol)
    plt.show()
    
    cumulative_return = data_set.cumsum()
    cumulative_return.plot()
    plt.title(symbol + " Cumulative Returns")
    plt.show()
    plt.figure(figsize=(10,10))
    lag_plot(data_set['Close'], lag=5)
    plt.title(symbol + ' Autocorrelation plot')
    plt.show()
    '''


    shape = data_set.shape[0]
    shape_temp = shape-1
    size = int(len(data_set)*0.8)
    train_data, test_data = data_set[0:size], data_set[size:]

    '''
    plt.figure(figsize=(12,7))
    plt.title(symbol + ' Prices')
    plt.xlabel('Dates')
    plt.ylabel('Prices')
    plt.plot(data_set['Open'], 'blue', label='Training Data')
    plt.plot(test_data['Open'], 'green', label='Testing Data')
    plt.xticks(np.arange(0,shape_temp, 100), data_set['Date'][0:shape_temp:100])
    plt.legend()
    plt.show()
    '''

    train = train_data['Open'].values
    test = test_data['Open'].values
    hist = [x for x in train]
    prediction = list()
    for t in range(len(test)):
        model = sm.tsa.arima.ARIMA(hist, order=(5,1,0))
        model_fit = model.fit()
        out = model_fit.forecast()
        prediction.append(out[0])
        ob = test[t]
        hist.append(ob)

    error = mean_squared_error(test, prediction)
    print('Testing Mean Squared Error: %.3f' % error)

    '''
    plt.figure(figsize=(12,7))
    plt.plot(data_set['Open'], 'green', color='blue', label='Training Data')
    plt.plot(test_data.index, prediction, color='green', marker='o', linestyle='dashed', 
            label='Predicted Price')
    plt.plot(test_data.index, test_data['Open'], color='red', label='Actual Price')
    plt.title(symbol + ' Prices Prediction')
    plt.xlabel('Dates')
    plt.ylabel('Prices')
    plt.xticks(np.arange(0,shape_temp, 100), data_set['Date'][0:shape_temp:100])
    plt.legend()
    plt.show()
    '''

    '''
    plt.figure(figsize=(12,7))
    plt.plot(test_data.index, prediction, color='green', marker='o', linestyle='dashed', 
            label='Predicted Price')
    plt.plot(test_data.index, test_data['Open'], color='red', label='Actual Price')
    plt.title(symbol + ' Prices Prediction')
    plt.xlabel('Dates')
    plt.ylabel('Prices')
    plt.xticks(np.arange(553,691, 30), data_set['Date'][553:691:30])
    plt.legend()
    plt.show()
    '''
    length = list()
    for x in range(len(prediction)):
        length.append(str(x))
    df = pd.DataFrame(prediction)
    sizedf = pd.DataFrame(length)
    sizedf = sizedf.to_numpy()
    sizedf = sizedf.ravel()
    df = df.to_numpy().ravel()
    final = np.array((sizedf, df)).T
    return final

def pullStockData(symbol, days):
    NUM_DAYS = days
    INTERVAL = "1d"
    start = (datetime.date.today() - datetime.timedelta( int(NUM_DAYS) ) )
    end = datetime.datetime.today()
    data = yf.download(symbol, start=start, end=end, interval=INTERVAL)
    data.to_csv(symbol + '.csv')
    data_set = pd.read_csv(symbol + '.csv')
    dates = data_set['Date']
    price = data_set['Open']
    dates = dates.to_numpy()
    price = price.to_numpy()    
    data_array = np.array((dates,price)).T
    print(data_array.size)
    return data_array

def generate_risk(symbol):
    db = find_prediction(symbol)
    db = db.astype(float)
    sd = np.std(db)
    mean = np.mean(db)
    variation = sd/mean
    if (variation > 2):
        return((10, "SELL"))
    elif (variation > 1.5):
        return((9, "SELL"))
    elif (variation > 1.3):
        return((8, "SELL"))
    elif (variation > 1.1):
        return((7, "SELL"))
    elif (variation > 1):
        return((6, "HOLD"))
    elif (variation == 1):
        return((5, "HOLD"))
    elif (variation > 0.75):
        return((4, "HOLD"))
    elif (variation > 0.5):
        return((3, "BUY"))
    elif (variation > 0.1):
        return((2, "BUY"))
    else:
        return((1, "BUY"))

#find_prediction("CAT")
