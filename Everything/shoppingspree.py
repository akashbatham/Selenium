import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

total_sum=0
product_name = "Raspberry - 1/4 Kg"

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
d = webdriver.Chrome(options=options)
d.implicitly_wait(5)

d.get("https://rahulshettyacademy.com/seleniumPractise/")
d.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("er")
time.sleep(2)

vegs = d.find_elements(By.XPATH,'//h4[@class="product-name"]')
for name in vegs:
    acc = name.text
    print(acc)
    if "Raspberry - 1/4 Kg" in acc:
        indexo = vegs.index(name)
        stats = indexo+1
        d.find_element(By.XPATH, '//div[@class="products"]//div' + str([stats]) + '//a[2]').click()

veglist = ["Cauliflower - 1 Kg", "Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg","Water Melon - 1 Kg"]
vegs = d.find_elements(By.XPATH,'//h4[@class="product-name"]')
if vegs == veglist:
    print("Matching List")
else:
    print("Lists don't match")

time.sleep(5)

atc2 = d.find_elements(By.XPATH,'//div[@class="products"]/div')
for sound in atc2:
    sound.find_element(By.XPATH,'div/button').click()
    sound.find_element(By.XPATH,'h4')

# atc = d.find_elements(By.XPATH,'//button[text()="ADD TO CART"]')
# cou = len(atc)
# print(cou)
# for acts in atc:
#     if acts.text == "ADD TO CART":
#         acts.click()
time.sleep(2)

d.find_element(By.XPATH,'//img[@alt="Cart"]').click()
d.find_element(By.XPATH,'//button[text()="PROCEED TO CHECKOUT"]').click()

#Inside Cart
ele = d.find_element(By.XPATH,'//table[@class="cartTable"]/thead/tr/td[3]/b').text
if ele!= "Quantity":
    print("Change the title to Quantity")

d.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
d.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(d,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(d.find_element(By.CSS_SELECTOR,".promoInfo").text)
strcount = d.find_elements(By.XPATH, '//table[@class="cartTable"]//tbody//td[5]')

fulprice = 0
for i in strcount:
    fulprice = fulprice + int(i.text)
print(fulprice)

totcount = d.find_element(By.CLASS_NAME, "totAmt").text
finalcount = int(totcount)
if finalcount != fulprice:
    print("test pass")

d.find_element(By.XPATH,"//button[text()='Place Order']").click()