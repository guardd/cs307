def findTaxRate(state, amount):
    if (state == "CO"):
        return '4.55%'
    else if (state == "IL"):
        return '4.955%'
    else if (state == "IN"):
        return '3.23%'
    else if (state == "IL"):
        return '4.955%'
    else if (state == "KY"):
        return '5%'
    else if (state == "MA"):
        return '5%'
    else if (state == "MI"):
        return '4.25%'
    else if (state == "NH"):
        return '5%'
    else if (state == "NC"):
        return '4.99%'
    else if (state == "PA"):
        return '3.07%'
    else if (state == "UT"):
        return '4.95%'

    else if (state == "AL"):
        if (amount > 0 and amount < 500):
            return '2%'
        if (amount >= 500 and amount < 3000):
            return '4%'
        if (amount > 3000)
            return '5%'

    else if (state == "AZ"):
        if (amount > 0 and amount < 26500):
            return '2.59%'
        if (amount >= 26501 and amount < 53000):
            return '3.34%'
        if (amount >= 53001 and amount < 159000):
            return '4.17%'
        if (amount >= 159000)
            return '4.50%'

    else if (state == "AK"):
        if (amount > 0 and amount < 5000):
            return '0%'
        if (amount >= 5000 and amount <= 9999):
            return '2%'
        if (amount > 10000 and amount <= 14299):
            return '3%'
        if (amount > 14300 and amount <= 23599.99):
            return '3.4%'
        if (amount > 23600 and amount <= 39699.99):
            return '5%'
        if (amount >= 39700)
            return '5.9%'
        
    else if (state == "CA"):
        if (amount > 0 and amount < 9325):
            return '1%'
        if (amount >= 9326 and amount <= 22107):
            return '2%'
        if (amount > 22108 and amount <= 34892):
            return '4%'
        if (amount > 34893 and amount <= 48435):
            return '6%'
        if (amount > 48436 and amount <= 61214):
            return '8%'
        if (amount > 61215 and amount <= 312686):
            return '9.3%'
        if (amount > 312687 and amount <= 375221):
            return '10.3%'
        if (amount > 375222 and amount <= 625369):
            return '11.3%'
        if (amount >= 625370)
            return '12.3%'

    else if (state == "CT"):
        if (amount > 0 and amount < 10000):
            return '3%'
        if (amount >= 10001 and amount <= 50000):
            return '5%'
        if (amount > 50001 and amount <= 100000):
            return '5.5%'
        if (amount > 100001 and amount <= 200000):
            return '6%'
        if (amount > 200001 and amount <= 250000):
            return '6.5%'
        if (amount > 250001 and amount <= 500000):
            return '6.9%'
        if (amount >= 500001)
            return '6.99%'

    else if (state == "DE"):
        if (amount > 0 and amount < 2000):
            return '0%'
        if (amount >= 2000 and amount <= 5000):
            return '2.2%'
        if (amount > 5000 and amount <= 10000):
            return '3.9%'
        if (amount > 10000 and amount <= 20000):
            return '4.8%'
        if (amount > 20000 and amount <= 25000):
            return '5.2%'
        if (amount > 25000 and amount <= 60000):
            return '5.5%'
        if (amount >= 60000)
            return '6.6%'

    else if (state == "DC"):
        if (amount > 0 and amount < 10000):
            return '4%'
        if (amount >= 10000 and amount <= 40000):
            return '6%'
        if (amount > 40000 and amount <= 60000):
            return '6.5%'
        if (amount > 60000 and amount <= 250000):
            return '8.5%'
        if (amount > 250000 and amount <= 500000):
            return '9.25%'
        if (amount > 500000 and amount <= 1000000):
            return '9.75%'
        if (amount >= 1000000)
            return '10.75%'

    else if (state == "GA"):
        if (amount > 0 and amount < 750):
            return '1%'
        if (amount >= 751 and amount <= 2250):
            return '2%'
        if (amount > 2251 and amount <= 3750):
            return '3%'
        if (amount > 3751 and amount <= 5250):
            return '4%'
        if (amount > 5251 and amount <= 7000):
            return '5%'
        if (amount > 7001):
            return '5.75%'

    else if (state == "HI"):
        if (amount > 0 and amount < 2400):
            return '1.4%'
        if (amount >= 2400 and amount <= 4800):
            return '3.2%'
        if (amount > 4800 and amount <= 9600):
            return '5.5%'
        if (amount > 9600 and amount <= 14400):
            return '6.4%'
        if (amount > 14400 and amount <= 19200):
            return '6.8%'
        if (amount > 19200 and amount <= 24000):
            return '7.2%'
        if (amount > 24000 and amount <= 36000):
            return '7.6%'
        if (amount > 36000 and amount <= 48000):
            return '7.9%'
        if (amount > 48000 and amount <= 150000):
            return '8.25%'
        if (amount > 150000 and amount <= 175000):
            return '9%'
        if (amount > 175000 and amount <= 200000):
            return '10%'
        if (amount > 200000):
            return '11%'

    else if (state == "ID"):
        if (amount > 0 and amount < 1588):
            return '1%'
        if (amount >= 1589 and amount <= 4763):
            return '3.1%'
        if (amount > 4764 and amount <= 6351):
            return '4.5%'
        if (amount > 6352 and amount <= 7939):
            return '5.5%'
        if (amount > 7940):
            return '6.5%'

    else if (state == "IA"):
        if (amount > 0 and amount < 1539):
            return '0.36%'
        if (amount >= 1540 and amount <= 3078):
            return '0.72%'
        if (amount > 3079 and amount <= 6156):
            return '2.43%'
        if (amount > 6157 and amount <= 13851):
            return '4.5%'
        if (amount > 13852 and amount <= 23085):
            return '6.12%'
        if (amount > 23086 and amount <= 30780):
            return '6.48%'
        if (amount > 30781 and amount <= 46170):
            return '6.8%'
        if (amount > 46171 and amount <= 69255):
            return '7.92%'
        if (amount > 69256):
            return '8.98%'
    
    else if (state == "IA"):
        if (amount > 0 and amount < 1539):
            return '0.36%'
        if (amount >= 1540 and amount <= 3078):
            return '0.72%'
        if (amount > 3079 and amount <= 6156):
            return '2.43%'
        if (amount > 6157 and amount <= 13851):
            return '4.5%'
        if (amount > 13852 and amount <= 23085):
            return '6.12%'
        if (amount > 23086 and amount <= 30780):
            return '6.48%'
        if (amount > 30781 and amount <= 46170):
            return '6.8%'
        if (amount > 46171 and amount <= 69255):
            return '7.92%'
        if (amount > 69256):
            return '8.98%'

    else if (state == "KS"):
        if (amount > 0 and amount < 15000):
            return '3.1%'
        if (amount >= 15001 and amount <= 30000):
            return '5.25%'
        if (amount > 30001):
            return '5.70%'

    else if (state == "KS"):
        if (amount > 0 and amount < 15000):
            return '3.1%'
        if (amount >= 15001 and amount <= 30000):
            return '5.25%'
        if (amount > 30001):
            return '5.70%'

    else if (state == "LA"):
        if (amount > 0 and amount < 12500):
            return '2%'
        if (amount >= 12501 and amount <= 50000):
            return '4%'
        if (amount > 50001):
            return '6%'

    else if (state == "ME"):
        if (amount > 0 and amount < 22999):
            return '5.8%'
        if (amount >= 23000 and amount <= 54449):
            return '6.75%'
        if (amount > 54450):
            return '7.15%'
    
    else if (state == "MD"):
        if (amount > 0 and amount < 1000):
            return '2%'
        if (amount >= 1001 and amount <= 2000):
            return '3%'
        if (amount > 2001 and amount <= 3000):
            return '4%'
        if (amount > 3001 and amount <= 100000):
            return '4.75%'
        if (amount > 100001 and amount <= 125000):
            return '5%'
        if (amount > 125001 and amount <= 150000):
            return '5.25%'
        if (amount > 150001 and amount <= 250000):
            return '5.5%'
        if (amount > 250001):
            return '5.75%'

    else if (state == "MN"):
        if (amount > 0 and amount < 27230):
            return '5.35%'
        if (amount >= 27321 and amount <= 89440):
            return '6.8%'
         if (amount >= 89441 and amount <= 166040):
            return '7.85%'
        if (amount > 166041):
            return '9.85%'
    
    else if (state == "MS"):
        if (amount > 0 and amount < 3000):
            return '0%'
        if (amount >= 3001 and amount <= 5000):
            return '3%'
         if (amount >= 5001 and amount <= 10000):
            return '4%'
        if (amount > 10000):
            return '5%'

    else if (state == "MO"):
        if (amount > 0 and amount < 99):
            return '0%'
        if (amount >= 100 and amount <= 1000):
            return '1.5%'
        if (amount >= 1001 and amount <= 2000):
            return '2%'
        if (amount >= 2001 and amount <= 3000):
            return '2.5%'
        if (amount >= 3001 and amount <= 4000):
            return '3%'
        if (amount >= 4001 and amount <= 5000):
            return '3.5%'
        if (amount >= 5001 and amount <= 6000):
            return '4%'
        if (amount >= 6001 and amount <= 7000):
            return '4.5%'
        if (amount >= 7001 and amount <= 8000):
            return '5%'
        if (amount >= 8001 and amount <= 9000):
            return '5.5%'
        if (amount > 9001):
            return '6%'

    else if (state == "MT"):
        if (amount > 0 and amount < 2800):
            return '1%'
        if (amount >= 2801 and amount <= 5000):
            return '2%'
        if (amount >= 5001 and amount <= 7600):
            return '3%'
        if (amount >= 76001 and amount <= 10300):
            return '4%'
        if (amount >= 10301 and amount <= 13300):
            return '5%'
        if (amount >= 13301 and amount <= 17100):
            return '6%'
        if (amount >= 17101):
            return '6.95%'

    else if (state == "NE"):
        if (amount > 0 and amount < 3050):
            return '2.46%'
        if (amount >= 3051 and amount <= 18280):
            return '3.51%'
        if (amount >= 18281 and amount <= 29460):
            return '5.01%'
        if (amount >= 29461):
            return '6.84%'

    else if (state == "NJ"):
        if (amount > 0 and amount < 20000):
            return '1.4%'
        if (amount >= 20001 and amount <= 35000):
            return '1.75%'
        if (amount >= 35001 and amount <= 40000):
            return '3.5%'
        if (amount >= 40001 and amount <= 75000):
            return '5.525%'
        if (amount >= 75001 and amount <= 500000):
            return '6.37%'
        if (amount >= 500001 and amount <= 5000000):
            return '8.97%'
        if (amount >= 5000001):
            return '10.75%'

    else if (state == "NM"):
        if (amount > 0 and amount < 5500):
            return '1.7%'
        if (amount >= 5501 and amount <= 11000):
            return '3.2%'
        if (amount >= 11001 and amount <= 16000):
            return '4.7%'
        if (amount >= 16001):
            return '4.9%'

    else if (state == "NY"):
        if (amount > 0 and amount < 8500):
            return '4%'
        if (amount >= 8501 and amount <= 11700):
            return '4.5%'
        if (amount >= 11701 and amount <= 13900):
            return '5.25%'
        if (amount >= 13901 and amount <= 21400):
            return '5.9%'
        if (amount >= 21401 and amount <= 80650):
            return '6.33%'
        if (amount >= 80651 and amount <= 215400):
            return '6.57%'
        if (amount >= 215401 and amount <= 1077550):
            return '6.85%'
        if (amount >= 1077550):
            return '8.82%'

    else if (state == "ND"):
        if (amount > 0 and amount < 40125):
            return '1.1%'
        if (amount >= 40126 and amount <= 97150):
            return '2.04%'
        if (amount >= 97151 and amount <= 202650):
            return '2.27%'
        if (amount >= 202651 and amoutn <= 440600):
            return '2.64%'
        if (amount >= 440601):
            return '2.9%'

    else if (state == "OH"):
        if (amount > 0 and amount < 5200):
            return '0.495%'
        if (amount >= 5201 and amount <= 10400):
            return '0.99%'
        if (amount >= 10401 and amount <= 15650):
            return '1.98%'
        if (amount >= 15651 and amoutn <= 20900):
            return '2.476%'
        if (amount >= 20901 and amoutn <= 41700):
            return '2.969%'
        if (amount >= 41701 and amoutn <= 83350):
            return '3.465%'
        if (amount >= 83351 and amoutn <= 104250):
            return '3.96%'
        if (amount >= 104251 and amoutn <= 208500):
            return '4.597%'
        if (amount >= 208501):
            return '4.997%'

    else if (state == "OK"):
        if (amount > 0 and amount < 1000):
            return '0.5%'
        if (amount >= 1001 and amount <= 2500):
            return '1%'
        if (amount >= 2501 and amount <= 3750):
            return '2%'
        if (amount >= 3751 and amoutn <= 4900):
            return '3%'
        if (amount >= 4901 and amoutn <= 7200):
            return '4%'
        if (amount >= 7201 and amoutn <= 8700):
            return '3.465%'
        if (amount >= 8701):
            return '5.25%'

    else if (state == "OR"):
        if (amount > 0 and amount < 3350):
            return '5%'
        if (amount >= 3351 and amount <= 8400):
            return '7%'
        if (amount >= 8401 and amount <= 125000):
            return '9%'
        if (amount >= 125001):
            return '9.9%'

    else if (state == "RI"):
        if (amount > 0 and amount < 60550):
            return '3.75%'
        if (amount >= 60551 and amount <= 137650):
            return '4.75%'
        if (amount >= 137651):
            return '5.99%'

    else if (state == "SC"):
        if (amount > 0 and amount < 2970):
            return '0%'
        if (amount >= 2971 and amount <= 5940):
            return '3%'
        if (amount >= 5941 and amount <= 8910):
            return '4%'
        if (amount >= 8911 and amoutn <= 11880):
            return '5%'
        if (amount >= 11881 and amoutn <= 14860):
            return '6%'
        if (amount >= 14861):
            return '7%'

    else if (state == "VT"):
        if (amount > 0 and amount < 37450):
            return '3.55%'
        if (amount >= 37451 and amount <= 90750):
            return '6.8%'
        if (amount >= 90751 and amount <= 189300):
            return '7.8%'
        if (amount >= 189301 and amoutn <= 411500):
            return '8.8%'
        if (amount >= 411501):
            return '8.95%'

    else if (state == "VA"):
        if (amount > 0 and amount < 3000):
            return '2%'
        if (amount >= 3001 and amount <= 5000):
            return '3%'
        if (amount >= 5001 and amount <= 17000):
            return '5%'
        if (amount >= 17001):
            return '5.75%'

    else if (state == "WV"):
        if (amount > 0 and amount < 10000):
            return '3%'
        if (amount >= 10001 and amount <= 25000):
            return '4%'
        if (amount >= 25001 and amount <= 40000):
            return '4.5%'
        if (amount >= 40001 and amoutn <= 60000):
            return '6%'
        if (amount >= 60001):
            return '6.5%'

    else if (state == "WI"):
        if (amount > 0 and amount < 11090):
            return '4%'
        if (amount >= 11091 and amount <= 22190):
            return '5.84%'
        if (amount >= 22191 and amount <= 244270):
            return '6.27%'
        if (amount >= 244271):
            return '7.65%'
    else {
        return 'Invalid State'
    }
def calculateValue(state, amount):
    rate = findTaxRate(state, amount)
    if (rate == 'Invalid State'):
        return 'Invalid State'
    rate = rate[:-1]
    rateValue = int(rate)
    amount = (amount * rateValue/100)
    return str(amount)
