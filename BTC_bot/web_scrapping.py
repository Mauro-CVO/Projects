import api_key
import requests
# from coinmarketcap import Market

def scrap():
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key.key
    }

    parameters = {
    'start':'1',
    'limit':'20',
    'convert':'MXN'
    }

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    json = requests.get(url, params= parameters, headers=headers).json()

    coins = json['data']

    value = [[i['symbol'],i['quote']['MXN']['price']] for i in coins if
    i['symbol'] == 'BTC' or i['symbol'] == 'ETH' or i['symbol'] == 'DOGE' ]
    #print(value)
    return value

if __name__ == '__main__':
    scrap()