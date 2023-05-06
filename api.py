# key for api request
# IP_KEY = "xbDpKsZJcFgmSyLlAXHo"
import json
import requests
IP_URL = "http://api.liangmlk.cn?ak=xbDpKsZJcFgmSyLlAXHo&appid=602&ip="


class atom (object):#class for all the info about target location

    def __init__(self):
        self.ip = ""
        self.country = ""
        self.province = ""
        self.city = ""
        self.isp = ""
        self.weather = ""

    def get_loc(self, ip):#use ip to get the location
        self.ip = ip
        post = IP_URL + self.ip
        loc_json = requests.get(post)

        # loc = json.loads(loc_json)
        # self.country = loc[country]
        #print(loc_json.text)
