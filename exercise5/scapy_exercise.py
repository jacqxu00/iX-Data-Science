# -*- coding: utf-8 -*-
"""
Jacqueline Xu
iXperience Tel Aviv
27 May 2019
Exercise 4: SQL Database
"""

import pymysql

conn = pymysql.connect(host="ix-ds-lisbon.c8zzomd9kqtu.us-east-2.rds.amazonaws.com",
                     user="guest",
                     passwd="x9xpV5]2M6BQt7",  
                     db="nobel")    

cur = conn.cursor()
cur.execute("SELECT * FROM location")

cur.fetchall()

cur.close()
conn.close()

#%%

import pandas as pd

# df = pd.read_clipboard()
url = "https://www.worldatlas.com/articles/largest-cities-in-europe-by-population.html"

 # read_html returns a list of databases
 # it reads every table on the webpage (in this case there is only one)
df = pd.read_html(url)[0]
print(df)

#%%

import requests
import extruct
from pprint import pprint


url = "http://books.toscrape.com/"
r = requests.get(url)
data = extruct.extract(r.text)
pprint(data)

# incomplete

'''
print(r.status_code)
print(r.content)

data = r.json()
print(data)
print(data["message"])
'''