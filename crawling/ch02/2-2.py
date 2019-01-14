import urllib.request as req
from bs4 import BeautifulSoup as bs

URL = 'https://news.naver.com/main/home.nhn'
html = req.urlopen(URL)

dom = bs(html, 'html.parser')
strong1 = dom.select('#text_today_main_news_801001 > li > div > a > strong')
# 위치는 페이지검사에서 해당dom 우클릭->카피->카피셀렉트
# 선택자의 마지막 태그(타겟)를 이름으로 설정하면 편함

print('이시간 주요뉴스')
for s in strong1:
    print("제목 : ", s.string)

print()
strong2 = dom.select('#section_economy > div.com_list > div > ul > li > a > strong')
print('이시간 경제뉴스')
for s in strong2:
    print("제목 : ", s.string)
