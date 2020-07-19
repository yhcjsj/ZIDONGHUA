import requests, logging
from config import Log

HOST = "http:/192.168.1.100:8082/login"

class Login():
    def login(username, password):
        url = "http://192.168.1.100:8082/login"
        data = {"username": username, "password": password}
        heades = {"Content-Type": "application/json"}
        rsp = requests.post(url, json=data, headers=heades)
        print(rsp.content.decode("utf-8"))
        return rsp.json()

    a = login("lucy", "123456")
    # print(a.json())
    # logging.info("测试结{}".format(a.json()))
