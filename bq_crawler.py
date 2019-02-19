# -*-coding:utf8-*-
# 流程 ：　host/txt/id 获取类型 ----> host/book/id 获取所有章节 ----> 遍历章节，获取内容。
import requests
import re
import json
import random
import sys
import datetime
import time
from imp import reload
from multiprocessing.dummy import Pool as ThreadPool

# Request header.
head = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Host': 'www.qu.la',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

# Max book number of 'www.qu.la/book/number'.
MAX_BOOK_NUM = 157000

for number in range(20794, 157000):
    url_book = 'https://www.qu.la/book/' + str(number) + '/'
    url_txt = 'https://www.qu.la/txt/' + str(number) + '/'
    res = requests.get(url_txt, headers = head).text
    author = re.findall(r'<span id="author">(.*)</span>', res)[0]
    book_name = re.findall(r'<h1>(.*)</h1>', res)[0]
    book_type = re.findall(r'分 类：<span class="pd_r">(.*)</span>', res)[0]
    book_status = re.findall(r'状 态：<span class="pd_r">(.*)</span>', res)[0]
    #print(res)
    print('编号: ' + str(number) + '书名: ' + book_name + '  类型: ' + book_type + ' ' + author + '  状态: ' + book_status)
    #<span id="author">作者：长公</span>