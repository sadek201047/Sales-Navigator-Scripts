import os, csv, time, winsound, requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


"""log into website"""

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.execute_script("window.open('about:blank', 'tab1');") 
driver.execute_script("window.open('about:blank', 'tab2');")
driver.execute_script("window.open('about:blank', 'tab3');")
driver.execute_script("window.open('about:blank', 'tab4');")
driver.execute_script("window.open('about:blank', 'tab5');")
driver.execute_script("window.open('about:blank', 'tab6');")
driver.execute_script("window.open('about:blank', 'tab7');")
driver.execute_script("window.open('about:blank', 'tab8');")
driver.execute_script("window.open('about:blank', 'tab9');")
driver.execute_script("window.open('about:blank', 'tab10');")

input('press Ok')
with open('book1.csv', 'r') as csv_file:
       csv_reader = csv.reader(csv_file)
       links = list(csv_reader)

x = -1

while x < len(links):
  for i in range(1,11):
   	 x = x + 1
   	 driver.switch_to.window("tab"+str(i))
   	 driver.get(links[x][0])
   	 time.sleep(1)

  for f in range(1,11):
    driver.switch_to.window("tab"+str(f))
    try:
         check_saved = driver.find_elements_by_xpath('//span[@class="profile-topcard-actions__unsave-lead-secondary ph2"]')
         if len(check_saved) == 0:
            Button = driver.find_element_by_xpath('//button[@class="save-to-list-dropdown__trigger__profile t-16"]')
            Button.click()
            time.sleep(2)
            Button2 = driver.find_element_by_xpath('//artdeco-dropdown-item[@class="a11y-artdeco-dropdown ember-view"]')
            Button2.click()
            time.sleep(1)
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
