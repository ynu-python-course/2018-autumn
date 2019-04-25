import zipfile
zfile = zipfile.ZipFile("F:/calculator.zip")

passFile=open('F:/pwd.txt') #读取你设定的密码文件

for line in passFile.readlines():
  try:
    password = line.strip('\n')
    zfile.extractall(path='F:/', members=zfile.namelist(), pwd=password.encode('utf-8'))
    print("正确的密码是:",password)
    break
  except:
    print(password,"错了")