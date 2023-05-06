import sys
from gui import *
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
import json
import requests
IP_URL = "http://api.liangmlk.cn?ak=xbDpKsZJcFgmSyLlAXHo&appid=602&ip="


def main():
    
    class atom (object):  # class for all the info about target location

        def __init__(self):
            self.ip = ""
            self.country = ""
            self.province = ""
            self.city = ""
            self.weather = ""
            self.type = ""

        def get_loc(self, ip):  # use ip to get the location
            self.ip = ip

            post = IP_URL + self.ip
            loc_json = requests.get(post)

            loc = json.loads(loc_json.text)["result"]
            # print(loc)
            self.country = loc["country"]
            self.province = loc["province"]
            self.city = loc["city"]
            self.type = loc["type"]

        def show_info(self):#show all info to dialog
            location = f'country:{atom.country}   province:{atom.province}  city:{atom.city}'
            wheather = f''

            sub_ui.text_ip.setText(atom.ip)
            sub_ui.text_loc.setText(location)
            sub_ui.text_weather.setText(wheather)
    
    app = QApplication(sys.argv)
    #creat mainwindow
    mainwindow = QMainWindow()
    main_ui = Ui_MainWindow()
    main_ui.setupUi(mainwindow)

    #create subwindow
    subwindow = QDialog()
    sub_ui = Ui_Dialog()
    sub_ui.setupUi(subwindow)

    #show mainwindow
    mainwindow.show()

    #after clicked, subwindow shows
    btn = main_ui.pushButton
    btn.clicked.connect( subwindow.show )#no parentheses() for function

    #post ip
    atom = atom()
    btn.clicked.connect( lambda: atom.get_loc(main_ui.textEdit.toPlainText()) )

    #show info
    btn.clicked.connect( atom.show_info )

    #quit
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()