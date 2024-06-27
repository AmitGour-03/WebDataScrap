from bs4 import BeautifulSoup
import os
import pandas as pd

# Making DataFrame Using Pandas to store the desired data by bs4
d= {'title':[], 'price':[], 'link': []}  # empty dict created

for file in os.listdir("data2"):

    try:
        with open(f"data2/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')

        # By seeing the html code, for title (as t)we can write:
        t = soup.find("h2")
        title = t.get_text()

        # By seeing the html code, for price link (as l) we can write:
        l = t.find("a")
        link = "https://amazon.in/" + l['href']   # we have appended this to open the link later

        # By seeing the html code, for price (as p)we can write:  here we will check in how many span particular class we choose, occur in 1 page; in our case it is 27 in page 1.(Got it)
        p = soup.find("span", attrs={"class": 'a-price-whole'})
        price = p.get_text()         # u'\u20B9' --> This is for unicode char for INR

        # print the product's title and price
        # print(title, link, price)  # for testing

        # appending into dict
        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)

        # print(p.get_text())  # for testing

        # break  # check for one product title only(just testing)
        # print(soup.prettify())

    except Exception as e:
        print(e)

# Making a data frame to store the  desired scraped data
df = pd.DataFrame(data=d)
df.to_csv('data2.csv')