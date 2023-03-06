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
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument(f'user_agent={user_agent}')
browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

browser.get('https://python.org')
upcoming_events = {}

key = 0
events_menu = browser.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
events_fields = events_menu.find_elements(By.TAG_NAME, 'li')

for event in events_fields:
    event_details = {
        'time': event.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split('T')[0],
        'name': event.find_element(By.TAG_NAME, 'a').text
    }
    upcoming_events[key] = event_details
    key += 1

print(upcoming_events)
