from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

user_name = " your username" #or email 
password = " your password"

driver = webdriver.Chrome() #driver = browser 
driver.get ("https://facebook.com")

element = driver.find_element_by_id("email") #will scrape by email element
element.send_keys(user_name)

element = driver.find_element_by_id("pass") #if email element found = pass 
element.send_keys(password) #browser will input your password
element.send_keys(Keys.RETURN) #browser will select enter 
element.close()