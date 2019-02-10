#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


hs = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


# In[4]:


with requests.Session() as s:
    url = 'http://hyint.nhu.edu.tw/nhuhyint/LoginCheck.jsp'
    target = 'http://hyint.nhu.edu.tw/nhuhyint/sendurl_api_v3.jsp?dbid=DB17143'
    r = s.get(target, headers=hs)
    soup = BeautifulSoup(r.content, 'html5lib')
    token = soup.find('input', attrs={'name': 'csrf'})['value']
    logintime = soup.find('input',attrs={'name':'url'})['value']
    Parse = logintime.split('=',5)
    time = ''+Parse[5]
    login_data = dict(csrf=token,
                      url="sendurl_api_v3.jsp?debug=&dbid=DB17143&type=&url=http://www.airitilibrary.com&logintime="+time,
                      uid="10525123",
                      pwd="")
    '''
    uid = 登入帳號
    pwd = 登入密碼
    '''
    r = s.post(url, data=login_data, headers=hs)
    a = s.get("http://www.airitilibrary.com")


# In[5]:


print(a.text)


# In[ ]:




