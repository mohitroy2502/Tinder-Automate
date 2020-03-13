# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
from time import sleep

from secrets import *

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe')
        
    def login(self):
        self.driver.get("https://tinder.com")
        
        sleep(10)
        
        #more_option = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/button')
        #more_option.click()
        
        fb_link = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_link.click()
        
        base_window = self.driver.window_handles[0]
        
        self.driver.switch_to_window(self.driver.window_handles[1])
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        
        
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)
        
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        
        self.driver.switch_to_window(base_window)
        
        popup1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup1.click()
        
        popup2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup2.click()
        
        
    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()
            
    def unlike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()
            
    def autoswipe():
        while True:
            sleep(0.5)
            self.like()
        
bot = TinderBot()
bot.login()