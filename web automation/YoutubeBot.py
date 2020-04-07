from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class YoutubeBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Firefox()
        
    def login(self):
        bot=self.bot
        bot.get('https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3D%252F&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        time.sleep(2)
        email=bot.find_element_by_id('identifierId')
        email.send_keys(self.username)
        time.sleep(3)
        email.send_keys(Keys.RETURN)
        time.sleep(2)
        password=bot.find_element_by_name('password')
        password.send_keys(self.password)
        time.sleep(2)
        password.send_keys(Keys.RETURN)

load=YoutubeBot("Your_Email","Your_Password")
load.login()
