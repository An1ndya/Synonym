import requests
import json


url = "https://api.exchangeratesapi.io/latest?symbols=USD,GBP"
 
response = requests.get(url)

data = response.text
parsed = json.loads(data)

print(json.dumps(parsed, indent=4))