

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_driver_path = r"C:\Users\kiran\Downloads\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome()

driver.get('https://www.readwhere.com')
driver.find_element(By.XPATH, '//a[@id="rw_login_btn"]').click()


print(driver.title)
print(driver.current_url)
time.sleep(2)
driver.switch_to.frame(0)
driver.find_element_by_xpath('//*[@id="resend"]').send_keys('kiransaraswat2803@gmail.com')
driver.find_element_by_xpath('//input[@id="signinform-password"]').send_keys('123456')
driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()
driver.find_element(By.ID,"newspaper_btn").click()
time.sleep(6)
