import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime

res = req.get('http://naver.com')
dom = bs(res.text, 'html.parser')
titles = dom.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li > a.ah_a > span.ah_k')

# 파일 생성
fname = "{:%Y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(fname, mode='w', encoding='utf-8')
# 파일 쓰기
for tit in titles:
    file.write(tit.text+'\n')
#파일 닫기
file.close()