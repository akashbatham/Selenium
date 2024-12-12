import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
d = webdriver.Chrome(options=options)

d.get("https://rahulshettyacademy.com/AutomationPractice/")
d.find_element(By.CSS_SELECTOR,'a[id="opentab"]').click()
windowsOpened = d.window_handles

time.sleep(5)
d.switch_to.window(windowsOpened[1])
d.find_element(By.XPATH,'//a[@href="https://www.udemy.com/user/testing-minds/"]').click()
print(d.find_element(By.TAG_NAME,'h1').text)




