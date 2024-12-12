import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
d = webdriver.Chrome(options=options)

d.get("https://testautomationpractice.blogspot.com/")
d.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("apple")
d.find_element(By.XPATH, '//span/input[@type="submit"]').click()
time.sleep(3)

listed = d.find_elements(By.ID, "wikipedia-search-result-link")
print(len(listed))
for txt in listed:
    print()


print("output")
