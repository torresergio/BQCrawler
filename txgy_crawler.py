# -*-coding:utf8-*-
# 流程 ：　以 s_status、s_tid、p 三个锚点的值遍历网站。
import requests
import re
import json
import sys
import datetime
import time
from imp import reload

# Request header.
head = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Host': 'gongyi.qq.com',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

# status : 1--募款中, 2--执行中, 3--已结束
status = (1, 2, 3)

# tid : 71--疾病救助, 72--救灾扶贫, 73--教育助学, 74--自然保护, 75--其他
tid = (71, 72, 73, 74, 75)

for s_status in status:
    for s_tid in tid:
        for s_page in range(1, 100):
            url_book = 'https://gongyi.qq.com/succor/project_list.htm#s_status=' + str(s_status) + '&s_tid=' + str(s_tid) + '&p=' + str(s_page)
            print(url_book)
            
text = '\u7D27\u6025\u6551\u52A9\u4E2D\u5FC3\u4F9D\u6258\u57282011\u5E743\u6708\u5DF2\u5EFA\u7ACB\u7684\u751F\u547D'
text.encode('utf-8')
print(text)