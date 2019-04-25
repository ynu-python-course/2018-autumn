import sys, requests, json, re, urllib
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QPushButton, QComboBox,\
    QLineEdit, QGridLayout, QDesktopWidget, QApplication
from PyQt5.QtGui import QPalette, QBrush, QPixmap

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.train_type = "G"
        self.start_place = ""
        self.end_place = ""
        self.date = ""
        self.picture = ""
        self.initUI()

    def initUI(self):
        # 网格布局
        grid = QGridLayout()
        # 设置组件间隔10
        grid.setSpacing(10)
        # 放到屏幕中央
        self.resize(1000, 500)
        self.center()

        # 设置背景
        palette1 = QPalette()
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('3.jpg')))  # 设置背景图片
        self.setPalette(palette1)

        # 文本显示
        self.QLtrain_type = QLabel("请选择火车类型（待选：G，D，Z，T，K)")
        self.QLstart = QLabel("请输入你起始站(如昆明)")
        self.QLend = QLabel("请输入终止站（如重庆)")
        self.QLdate = QLabel("请输入你要乘车的日期（示列：2019-01-06）")
        self.QLpicture = QLabel("请输入你要查看的城市")

        # 文本编辑
        #下拉选单组件
        self.QCtrain_type = QComboBox(self)
        self.QCtrain_type.addItem("G")
        self.QCtrain_type.addItem("D")
        self.QCtrain_type.addItem("Z")
        self.QCtrain_type.addItem("T")
        self.QCtrain_type.addItem("K")
        # QLineEdit是单行文本编辑框组件
        self.QEstart = QLineEdit()
        self.QEend = QLineEdit()
        self.QEdate = QLineEdit()
        self.QEpicture = QLineEdit()
        # QTextEdit是多行文本编辑框组件
        self.textEdit = QTextEdit()
        # QPushButton是按钮组件
        self.btn1 = QPushButton("确认", self)
        self.btn2 = QPushButton("退出", self)
        self.btn3 = QPushButton("确认", self)

        # 增加组件到widget
        grid.addWidget(self.QLtrain_type, 1, 0)
        grid.addWidget(self.QCtrain_type, 1, 1)

        grid.addWidget(self.QLstart, 2, 0)
        grid.addWidget(self.QEstart, 2, 1)

        grid.addWidget(self.QLend, 3, 0)
        grid.addWidget(self.QEend, 3, 1)

        grid.addWidget(self.QLdate, 4, 0)
        grid.addWidget(self.QEdate, 4, 1)

        grid.addWidget(self.btn1, 5, 0)
        grid.addWidget(self.btn2, 5, 1)

        grid.addWidget(self.textEdit, 6, 1)
        grid.addWidget(self.QLpicture, 7, 0)
        grid.addWidget(self.QEpicture, 8, 0)
        grid.addWidget(self.btn3, 8, 1)

        self.setLayout(grid)
        # 窗口的标题
        self.setWindowTitle('查票')

        # 如果各个框内容变化，更新
        self.QCtrain_type.activated[str].connect(self.onActivated1)
        self.QEstart.textChanged[str].connect(self.onActivated2)
        self.QEend.textChanged[str].connect(self.onActivated3)
        self.QEdate.textChanged[str].connect(self.onActivated4)
        self.QEpicture.textChanged[str].connect(self.onActivated5)
        # 三个按钮的事件和槽绑定
        self.btn1.clicked.connect(self.btnPress1_clicked)
        self.btn2.clicked.connect(self.btnPress2_clicked)
        self.btn3.clicked.connect(self.btnPress3_clicked)

        self.show()

    def onActivated1(self, text):
        self.train_type = text
    # 起始地输入框变化
    def onActivated2(self, text):
        self.start_place = text
    # 终点地输入框变化
    def onActivated3(self, text):
        self.end_place = text
    # 乘车日期输入框变化
    def onActivated4(self, text):
        self.date = text
    # 城市图片信息变化
    def onActivated5(self, text):
        self.picture = text
    # 将窗口移动到中间
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 图片下载
    def get_onepage_urls(self, onepageurl):
        """获取单个翻页的所有图片的urls+当前翻页的下一翻页的url"""
        # if not onepageurl:
        # print('已到最后一页, 结束')
        # return [], ''
        try:
            html = requests.get(onepageurl)
            html.encoding = 'utf-8'
            html = html.text
        except Exception as e:
            print(e)
            pic_urls = []
            fanye_url = ''
            return pic_urls, fanye_url
        pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
        fanye_urls = re.findall(re.compile(r'<a href="(.*)" class="n">下一页</a>'), html, flags=0)
        fanye_url = 'http://image.baidu.com' + fanye_urls[0] if fanye_urls else ''
        return pic_urls, fanye_url

    def down_pic(self, pic_urls):
        """给出图片链接列表, 下载所有图片"""
        ct = 0
        for i, pic_url in enumerate(pic_urls):
            try:
                pic = requests.get(pic_url, timeout=15)
                string = str(i + 1) + '.jpg'
                with open(string, 'wb') as f:
                    f.write(pic.content)
                    print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
                    ct = ct + 1
                    if (ct > 10):  # 下载11张图片
                        break
            except Exception as e:
                print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
                print(e)
                sys.exit()

    def btnPress3_clicked(self):
        # 下载图片
        I = self.picture
        keyword = I
        # keyword = '***'  # 关键词, 改为你想输入的词即可, 相当于在百度图片里搜索一样
        url_init_first = r'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1497491098685_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1497491098685%5E00_1519X735&word='
        url_init = url_init_first + urllib.parse.quote(keyword, safe='/')
        all_pic_urls = []
        onepage_urls, fanye_url = self.get_onepage_urls(url_init)
        all_pic_urls.extend(onepage_urls)

        fanye_count = 0  # 累计翻页数
        while 1:
            onepage_urls, fanye_url = self.get_onepage_urls(fanye_url)
            fanye_count += 1
            # print('第页' % str(fanye_count))
            if fanye_url == '' and onepage_urls == []:
                break
            all_pic_urls.extend(onepage_urls)

        self.down_pic(list(set(all_pic_urls)))

    def btnPress2_clicked(self):
        sys.exit()

    def btnPress1_clicked(self):
        info_list = []
        city_dic = {"昆明": "KMM", "成都": "CDW", "贵阳": "GIW", "上海": "SHH", "天津": "TJP", "长沙": "CSQ", "福州": "FZS",
                    "广州": "GZQ", "哈尔滨": "HBB", "合肥": "HFH", "呼和浩特": "HHC", "海口": "VUQ", "杭州": "HZH", "济南": "JNK",
                    "兰州": "LZJ", "拉萨": "LSO", "南昌": "NCG", "南京": "NJH", "南宁": "NCG", "石家庄": "SJP", "沈阳": "SYT",
                    "太原": "TYV", "武汉": "WHN", "乌鲁木齐": "WMR", "西安": "XAY", "西宁": "XNO", "银川": "YIJ", "郑州": "ZZF",
                    "重庆": "CQW"}
        test = []
        # 将下拉选择框的信息接收
        train_type = self.train_type
        start_place = self.start_place
        end_place = self.end_place
        date = self.date
        news_place = city_dic[start_place]
        newe_place = city_dic[end_place]
        I = train_type
        if (I != "G" and I != "K"):
            self.textEdit.setPlainText("无法查找")
            sys.exit()
        raw1 = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=" + date
        raw2 = "&leftTicketDTO.from_station=" + news_place
        raw3 = "&leftTicketDTO.to_station=" + newe_place
        raw4 = "&purpose_codes=ADULT"
        url = raw1 + raw2 + raw3 + raw4
        r = requests.get(url)
        html = r.text
        json_dict = json.loads(html)
        for count in range(len(json_dict["data"]["result"])):
            time = json_dict["data"]["result"][count].split("|")
            if (I == "G"):
                info_list.append(time[3])
                for info in range(8, 11):
                    info_list.append(time[info])
                    pass
                # info_list.append(time[25])
                for i in range(31, 29, -1):
                    info_list.append(time[i])
                    pass
                test.append(info_list)
                info_list = []
                pass

            elif (I == "K"):
                info_list.append(time[3])  # 1
                for info in range(8, 11):  # 3
                    info_list.append(time[info])
                    pass
                info_list.append(time[23])  # 1
                for i in range(25, 30):  # 5
                    info_list.append(time[i])
                    pass
                test.append(info_list)
                info_list = []
                pass
            pass
        if (I == "G"):
            tplt = "{:6}\t{:4}\t{:4}\t{:4}\t{:4}\t{:4}"
            s1 = tplt.format("车次", "出发时间", "到达时间", "历时", "一等座", "二等座") + "\n"
            for i in range(len(test)):
                # print(infom[0])
                infom = test[i]
                for i in range(4, 6):
                    if (infom[i] == ""):
                        infom[i] = "--"
                if (I in infom[0]):
                    temp1 = tplt.format(infom[0], infom[1], infom[2], infom[3], infom[4], infom[5])
                    s1 = s1 + temp1 + "\n"
                    pass
                else:
                    continue
            self.textEdit.setPlainText(s1)
        elif (I == "K"):
            tplt2 = "{:6}\t{:4}\t{:4}\t{:4}\t{:2}\t{:2}\t{:2}\t{:2}\t{:2}\t{:2}"
            s2 = tplt2.format("车次", "出发时间", "到达时间", "历时", "软卧", "动卧", "硬卧", "软座", "硬座", "无座") + "\n"
            for i in range(len(test)):
                # print(infom[0])
                infom = test[i]
                for i in range(4, 7):
                    if (infom[i] == ""):
                        infom[i] = "--"
                if (I in infom[0]):
                    temp2 = tplt2.format(infom[0], infom[1], infom[2], infom[3], infom[4], infom[5], infom[6], infom[7],
                                       infom[8], infom[9])
                    s2 = s2 + temp2 + "\n"
                    pass
                else:
                    continue
                pass
            self.textEdit.setPlainText(s2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 界面
    ex = Example()

    sys.exit(app.exec_())