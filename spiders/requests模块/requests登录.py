#!/usr/bin/env python
__author__ = 'Chocolee'

import requests

post_dict = {
    "phone": '8615110111879',
    'password': 'lyl890625',
    'oneMonth': 1
}


r1 = requests.get('http://dig.chouti.com')
print(r1.cookies.get_dict())

response = requests.post(
    url='http://dig.chouti.com/login',
    data=post_dict,
    headers={
        'Referer': 'http://dig.chouti.com',
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }
)

print(response.text)
cookie_dict = response.cookies.get_dict()
print(cookie_dict)