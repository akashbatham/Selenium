import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#servJQ = Service("C:\\akashPython\\selenium\\drivers\\chromedriver.exe")
#driver = webdriver.Chrome(service = servJQ)


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID,"autosuggest").send_keys("In")
time.sleep(2)
lis = driver.find_elements(By.XPATH, '//li[@role="presentation"]/a')
print(len(lis))

for word in lis:
    if "Faso" in word.text:
        word.click()
        time.sleep(10)