# Initiating code
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()    # Browse in FireFox WebBrowser

# For Navigation:
driver.get("https://www.youtube.com/")

assert "YouTube" in driver.title

time.sleep(6)

# Finding element within the document (URL given)

# This below commented line of code which selects the first input element on the page. This might not always be the search bar. A more reliable way is to use the element's name attribute:
# elem = driver.find_element(By.NAME, "search")  -> throws an error
# elem = driver.find_element(By.CSS_SELECTOR, ".yt-uix-searchbar-input")
# elem = driver.find_element(By.CSS_SELECTOR, ".yt-uix-searchbar-input")

elem = driver.find_element(By.TAG_NAME, "input")
 

# For Tag_Name: Just do inspect element by F12 in the URL given and hower on what element you need then we will get the tagname.

# Here, we also want to see the HTML code and give specific element idea (by F12- inspect element)

# It is possible to call send_keys on any element, which makes it possible to test keyboard shortcuts such as those used on GMail. A side-effect of this is that typing something into a text field won’t automatically clear it. Instead, what you type will be appended to what’s already there. You can easily clear the contents of a text field or textarea with the clear method:


elem.clear()


elem.send_keys("Devon ke Dev Mahadev", Keys.RETURN)
# Now, you’ve got an element. What can you do with it? First of all, you may want to enter some text into a text field:

time.sleep(10)  # for seeing the desired result

# It helps us to search the entered text in the text Box 
# elem.send_keys(Keys.ENTER)   # lets check this, we will combine this line and above line of code together

assert "No results found." not in driver.page_source    # if respective data not found within the document (URL given)

time.sleep(15)  # for seeing internally activity doing by code by some hault.

print("*************************************************\n             Work Done Successfully\n")

# close the working of code.
driver.close()