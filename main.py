import sys
from gui import *
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
import json
import requests
IP_URL = "https://restapi.amap.com/v3/ip?"
CODE_URL = "https://restapi.amap.com/v3/config/district?"
WEATHER_INFO = "https://restapi.amap.com/v3/weather/weatherInfo?"
def main():
    
    class atom (object):  # class for all the info about target location

        def __init__(self):
            self.ip = ""
            self.country = "中国"
            self.province = ""
            self.city = ""
            self.weather = ""
            self.code = ""
            self.range = ""

        def get_loc(self, ip):  # use ip to get the location
            self.ip = ip
            key = "7c7c4176583750a3aa9b0fe5deb3823d"

            post = f'{IP_URL}ip={self.ip}&key={key}'
            loc_json = requests.get(post)

            loc = json.loads(loc_json.text)

            self.province = loc["province"]
            self.city = loc["city"]
            self.code = loc["adcode"]
            self.range = loc["rectangle"]

        def show_info(self):#show all info to dialog
            location = f'国家:{atom.country}   省份:{atom.province}  城市:{atom.city}'
            wheather = self.get_weather()

            sub_ui.text_ip.setText(atom.ip)
            sub_ui.text_loc.setText(location)
            sub_ui.text_weather.setText(wheather)
        
        def get_code(self):
            key = "7c7c4176583750a3aa9b0fe5deb3823d"
            post = f'{CODE_URL}key={key}&keywords={self.city}'

            code_json = requests.get(post)

            code = json.loads(code_json.text)["districts"][0]["adcode"] #adcode for city
            return code

        def get_weather(self):
            key = "7c7c4176583750a3aa9b0fe5deb3823d"
            code = self.get_code()
            post = f'{WEATHER_INFO}key={key}&city={code}'

            wheather_json = requests.get(post)

            wth = json.loads(wheather_json.text)["lives"][0]

            wth_info = f'天气:{wth["weather"]}\n气温:{wth["temperature"]}\n风向:{wth["winddirection"]}\n风力:{wth["windpower"]}\n空气湿度:{wth["humidity"]}'
            return wth_info
        
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