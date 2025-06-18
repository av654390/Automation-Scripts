import requests

url = "https://us6salxrpp103.corpnet2.com:59001/nwa"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

try:
    response = requests.get(url, headers=headers,verify=False)
    if response.status_code == 200:
        print(f"{url} is reachable")
    else:
        print(f"{url} returned status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error accessing {url}: {e}")
