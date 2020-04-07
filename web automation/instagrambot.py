from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Chrome()
    
    def login(self):
        bot=self.bot
        bot.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(2)
        email=bot.find_element_by_name('username')
        email.clear()
        email.send_keys(self.username)
        password=bot.find_element_by_name('password')
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        
        

load=Twitter("Your_Email","Your_password")
load.login()
