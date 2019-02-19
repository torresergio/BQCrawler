# -*-coding:utf8-*-
# 流程 ：　以 s_status、s_tid、p 三个锚点的值遍历网站。
import requests
import re
import json
import sys
import datetime
import time
import xlwt

FAIL_NUM = 0

def deal_json(json_data, table, line_num):
    line_count = 0
    for proj in json_data['plist']:
        try:
            table.write(line_num, 1, proj['startTime'])
            table.write(line_num, 2, proj['endTime'])
            table.write(line_num, 3, proj['stat']['money']) #已获得钱数,需要除100
            table.write(line_num, 4, proj['stat']['times']) #捐款人次
        except KeyError:
            FAIL_NUM = FAIL_NUM + 1
            break
        try:
            table.write(line_num, 5, proj['stat']['quota_money']) #企业配额，需要除100
            table.write(line_num, 6, proj['stat']['step_times'])
            table.write(line_num, 7, proj['stat']['together_donate_times'])
            table.write(line_num, 8, proj['stat']['together_create_times'])
            table.write(line_num, 9, proj['stat']['step_money'])
            table.write(line_num, 10, proj['needMoney']) #目标金额，需要除100
        except KeyError:
            print('fxxk')
        line_count = line_count + 1
        line_num = line_num + 1
    return line_count

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

# pages : 各个项的最大页个数
pages = (158, 31, 50, 11, 22, 1726, 286, 748, 132, 544, 678, 238, 311, 40, 186)
page_index = 0
for s_status in status:
    for s_tid in tid:
        line_num = 1
        book = xlwt.Workbook()
        table = book.add_sheet(str(s_status)+"_"+str(s_tid), cell_overwrite_ok=True);
        print(str(s_status)+" "+str(s_tid))
        for s_page in range(1, pages[page_index]):
            try:
                url = 'https://ssl.gongyi.qq.com/cgi-bin/WXSearchCGI?ptype=stat&s_status='\
                    + str(s_status) +'&s_tid='+str(s_tid) + '&p=' + str(s_page)
                res = requests.get(url, headers = head).text
                line_count = deal_json(json.loads(res[1:-1]), table, line_num)
            except:
                FAIL_NUM = FAIL_NUM + 1
                continue
            line_num = line_num + line_count
        page_index = page_index + 1
        book.save('tmp' + str(s_status) + str(s_tid) + '.xls')
print('Fail Num : ' + str(FAIL_NUM))
