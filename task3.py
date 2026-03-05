import requests

req = requests.get("https://api.github.com")

print("Headers:")
print(req.headers, "\n")

print("Date header:")
print(req.headers["Date"],"\n")

print("Body:")
print(req.text)