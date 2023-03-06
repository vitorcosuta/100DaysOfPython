import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Initializing Chrome service
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
             ' Chrome/110.0.0.0 Safari/537.36'
driver_path = r'C:\Development\chromedriver.exe'
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)  # We need to add this to prevent browser from closing by itself
chrome_options.add_argument(f'user_agent={user_agent}')
browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigating to a website
browser.get('https://www.amazon.com/Brave-New-World-Aldous-Huxley/dp/0060850523/ref=sr_1_1?crid=125NNCI2QXKTV')

# Finding the product price by CSS SELECTOR
price_field = browser.find_element(By.CSS_SELECTOR, '.swatchElement.selected span span span a span span')
print(price_field.text)

# Finding the product price by XPATH (VERY USEFUL)
price_field = browser.find_element(By.XPATH, '//*[@id="a-autoid-8-announce"]/span[2]/span')
print(price_field.text)

# Finding input field by NAME
# browser.get('https://python.org')
# search_field = browser.find_element(By.NAME, 'q')
# print(search_field.get_attribute('placeholder'))

# Finding website logo by CLASS
# python_logo = browser.find_element(By.CLASS_NAME, 'python-logo')
# print(python_logo.size)

# browser.close()  # Closes a particular tab
# browser.quit()  # Shuts down the entire browser
