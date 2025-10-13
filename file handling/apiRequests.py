import requests
import json

api_url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(api_url)

print(response.json())