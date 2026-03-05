import requests

url = "https://httpbin.org/get"

params = {
    "name": "Jan",
    "age": 17
}

response = requests.get(url, params=params)

print(response.url)
print(response.json())