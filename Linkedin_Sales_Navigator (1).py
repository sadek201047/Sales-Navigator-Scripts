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
        profiles = soup.find_all('div', class_='horizontal-person-entity-lockup-4 result-lockup__entity ml4')
        profiles_list = []
        for profile in profiles:
                full_name = profile.find_all('dt', class_='result-lockup__name')
                full_name = full_name[0].text
                profile_link = profile.find_all('a')
                profile_link = profile_link[0]['href']
                company_link = profile.find_all('dd', class_='result-lockup__highlight-keyword')
                company_link = company_link[0].find_all('a')[0]['href']
                Company_name = profile.find_all('a', class_='Sans-14px-black-75%-bold')
                company_name = Company_name[0].find('span').text
                tile_name = profile.find_all('span', class_='t-14 t-bold')
                tile_name = tile_name[0].text
                row = full_name.replace("\n", "") + ' # ' + company_name.replace("\n", "") + "#" + tile_name.replace("\n", "") + ' # ' + 'https://www.linkedin.com' + profile_link +   ' # ' + 'https://www.linkedin.com' + company_link
                print(row)

