import os
import csv
import time
import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import winsound

with open('book1.csv', 'r') as csv_file:
       csv_reader = csv.reader(csv_file)
       csv_reader2 = list(csv_reader)

#we could put all the parsing code inside here after print statement.........

driver = webdriver.Chrome()
link2 = "https://www.google.com"
input('log in')

for link in csv_reader2:
       link1 = link[0]
       driver.get(link1)
       time.sleep(2)
       try:
        check_saved = driver.find_elements_by_xpath('//span[@class="profile-topcard-actions__unsave-lead-secondary ph2"]')
        if len(check_saved) == 0:
            Button = driver.find_element_by_xpath('//button[@class="save-to-list-dropdown__trigger__profile t-16"]')
            Button.click()
            time.sleep(3)
            Button2 = driver.find_element_by_xpath('//artdeco-dropdown-item[@class="a11y-artdeco-dropdown ember-view"]')
            Button2.click()
            time.sleep(3)
            check_multi_account = driver.find_elements_by_xpath('//h2[@id="lead-cta-form__header"]')
            if len(check_multi_account) > 0:
                print('Multi_account')
                time.sleep(0)
            else:
                print('done')
                time.sleep(0)
        else:
            print('saved')
            time.sleep(0)
       except:
           print('manual_2')
           time.sleep(0)
  
