import requests

url = "https://api.github.com"

try:
    response = requests.get(url)
    print("Status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Connection error:", e)