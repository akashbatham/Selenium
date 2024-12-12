import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
d = webdriver.Chrome(options=options)

d.get("https://candymapper.com/")
time.sleep(3)

d.find_element(By.ID,'popup-widget238491-close-icon').click()