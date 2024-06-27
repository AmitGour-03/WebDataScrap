# Initiating code
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

query = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=1SQAEFHO42WD4&sprefix=laptop%2Caps%2C302&ref=nb_sb_noss_1")

element = driver.find_element(By.CLASS_NAME, "puis-card-container")
# we have different methods to find element. In this I went to amazon.in web and inspect the elements and get the class according to the product.

# print(element.text)

# for getting HTML code of element:
print(element.get_attribute("outerHTML"))

time.sleep(4)

driver.close()