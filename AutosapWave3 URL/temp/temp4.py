import requests
import certifi

url = "https://us6salxrpp101.corpnet2.com/nwa"
try:
    response = requests.get(url, verify=certifi.where())
    if response.status_code == 200:
        print(f"{url} is reachable")
    else:
        print(f"{url} returned status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error accessing {url}: {e}")
