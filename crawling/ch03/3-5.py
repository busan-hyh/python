#크롤링하고 몽고DB에 저장하기

import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime
from pymongo import MongoClient as mongo

res = req.get('http://naver.com')
dom = bs(res.text, 'html.parser')
titles = dom.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li > a.ah_a > span.ah_k')
# 2-5.py에서 복붙한 크롤링 코드▲

# 몽고DB에 저장하기
conn = mongo('mongodb://hyh:1234@192.168.111.101:27017')
db = conn.get_database('test')
member = db.get_collection('NAVER')

# 인서트방식
# db.NAVER.insert({'1':'1위컬럼','2':'2위컬럼',...})

doc = {
        '1': titles[0].text,'2':titles[1].text,'3':titles[2].text,'4':titles[3].text,'5':titles[4].text,
        '6':titles[5].text,'7':titles[6].text,'8':titles[7].text,'9':titles[8].text,'10':titles[9].text,
        'rdate': datetime.now()
        }

member.insert(doc)
