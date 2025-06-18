import requests
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress only the InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)

def check_url(url):
    try:
        # Set a User-Agent to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        }
        
        # Use a session to maintain cookies
        with requests.Session() as session:
            response = session.get(url, headers=headers, verify=False, timeout=10)
            print("Status Code:", response.status_code)
            if response.status_code == 200:
                print("Success! Access granted.")
            else:
                print("Failed to access the URL. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

if __name__ == "__main__":
    url = "http://us6sdlxvep101.corpnet2.com:8095/oseries-auth/login"
    
    check_url(url)
