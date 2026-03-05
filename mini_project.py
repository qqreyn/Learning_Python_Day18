import requests

base_url = "https://jsonplaceholder.typicode.com/"

endpoint = input("Choose endpoint (posts, comments, users): ")

url = base_url + endpoint

try:
    response = requests.get(url, timeout=5)

    print("\nStatus Code:")
    print(response.status_code)

    print("\nHeaders:")
    print(response.headers)

    data = response.json()

    print("\nFirst item from response:")

    if isinstance(data, list):
        item = data[0]
        for key, value in item.items():
            print(f"{key}: {value}")

except requests.exceptions.ConnectionError:
    print("Failed to connect to the server.")

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.RequestException as e:
    print("Error:", e)