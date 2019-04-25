import requests

url = 'http://113.55.4.18/login/index.php'

params = {"username": 20161120078, "password": 123456}
html=requests.post(url,data=params)
print(html.text)
