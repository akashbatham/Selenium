from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach",True)
options.add_argument('disable-infobars')
d = webdriver.Chrome(options=options)
d.maximize_window()
action = ActionChains(d)
#This statement is used to change the page resolution not the driver resolution
#d.execute_script("document.body.style.zoom = '75%'")
sleep(5)
d.get("https://www.allballapp.com/")
d.find_element(By.XPATH,'//span[contains(text(),"Discover the All Ball web app")]').click()
sleep(2)
d.find_element(By.XPATH,'//a[@class = "d-none d-md-block"]').click()
sleep(1)
d.find_element(By.ID,"input-loginemail").send_keys("akash_batham@softprodigy.com")
d.find_element(By.ID,"input-loginPassword").send_keys("Softprodigy@123")
d.find_element(By.XPATH,'//button[@class = "w-100 btn btn-lg btn-primary"]').click()
sleep(5)
eveClick = d.find_element(By.XPATH,'//span[contains(text(),"Devin March Test")]')
sleep(5)
action.click(on_element=eveClick).perform()
sleep(2)
d.find_element(By.XPATH,'//a[contains(text(),"Event Schedule")]').click()
sleep(2)
d.find_element(By.XPATH,'//span[contains(text(),"Event Scheduler")]').click()
sleep(5)
paths = d.find_elements(By.XPATH,'//div[@data-targetcourtid="6639325d5d7d6fcbe886dcd5"]')