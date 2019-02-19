# -*-coding:utf8-*-
# 流程 ：　以 s_status、s_tid、p 三个锚点的值遍历网站。
import requests
import re
import json
import sys
import datetime
import time

def deal_json(json_data, log_file):
    for proj in json_data['plist']:
        log_file.write('start time ' + proj['startTime'] + '\n')
        log_file.write('end time ' + proj['endTime'] + '\n')
        log_file.flush()

# Request header.
head = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Host': 'ssl.gongyi.qq.com',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Accept': '*/*',
}

# status : 1--募款中, 2--执行中, 3--已结束
status = (1, 2, 3)

# tid : 71--疾病救助, 72--救灾扶贫, 73--教育助学, 74--自然保护, 75--其他
tid = (71, 72, 73, 74, 75)

log_file = open('/tmp/suijianwei', mode = 'a')
for s_status in status:
    for s_tid in tid:
        log_file.write(str(s_status) + " " + str(s_tid))
        for s_page in range(1, 100):
            url = 'https://ssl.gongyi.qq.com/cgi-bin/WXSearchCGI?ptype=stat&s_status='\
                + str(s_status) +'&s_tid='+str(s_tid) + '&p=' + str(s_page)
            res = requests.get(url, headers = head).text
            deal_json(json.loads(res[1:-1]), log_file)         
            '''
            try:
                url = 'https://ssl.gongyi.qq.com/cgi-bin/WXSearchCGI?ptype=stat&s_status='\
                    + str(s_status) +'&s_tid='+str(s_tid) + '&p=' + str(s_page)
                res = requests.get(url, headers = head).text
                deal_json(json.loads(res[1:-1]), log_file)
            except:
                log_file.write('fxxk')
                continue
            '''
log_file.close()