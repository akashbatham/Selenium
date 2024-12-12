import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
d = webdriver.Chrome(options=options)

d.maximize_window()
d.get("https://www.globalsqa.com/demo-site/accordion-and-tabs/")

time.sleep(10)
d.find_element(By.XPATH, '//h3[@id="ui-id-3"]').click()
assert d.find_element(By.XPATH,'//h3[@aria-expanded="True"]')