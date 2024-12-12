from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach",True)
d = webdriver.Chrome(options = Options)

d.implicitly_wait(10)

wait = WebDriverWait(d,10)

wait.until(EC.presence_of_element_located(("XPATH")))

d.get()