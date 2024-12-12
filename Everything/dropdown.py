from selenium import webdriver

class dropdown:
    def dropdwn(self):
        d = webdriver.Chrome()
        d.get("https://www.google.com")

cobj = dropdown()
cobj.dropdwn()