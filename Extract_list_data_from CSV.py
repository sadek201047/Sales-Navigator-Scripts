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
login_confirm = input("confirm login and press ok: ")
 
#take the links from CSV as a list
with open('book1.csv', 'r') as csv_file:
       csv_reader = csv.reader(csv_file)
       links = list(csv_reader)
       


for link in links:
        link_0 = link[0]
        browser.get(link_0)
        slow_page_scrolldown()
        html_source = browser.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        next_button = soup.find_all(class_='next-text')
        profiles = soup.find_all('td', class_='artdeco-models-table-cell list-people-detail-header__entity ember-view')
        profiles_list = []
        for profile in profiles:
                full_name = profile.find_all('dt', class_='white-space-nowrap overflow-hidden text-overflow-ellipsis')
                full_name_text = full_name[0].text
                profile_link = full_name[0].find('a')['href']
                profile_link = 'https://www.linkedin.com' + profile_link
                try:
                     Company_name = profile.find(class_='artdeco-entity-lockup__title--alt-link ember-view').text
                except:
                     Company_name = "no account"   
                title = profile.find('span', class_='Sans-14px-black-90%').text
                row = full_name_text.replace("\n", "") + ' # ' + Company_name.replace("\n", "") + "#" + title.replace("\n", "") + ' # ' +  profile_link
                print(row)
