from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Linkedin:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Chrome()
    
    def login(self):
        bot=self.bot
        bot.get("https://www.linkedin.com/uas/login")
        time.sleep(3)
        email=bot.find_element_by_id("username")
        email.send_keys(self.username)
        password=bot.find_element_by_id("password")
        password.send_keys(self.password)
        time.sleep(3)
        password.send_keys(Keys.RETURN)
    
load=Linkedin("your_email","your_password")
load.login()
