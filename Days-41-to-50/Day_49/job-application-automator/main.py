import os
import time
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

browser.get('https://www.linkedin.com/jobs/search/?currentJobId=3454493835&distance=100'
            '&f_AL=true&f_E=1%2C2%2C3&geoId=105818291&keywords=desenvolvedor%20python'
            '&location=Belo%20Horizonte%2C%20Minas%20Gerais%2C%20Brasil&refresh=true&sortBy=R')

# Signing in to LinkedIn
sign_in_button = browser.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in_button.click()

my_email = os.environ['EMAIL']
my_password = os.environ['PASSWORD']

username_input = browser.find_element(By.ID, 'username')
username_input.send_keys(my_email)
time.sleep(2)

password_input = browser.find_element(By.ID, 'password')
password_input.send_keys(my_password)
time.sleep(2)

sign_in_button = browser.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()

# Applying for the job
time.sleep(5)
easy_apply_button = browser.find_element(By.CLASS_NAME, 'artdeco-button__text')
easy_apply_button.click()
