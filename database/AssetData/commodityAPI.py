  import requests

    base_currency = 'USD'
    symbol = 'XAU' 
    endpoint = 'latest'
    access_key = 'API_KEY'

    resp = requests.get(
        'https://commodities-api.com/api/'+endpoint+'?access_key='+access_key+'&base='+base_currency+'&symbols='+symbol)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /'+endpoint+'/ {}'.format(resp.status_code))
    print(resp.json())