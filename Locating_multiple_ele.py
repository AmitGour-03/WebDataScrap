# Initiating code
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

query = "laptop"
page_num = 2   # we can use for loop here in order to get the details of the web page (page wise) from given URL
driver.get(f"https://www.amazon.in/s?k={query}&page={page_num}&crid=1SQAEFHO42WD4&sprefix=laptop%2Caps%2C302&ref=nb_sb_noss_1")
# k={query}&page={page_num}.  This part is interesting. Learned from scraping HTML code of given url and observing url in search engine

elements = driver.find_elements(By.CLASS_NAME, "puis-card-container")
# we have different methods to find element. In this I went to amazon.in web and inspect the elements and get the class according to the product.

# print(elements)  # It gives a list

# No. of elements found
print(f"{len(elements)} elements are founded in your given URL page of amazon.in.")

for elem in elements:
    print(elem)       # Here I am printing the scarped results but in project we will store it in a specific file.



# for getting HTML code of element:
# print(element.get_attribute("outerHTML"))
# print(element.text)

time.sleep(4)

driver.close()