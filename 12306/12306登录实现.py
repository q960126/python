#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 日期    : 2018/1/18 22:04
# 作者    : Yuan-小江
# @Email  : 822309454@qq.com
# 文件名  : 12306登录实现.py
# 编辑工具: PyCharm
# 功能    ：12306登录
import requests
import time
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
disable_warnings(InsecureRequestWarning)

session = requests.session()
session.verify = False

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    "Host":"kyfw.12306.cn",
    "Referer":"https://kyfw.12306.cn/otn/passport?redirect=/otn/"
}


def get_login():
    session.get('https://kyfw.12306.cn/otn/login/init',headers = headers)
    try:
        if captcha_check():
            data = {
                'appid':'otn',
                'password':'qwe960126',
                'username':'18328498928'
            }
            while True:
                r = session.post('https://kyfw.12306.cn/passport/web/login',data = data,headers =headers)
                r.encoding = 'utf-8'
                if r.text.find('网络可能存在问题') == -1:
                    break
                time.sleep(1)
            if r.text.find('登录成功') != -1:
                r = session.get('https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin',headers=headers)
                r = session.post('https://kyfw.12306.cn/passport/web/auth/uamtk',data={'appid':'otn'},headers =headers)
                if r.text.find('验证通过') !=-1:
                    result = {
                        'tk':r.json()['newapptk']
                    }
                    r = session.post('https://kyfw.12306.cn/otn/uamauthclient',headers = headers,data=result)
                    print(r.json()['username'],'欢迎登陆12306')
                else:
                    get_login()
            else:
                get_login()
        else :
            get_login()
    except Exception  as e:
        print(e)

def captcha_check():
    # 检查验证码是否正确
    imagecontent = session.get('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.09478778385973807',headers=headers).content
    with open('验证码.jpg','wb')as f:
        f.write(imagecontent)
        f.close()
    numbers_id1 = ['46,41','108,39','182,41','250,43','37,116','108,112','181,113','250,107']
    anwsers = input('请输入验证码（请用逗号隔开）:').split(',')
    numbers_id2 = []
    for i in anwsers:
        numbers_id2.append(numbers_id1[int(i)-1])
    anwser = ','.join(numbers_id2)
    data = {
    'answer':anwser,
    'login_site':'E',
    'rand':'sjrand'
    }
    r = session.post('https://kyfw.12306.cn/passport/captcha/captcha-check',headers=headers,data=data)
    if r.text.find('验证码校验成功') != -1:
        print('验证码正确')
        return True
    print('验证码错误请重新输入')
    return False



def main():
    get_login()

if __name__ == '__main__':
    main()
