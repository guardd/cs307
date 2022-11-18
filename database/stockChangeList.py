import prediction
import StockData
import yfinance as yf
def percentage_change(stockABV):
    #currentPrice = StockData.get_price(stockABV)
    currentPrice = yf.Ticker(stockABV).history(period='1d')['Close'][0]
    predictedPrice = prediction.find_prediction(stockABV)[-1][1]
    percentage = float((((predictedPrice - currentPrice) / currentPrice)) * 100)
    return percentage

def percentage_change_list(percentage, downup, stockABVs):
    #0th column is size of thing
    abvlist = []
    abvPercentageList = []
    for abv in stockABVs:
        change = percentage_change(abv)
        if (downup > 0):
            if (change > downup):
                abvlist.append(abv)
                abvPercentageList.append(change)
        else: 
            if (change < downup):
                abvlist.append(abv)
                abvPercentageList.append(change)
    data = {}
    data['size'] = len(abvlist)
    data['abvs'] = abvlist
    data['percentages'] = abvPercentageList
    return data

