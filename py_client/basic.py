import requests

endpoint = "http://localhost:8000/api/"
res = requests.get(endpoint)

print(res.json())