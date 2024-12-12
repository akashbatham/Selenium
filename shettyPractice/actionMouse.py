from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
d = webdriver.Chrome(options = options)

d.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(d)
#Action class helps to move around in the webpage and let you perform mouse functions
#It has actions like double click, move to element, context click(Right click) and many more
#The action statment always ends with perform() method
action.move_to_element(d.find_element(By.ID,"mousehover")).perform() #Mouse hover on an element
action.context_click(d.find_element(By.LINK_TEXT,"Top")).perform() #Right Click