import requests

url = "https://fakestoreapi.com/products"

responses = requests.get(url)
print(responses.json())