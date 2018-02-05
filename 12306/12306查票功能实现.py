#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 日期    : 2018/1/17 12:34
# 作者    : Yuan-小江
# @Email  : 822309454@qq.com
# 文件名  : 12306查票功能实现.py
# 编辑工具: PyCharm
# 功能    ：12306查票

import requests, re,time,pprint
from datetime import datetime

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}


class TrainInquiry(object):

    def __init__(self, start_station, end_station, start_time):
        self.start_station = start_station
        # 出发站
        self.end_station = end_station
        # 终点站
        self.start_time = start_time
        # 出发时间
        self.start_station_code = ''
        self.end_station_code = ''

        self.get_station_code()

    def get_station_code(self, ):
        # 获取出发的站点代号
        global stations
        try:
            r = requests.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9044',
                             headers=header)
            r.raise_for_status()
            stations = dict(re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)', r.text))
            self.start_station_code = stations[self.start_station]
            self.end_station_code = stations[self.end_station]
        except:
            print( 'get_station_code:error')

    def cheak(self):
        # 返回所有车次信息
        data = {
            'leftTicketDTO.train_date': self.start_time,
            'leftTicketDTO.from_station': self.start_station_code,
            'leftTicketDTO.to_station': self.end_station_code,
            'purpose_codes': 'ADULT',
        }
        results = {}
        while True:
            try:
                r = requests.get('https://kyfw.12306.cn/otn/leftTicket/queryZ?', params=data, headers=header)
                r.raise_for_status()
                if r.json() != None:
                    infomation = r.json()['data']['result']
                    for i,x in enumerate(infomation):
                        a = x.split('|')
                        # print(i,x.split('|'))
                        for b in range(len(a)):
                            if a[b]=='':
                                a[b]='--'
                        results[a[3]]={
                            '一等座':a[-6],
                            '二等座':a[-7],
                            '软卧':a[-14],
                            '硬卧':a[-9],
                            '硬座':a[-8],
                            '无座':a[-11]
                        }

                    break
            except Exception as e:
                print(e)
                time.sleep(1)
        return results


def main():
    a = TrainInquiry('成都', '峨眉山', '2018-02-07')
    order = 'C6253'#指定车次
    pz = '二等座'
    while True:
        o = a.cheak()
        if o[order][pz] != '无':
            print('有票了快抢')
            break
        print(o[order][pz],datetime.now())
        time.sleep(2)
if __name__ == '__main__':
    main()
