import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
d = webdriver.Chrome(options=options)

d.maximize_window()
d.get("https://rahulshettyacademy.com/AutomationPractice/")

d.find_element(By.XPATH,'//input[@value="radio2"]').click()
#d.find_element(By.CSS_SELECTOR,'input[name="checkBoxOption3"]').click()
#d.find_element(By.CSS_SELECTOR,'input[name="checkBoxOption2"]').click()
#d.find_element(By.ID,"autocomplete").send_keys("India")

#AUTOCOMPLETE TEXTBOX
d.find_element(By.ID,'autocomplete').send_keys("In")
time.sleep(2)
Coun_ist = d.find_elements(By. XPATH,'//ul[@id="ui-id-1"]//li')
print(len(Coun_ist))
for coun in Coun_ist:
    #if "India" in coun.text:
    if coun.text == "India":
        coun.click()

print(d.find_element(By.ID,'autocomplete').get_attribute("value"))

assert d.find_element(By.ID,'autocomplete').get_attribute("value") == "India"

cb = d.find_elements(By.XPATH,'//input[@type="checkbox"]')
for cbs in cb:
    if cbs.get_attribute("value") == "option2":
        cbs.click()
        assert cbs.is_selected()
        break

