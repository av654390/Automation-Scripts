from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
def check_url_chrome_selenium(url, timeout=5):
  """
  Checks if a URL is reachable by opening it in Chrome using Selenium.
 
  Args:
      url: The URL to check.
      timeout: Maximum wait time in seconds for the page to load (default: 5).
 
  Returns:
      True if the URL is reachable and the page loads within the timeout, False otherwise.
  """
  try:
    driver = webdriver.Chrome(ChromeDriverManager().install())  # Replace with your preferred path if needed
    driver.set_page_load_timeout(timeout)
    driver.get(url)
    driver.quit()
    return True
  except TimeoutException:
    print(f"URL {url} timed out after {timeout} seconds.")
    return False
  except Exception as e:
    print(f"Error checking URL: {e}")
    return False
 
# Example usage
specific_url = "https://us6salxrpp102.corpnet2.com:59001/nwa"  # Replace with the desired URL
if check_url_chrome_selenium(specific_url):
  print(f"URL {specific_url} is reachable.")
else:
  print(f"URL {specific_url} is unreachable.")