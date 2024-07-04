

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_driver_path = r"C:\Users\kiran\Downloads\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome()

driver.get('https://www.readwhere.com')
driver.find_element(By.XPATH, '//a[@id="rw_login_btn"]').click()


print(driver.title)
print(driver.current_url)
time.sleep(6)
