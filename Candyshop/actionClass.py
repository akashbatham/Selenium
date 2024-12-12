from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach",True)
d = webdriver.Chrome(options = options)
d.maximize_window()
action = ActionChains(d)
d.get("https://rahulshettyacademy.com/dropdownsPractise/")
sleep(2)
d.find_element(By.ID,"hlnkholidaypacks").click()
sleep(2)
elemen = d.find_element(By.CLASS_NAME,"myspice_trip")
action.click(on_element=elemen).perform()
action.double_click(elemen)