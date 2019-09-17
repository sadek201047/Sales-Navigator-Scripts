import os, csv, time, winsound, requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


"""log into website"""

browser = webdriver.Chrome()
browser.get("https://www.google.com/")
browser.execute_script("window.open('about:blank', 'tab1');") 
browser.execute_script("window.open('about:blank', 'tab2');")
browser.execute_script("window.open('about:blank', 'tab3');")
browser.execute_script("window.open('about:blank', 'tab4');")
browser.execute_script("window.open('about:blank', 'tab5');")
browser.execute_script("window.open('about:blank', 'tab6');")
browser.execute_script("window.open('about:blank', 'tab7');")
browser.execute_script("window.open('about:blank', 'tab8');")
browser.execute_script("window.open('about:blank', 'tab9');")
browser.execute_script("window.open('about:blank', 'tab10');")

browser.switch_to.window(browser.window_handles[0])

with open('book1.csv', 'r') as csv_file:
       csv_reader = csv.reader(csv_file)
       links = list(csv_reader)

x = -1

while x > len(links):
  for i in range(0,11):
   	 x = x + 1
   	 browser.switch_to.window("tab"+str(i))
	 browser.get(links[x][0])