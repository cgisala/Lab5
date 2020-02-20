import requests

url = 'https://catfact.ninja/fact'

cat_data = requests.get(url).json()

print(cat_data)
print(cat_data['fact'])