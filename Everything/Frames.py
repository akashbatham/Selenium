import time
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_experimental_option("excludeSwitches",["enable-automation"])
d = webdriver.Chrome(options=options)

d.get("https://ui.vision/demo/webtest/frames/")
d.switch_to.frame(d.find_element(By.XPATH,'//frame[@src="frame_5.html"]'))
d.find_element(By.LINK_TEXT,"https://a9t9.com").click()
time.sleep(5)
d.find_element(By.XPATH,'//a[@id="logo"]')
