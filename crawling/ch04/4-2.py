#크롤링
import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime

res = req.get('http://naver.com')
dom = bs(res.text, 'html.parser')
titles = dom.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li > a.ah_a > span.ah_k')
# 2-5.py에서 복붙한 크롤링 코드▲

#하둡저장
from pywebhdfs.webhdfs import PyWebHdfsClient as hadoop
hdfs = hadoop(user_name='hadoop', port=50070, host='192.168.111.101')

