#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data_url="https://en.wikipedia.org/wiki/List_of_companies_of_the_United_Kingdom_A%E2%80%93J"


# In[3]:


get_url=requests.get(data_url)
get_url


# In[4]:


data_soup=BeautifulSoup(get_url.text,"html")
data_soup


# In[5]:


data_soup.find("tr")


# In[6]:


data_soup.find_all("div")


# In[7]:


table = data_soup.find("table", class_="wikitable sortable")
table


# In[8]:


headers = []
header_row = table.find("tr")
for th in header_row.find_all("th"):
    headers.append(th.text.strip())


# In[9]:


rows = []
for row in table.find_all("tr")[1:]:  
    cells = [cell.text.strip() for cell in row.find_all(["td", "th"])]
    rows.append(cells)


# In[10]:


data=pd.DataFrame(rows,columns=headers)
data


# In[11]:


world_titles=data_soup.find_all("th")
world_titles


# In[12]:


worls_table_titles=[title.text for title in world_titles]
worls_table_titles


# In[13]:


data.columns = data.columns.str.replace(r"[^\w\s]", "").str.replace(" ", "_")

revenue_counts = data["2018_revenues_USD_M"].value_counts()
print("\nRevenues Counts:")
print(revenue_counts)


# In[14]:


plt.figure(figsize=(10, 6))
revenue_counts.plot(kind="bar")
plt.title("Number of Companies by 2018 Revenues")
plt.xlabel("2018 Revenues (USD $M)")
plt.ylabel("Number of Companies")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# In[15]:


employee_counts = data["Employees"].value_counts()
print("\nEmployee Counts:")
print(employee_counts)


# In[16]:


plt.figure(figsize=(10, 6))
employee_counts.plot(kind="bar")
plt.title("Number of Companies by Employees")
plt.xlabel("Employees")
plt.ylabel("Number of Companies")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# In[17]:


data.to_csv("companies_data.csv", index=False)

