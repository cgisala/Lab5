import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

coin_data = requests.get(url).json()

print(coin_data)
# print(coin_data['bpi']['USD'])