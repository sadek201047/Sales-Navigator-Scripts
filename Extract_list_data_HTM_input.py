import os
import csv
import time
import winsound
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""log into website"""

browser = webdriver.Chrome()
browser.get("https://www.linkedin.com/") 
time.sleep(5)
login_confirm = input("confirm login and press ok: ")

       



def findit():
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    next_button = soup.find_all(class_='next-text')
    profiles = soup.find_all('tr', class_='artdeco-table-row unselected')
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
