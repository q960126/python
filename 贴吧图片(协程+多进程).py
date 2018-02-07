

# coding:utf-8
# 多进程+协程
import requests
import time
from lxml import etree
import os,re,hashlib
import gevent
from gevent import monkey
from multiprocessing import Pool
import threading
monkey.patch_all(thread=False)

header = {
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
'105'
'https://tieba.baidu.com/p/5033202671?see_lz=1&pn=1'
def get_html(url):

    try:
        r = requests.get(url,headers = header)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        print('get_html 出错')
        return None
def download(image_url):
    content = requests.get(image_url,headers = header).content
    path = 'D:/python/贴吧'
    if  not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)
    md5 = hashlib.md5(content).hexdigest()
    with open(md5+'.jpg','wb') as f:
        f.write(content)
def parse_index(url):
    sel = etree.HTML(get_html(url))
    image_urls = sel.xpath('//img[@class="BDE_Image"]//@src')
    tocks = []
    for url in image_urls:
        tocks.append(gevent.spawn(download,url))
    gevent.joinall(tocks)
def main():
    start_time = time.time()
    tp_url = 'https://tieba.baidu.com/p/5033202671?see_lz=1&pn={}'
    pool = Pool(4)
    tocks = []
    for i in range(1,106):
        pool.apply_async(parse_index,args=(tp_url.format(i),))
    pool.close()
    pool.join()

    print('用时',time.time()-start_time)
if __name__ == '__main__':
    main()

