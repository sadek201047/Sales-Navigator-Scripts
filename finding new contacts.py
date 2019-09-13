import os
import csv
import time
import winsound
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def slow_page_scrolldown():
        browser.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 1500)")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 2000)")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 2500)")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 3000)")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 3500)")
        time.sleep(.5)
        browser.execute_script("window.scrollTo(0, 4000)")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 4500)")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 5000)")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 5700)")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 6000)")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 6500)")
        time.sleep(1)

def fast_page_scrolldown():
        browser.execute_script("window.scrollTo(0, 1500)")
        time.sleep(2)
        browser.execute_script("window.scrollTo(0, 3000)")
        time.sleep(2)
        browser.execute_script("window.scrollTo(0, 4500)")
        time.sleep(2)
        browser.execute_script("window.scrollTo(0, 6500)")
        time.sleep(2)


"""log into website"""

browser = webdriver.Chrome()
browser.get("https://www.linkedin.com/") 
time.sleep(5)
login_confirm = input("Please open connections page and scroll down: ")
 

html_source = browser.page_source
soup = BeautifulSoup(html_source, 'html.parser')
new_contacts = soup.find_all('div', class_='mn-connection-card__details')
for profile in new_contacts:
        profile_link = profile.find_all('a')[0]['href']
        profile_link = "https://www.linkedin.com" + profile_link
        profile_name = profile.find('span', class_='mn-connection-card__name t-16 t-black t-bold').text
        profile_title = profile.find('span', class_='mn-connection-card__occupation t-14 t-black--light t-normal').text
        profile_time = profile.find('time', class_='time-badge time-ago').text
        row = profile_link + ' # ' + profile_name.replace("\n", "") + "#" + profile_title.replace("\n", "") + ' # ' + profile_time.replace("\n", "")
        print(row)

