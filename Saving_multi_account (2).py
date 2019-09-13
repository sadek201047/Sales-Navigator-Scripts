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
login_confirm = input("confirm login and press ok: ")

for item in range(1,10):
  browser.execute_script("window.open('about:blank', 'tab'+str(item);")
  browser.switch_to.window("tab1")


browser.switch_to.window(browser.window_handles[0])
 
#take the links from CSV as a list
with open('book1.csv', 'r') as csv_file:
       csv_reader = csv.reader(csv_file)
       links = list(csv_reader)
       
x = -1
for link in links:

	
 for i in range(2,10):
    x = x + 1
	link_0 = links[x]
	browser.get(link_0[0])
	Button = driver.find_element_by_xpath('//button[@class="save-to-list-dropdown__trigger__profile t-16"]')
    Button.click()
    time.sleep(.5)
	
	browser.switch_to.window("tab2")
	x = x + 1
	browser.get(links[x][0])
	Button = driver.find_element_by_xpath('//button[@class="save-to-list-dropdown__trigger__profile t-16"]')
    Button.click()
    time.sleep(.5)

	
	browser.switch_to.window("tab3")
	x = x + 1
	browser.get(links[x][0])
	Button = driver.find_element_by_xpath('//button[@class="save-to-list-dropdown__trigger__profile t-16"]')
    Button.click()
    time.sleep(.5)


	browser.switch_to.window("tab4")
	x = x + 1
	browser.get(links[x][0])
	Button = driver.find_element_by_xpath('//button[@class="save-to-list-dropdown__trigger__profile t-16"]')
    Button.click()
    time.sleep(.5)


	browser.switch_to.window("tab5")
	x = x + 1
	browser.get(links[x][0])
	Button = driver.find_element_by_xpath('//button[@class="save-to-list-dropdown__trigger__profile t-16"]')
    Button.click()
    time.sleep(.5)


    browser.switch_to.window("tab6")
    x = x + 1
    browser.get(links[x][0])
    Button = driver.find_element_by_xpath('//button[@class="save-to-list-dropdown__trigger__profile t-16"]')
    Button.click()
    time.sleep(.5)


    browser.switch_to.window("tab7")
    x = x + 1
    browser.get(links[x][0])
    Button = driver.find_element_by_xpath('//button[@class="save-to-list-dropdown__trigger__profile t-16"]')
    Button.click()
    time.sleep(.5)

    browser.switch_to.window("tab8")
    x = x + 1
    browser.get(links[x][0])
    Button = driver.find_element_by_xpath('//button[@class="save-to-list-dropdown__trigger__profile t-16"]')
    Button.click()
    time.sleep(.5)


    browser.switch_to.window("tab9")
    x = x + 1
    browser.get(links[x][0])
    Button = driver.find_element_by_xpath('//button[@class="save-to-list-dropdown__trigger__profile t-16"]')
    Button.click()
    time.sleep(.5)


    browser.switch_to.window(browser.window_handles[0])
    Button2 = driver.find_element_by_xpath('//artdeco-dropdown-item[@class="a11y-artdeco-dropdown ember-view"]')
    Button2.click()
    time.sleep(.25)

    browser.switch_to.window("tab2")
    Button2 = driver.find_element_by_xpath('//artdeco-dropdown-item[@class="a11y-artdeco-dropdown ember-view"]')
    Button2.click()
    time.sleep(.25)

    browser.switch_to.window("tab3")
    Button2 = driver.find_element_by_xpath('//artdeco-dropdown-item[@class="a11y-artdeco-dropdown ember-view"]')
    Button2.click()
    time.sleep(.25)

    browser.switch_to.window("tab4")
    Button2 = driver.find_element_by_xpath('//artdeco-dropdown-item[@class="a11y-artdeco-dropdown ember-view"]')
    Button2.click()
    time.sleep(.25)

    browser.switch_to.window("tab5")
    Button2 = driver.find_element_by_xpath('//artdeco-dropdown-item[@class="a11y-artdeco-dropdown ember-view"]')
    Button2.click()
    time.sleep(.25)

    browser.switch_to.window("tab6")
    Button2 = driver.find_element_by_xpath('//artdeco-dropdown-item[@class="a11y-artdeco-dropdown ember-view"]')
    Button2.click()
    time.sleep(.25)

    browser.switch_to.window("tab7")
    Button2 = driver.find_element_by_xpath('//artdeco-dropdown-item[@class="a11y-artdeco-dropdown ember-view"]')
    Button2.click()
    time.sleep(.25)

    browser.switch_to.window("tab8")
    Button2 = driver.find_element_by_xpath('//artdeco-dropdown-item[@class="a11y-artdeco-dropdown ember-view"]')
    Button2.click()
    time.sleep(.25)

    browser.switch_to.window("tab9")
    Button2 = driver.find_element_by_xpath('//artdeco-dropdown-item[@class="a11y-artdeco-dropdown ember-view"]')
    Button2.click()
    time.sleep(.25)

    input('press Enter after completed')   
        

