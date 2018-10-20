#!/usr/bin/env python
__author__ = 'Chocolee'

import requests, uuid
from bs4 import BeautifulSoup


response = requests.get(
    url='https://www.autohome.com.cn/news/'
)
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, features='lxml')

target = soup.find(id="auto-channel-lazyload-article")

li_list = target.find_all('li')

for i in li_list:
    a = i.find('a')

    if a:
        print(a.attrs.get('href'))
        txt = a.find('h3')
        print(txt.text)
        img_url = a.find('img').attrs.get('src')
        print(img_url)
        img_response = requests.get(url='http:%s' % (img_url))
        file_name = str(uuid.uuid4()) + '.jpg'
        with open(file_name, 'wb') as f:
            f.write(img_response.content)
