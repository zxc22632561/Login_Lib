#!/usr/bin/env python
# coding: utf-8

# In[78]:


import requests
from bs4 import BeautifulSoup


# In[77]:


hs = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


# In[119]:


with requests.Session() as s:
    url = 'http://hyint.nhu.edu.tw/nhuhyint/LoginCheck.jsp'
    r = s.get(url, headers=hs)
    soup = BeautifulSoup(r.content, 'html5lib')
    token = soup.find('input', attrs={'name': 'csrf'})['value']
    login_data = dict(csrf=token,uid="10525123", pwd="a524700a")
    r = s.post(url, data=login_data, headers=hs)
    a = s.get("http://hyint.nhu.edu.tw/nhuhyint/home.jsp")


# In[120]:


print(a.text)


# In[ ]:




