# Initiating code
# Reference: https://selenium-python.readthedocs.io/getting-started.html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

query = "mobile"
file = 0
for i in range(1,11):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=1SQAEFHO42WD4&sprefix=laptop%2Caps%2C302&ref=nb_sb_noss_1")
   
    elements = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    
    # No. of elements found in ith page
    print(f"{len(elements)} elements are founded in your given URL's {i}th page of amazon.in.")

    for elem in elements:
        d= elem.get_attribute("outerHTML")
        with open(f"data2/{query}_{file}. html", "w", encoding="utf-8") as f:  # It will store these HTML code in specific created location. Here also, I have created a data folder
            f.write(d)
            file += 1
    
    # print(element.text)

    time.sleep(4)



driver.close()