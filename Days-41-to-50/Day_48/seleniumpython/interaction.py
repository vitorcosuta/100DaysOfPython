import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
             ' Chrome/110.0.0.0 Safari/537.36'
driver_path = r'C:\Development\chromedriver.exe'
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument(f'user_agent={user_agent}')
browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

browser.get('https://en.wikipedia.org/wiki/Main_Page')

number_of_articles = browser.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text
print(number_of_articles)