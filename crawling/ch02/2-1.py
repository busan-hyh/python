from bs4 import BeautifulSoup as bs
import urllib.request as req

URL = 'http://chhak.com/py/test1.html'
html = req.urlopen(URL)

dom = bs(html, 'html.parser')
title = dom.select_one('h1').string
#h1태그의 텍스트노드를 찝어내기 .text .string .get_text() 모두 텍스트노드 찝어내는 용도

items = dom.select('ul > li')
#[]는 리스트. 반복문으로 출력해야함

print('제  목 : ', title)
for li in items:
    print('아이템 : ', li.string)
