from selenium import webdriver
from selenium.webdriver.common.by import By
import time

name = "Akash"
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
d = webdriver.Chrome(options=options)

d.get("https://rahulshettyacademy.com/AutomationPractice/")
d.find_element(By.ID,"name").send_keys(name)
d.find_element(By.ID,"alertbtn").click()
alert = d.switch_to.alert
alerttext = alert.text
time.sleep(2)
assert name in alerttext
alert.accept()
time.sleep(3)

d.find_element(By.ID,"name").send_keys(name)
d.find_element(By.ID,"confirmbtn").click()
alert = d.switch_to.alert
alerttext = alert.text
time.sleep(2)
assert name in alerttext
alert.dismiss()