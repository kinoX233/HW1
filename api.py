#key for api request
#IP_KEY = "c71abfe217768898585750c10c423aca"
IP_URL = "http://api.liangmlk.cn"#test ip 192.168.211.228 http://ip.taobao.com/service/getIpInfo2.php
import requests
import json

class atom (object):

    def __init__(self):
        self.ip = ""
        self.country = ""
        self.province = ""
        self.city = ""
        self.isp = ""
        self.weather = ""

    def get_loc(self,ip):
        self.ip=ip
        datain = {'data':self.ip}
        loc_json = requests.post(IP_URL,data=datain)

        #loc = json.loads(loc_json)
        #self.country = loc[country]
        #print(loc)
        print(loc_json.text)