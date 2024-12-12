from selenium import webdriver

class dropdown:
    def dropdwn(self):
        d = webdriver.Chrome()
        d.get("https://www.facebook.com")
        d.implicitly_wait(5)

    def my_firstMethod(self,name):
        print(f"Hello",{name})

cobj = dropdown()
cobj.dropdwn()
cobj.my_firstMethod("Catastrophe")