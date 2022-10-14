import requests
class CommodityData:
    

    base_currency = 'USD'
    symbol = 'XAU' 
    endpoint = 'latest'
    access_key = 'zlksliz38pfu59i5qiapo815taa1g783gxu0dh6e083wevv80860yg2j13gw'

    resp = requests.get(
        'https://commodities-api.com/api/'+endpoint+'?access_key='+access_key+'&base='+base_currency+'&symbols='+symbol)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /'+endpoint+'/ {}'.format(resp.status_code))
    print(resp.json())