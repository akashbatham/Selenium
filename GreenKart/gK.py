from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#serviceHq = Service('C:\akashPython\selenium\drivers\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
