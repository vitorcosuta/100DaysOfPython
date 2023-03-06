import selenium.common.exceptions
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
             ' Chrome/110.0.0.0 Safari/537.36'
driver_path = r'C:\Development\chromedriver.exe'
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument(f'user_agent={user_agent}')
browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

browser.get('https://orteil.dashnet.org/experiments/cookie/')

cookie_button = browser.find_element(By.ID, 'cookie')

timeout = time.time() + 60*5
buy_upgrade_interval = time.time() + 5
while True:

    if time.time() > timeout:
        break

    if time.time() > buy_upgrade_interval:
        current_money = int(browser.find_element(By.ID, 'money').text.replace(',', '_'))
        upgrade_store = browser.find_element(By.ID, 'store')
        upgrades = upgrade_store.find_elements(By.TAG_NAME, 'div')

        for upgrade in upgrades[::-1]:  # Accessing the upgrades on reverse to buy the most expensive one if possible
            try:
                upgrade_cost = upgrade.find_element(By.TAG_NAME, 'b').text
            except selenium.common.exceptions.NoSuchElementException:
                pass
            else:
                if upgrade_cost != '':
                    upgrade_cost = int(upgrade_cost.split('-')[1].strip().replace(',', '_'))
                    if upgrade_cost <= current_money:
                        upgrade.click()
                        break

        buy_upgrade_interval = time.time() + 5

    cookie_button.click()
