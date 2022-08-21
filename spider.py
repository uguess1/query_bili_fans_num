import requests

from config import DEFAULT_JSON
from function import *


class Crawler:
    def __init__(self):
        self.__HEADER = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
        }
        rem_data = get_data(DATAPATH, DEFAULT_JSON)
        self.__vmid = rem_data["currchoose"]
        self.__fan_num = (
            -1
            if self.__vmid not in rem_data["fans_num"]
            else rem_data["fans_num"][self.__vmid][1]
        )
        self.__username = (
            ""
            if self.__vmid not in rem_data["fans_num"]
            else rem_data["fans_num"][self.__vmid][0]
        )
        self.__change = "距离上次刷新变化:  0"

    # vmid=33605910
    @logger.catch()
    def get_fans(self, mid=""):
        if mid == "":
            mid = self.__vmid
        url = "http://api.bilibili.com/x/web-interface/card"
        params = {"mid": mid}
        ans = requests.get(url=url, headers=self.__HEADER, params=params, timeout=10)
        ans.encoding = "utf-8"
        ans = ans.json()
        if ans["code"] == 0:
            self.__username = ans["data"]["card"]["name"]
            self.__fan_num = ans["data"]["card"]["fans"]
            print("刷新成功！")
        return ans["code"]

    def get_fans_num(self):
        return self.__fan_num

    def set_vmid(self, vmid):
        self.__vmid = vmid

    def get_vmid(self):
        return self.__vmid

    def get_change(self):
        return self.__change

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username
