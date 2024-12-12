##CHAINING OF WEBELEMENTS

#You can create a child Xpath for an already existing Xpath
#For example
#You have created a list of xpaths
#Then you can create a for loop to move through the list while creating a xpath in continuation to the main xpath

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

veglist = ["Cauliflower - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg","Water Melon - 1 Kg", "Cucumber - 1 Kg"]
actuallist = []

total_sum=0
product_name = "Raspberry - 1/4 Kg"

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
d = webdriver.Chrome(options=options)
d.implicitly_wait(5)

d.get("https://rahulshettyacademy.com/seleniumPractise/")
d.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("er")
time.sleep(3)

atc2 = d.find_elements(By.XPATH,'//div[@class="products"]/div')
for sound in atc2:
    actuallist.append(sound.find_element(By.XPATH, 'h4').text)
    sound.find_element(By.XPATH,'div/button').click()

assert sorted(actuallist) == sorted(veglist)
if actuallist == veglist:
    print("List matches")

# wait = WebDriverWait(d,10)
# wait.until(expected_conditions.presence_of_element_located(("XPATH")))