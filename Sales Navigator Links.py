import os, csv, time, winsound, requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


"""log into website"""

browser = webdriver.Chrome()
browser.get("https://www.linkedin.com/") 
login_confirm = input("confirm login and press ok: ")


with open('book1.csv', 'r') as csv_file:
       csv_reader = csv.reader(csv_file)
       links = list(csv_reader)

"""Finding element by class with selenium has not worked"""
for link in links:
    browser.get(link[0])
    time.sleep(2)
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    Button = soup.find('button', class_='pv-s-profile-actions pv-s-profile-actions--view-profile-in-sales-navigator ml2 artdeco-button artdeco-button--2 artdeco-button--secondary ember-view')
    #Button = browser.find_element_by_class('pv-s-profile-actions pv-s-profile-actions--view-profile-in-sales-navigator ml2 artdeco-button artdeco-button--2 artdeco-button--secondary ember-view')
    Button2 = '//*[@id="'+ Button['id']+'"]'
    browser.find_element_by_xpath(Button2).click()
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(3)
    print(browser.current_url)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
