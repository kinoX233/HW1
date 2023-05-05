#key for api request
IP_KEY = "c71abfe217768898585750c10c423aca"
IP_URL = "http://apis.juhe.cn/ip/ipNew"
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

    def get_loc(self):
        params = {'key':IP_KEY,'ip':self.ip}
        loc_json = requests.post(IP_URL,params=params)
        loc = json.loads(loc_json)
        #self.country = loc[country]
        print(loc)