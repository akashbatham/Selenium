from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach",True)
d = webdriver.Chrome(options = options)
d.maximize_window()

d.get("https://rahulshettyacademy.com/dropdownsPractise/")
d.find_element(By.XPATH,'//input[@id="autosuggest"]').send_keys("IN")
sleep(3)
places = d.find_elements(By.XPATH,'//ul[@id="ui-id-1"]/li/a')
for a in places:
    country = a.text
    if country == "India":
        a.click()
d.find_element(By.XPATH,'//a[@id="hlnkholidaypacks"]').click()
sleep(2)
d.find_element(By.ID,"ctl00_mainContent_HolidayPackages_DropDownListPackage_CTXT").click()
sleep(2)
cities = d.find_elements(By.XPATH,'//div[@id="dropdownGroup1"]/div/ul/li/a')
for city in cities:
    sites = city.text
    if sites == "Gulmarg":
        city.click()
sleep(2)
d.find_element(By.ID,"ctl00_mainContent_HolidayPackages_DropDownListFrom_CTXT").click()
sleep(2)
citiesTwo = d.find_elements(By.XPATH,'//div[@id="dropdownGroup1"]/div/ul/li/a')
for cityTwo in citiesTwo:
    sitesTwo = cityTwo.text
    if sitesTwo == "Jammu":
        cityTwo.click()
sleep(2)
d.find_element(By.ID,"ctl00_mainContent_HolidayPackages_TxtTravelDate").click()

#Year change code
year = d.find_element(By.XPATH,'//span[@class="ui-datepicker-year"]').text
while year != "2026":
    d.find_element(By.XPATH,'//a[@title="Next"]').click()
    sleep(2)
    year = d.find_element(By.XPATH, '//span[@class="ui-datepicker-year"]').text

#Month change code
month = d.find_element(By.XPATH,'//span[@class="ui-datepicker-month"]').text
while month != "June":
    d.find_element(By.XPATH,'//a[@title="Next"]').click()
    sleep(2)
    month = d.find_element(By.XPATH,'//span[@class="ui-datepicker-month"]').text
print(year, month)

dates = d.find_elements(By.XPATH,'//table[@class="ui-datepicker-calendar"]/tbody/tr/td/a')
for date in dates:
    dat = date.text
    if dat == "18":
        date.click()