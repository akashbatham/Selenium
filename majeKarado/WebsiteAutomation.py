from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = Options()
options.add_experimental_option("detach", True)
d = webdriver.Chrome(options=options)
d.maximize_window()

d.get("https://rahulshettyacademy.com/loginpagePractise/")
d.find_element(By.XPATH,'//a[@target="_blank"]').click()

windows = d.window_handles

d.switch_to.window(windows[1])
texreq = d.find_element(By.XPATH,'//p[@class="im-para red"]/strong/a').text
print(texreq)

d.switch_to.window(windows[0])
d.find_element(By.ID,"username").send_keys(texreq)
d.find_element(By.ID,"password").send_keys("password")

d.find_element(By.ID,"terms").click()
d.find_element(By.ID,"signInBtn").click()
wait = WebDriverWait(d,10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.alert-danger')))
inte = d.find_element(By.CSS_SELECTOR,'.alert-danger').text
print(inte)