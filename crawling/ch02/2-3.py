import requests as req
from bs4 import BeautifulSoup as bs

# 세션 시작
sess = req.session()

# 로그인하기

uid = 'ksb0503'
pw = '123456789'
login_check_url = 'https://here.busan.com/bbs/login_check.php'

sess.post(login_check_url,data={'mb_id':uid, 'mb_password':pw}) #sess는 로그인된 세션이 되었다

# 마이페이지
mypage_url = 'http://here.busan.com/member/member_mypage.php'
res = sess.get(mypage_url) #로그인된 세션이 mypage_url로 요청한 결과가 res(html)이다.

# 아이디/보유포인트 스크래핑하기
dom = bs(res.text, 'html.parser')
my_id = dom.select_one('#design_contents > dl > dd > span.id')
print(my_id.string)

# nth-child(1) 는 select_one에서 안먹으므로 nth-of-type(1)로 바꿔야함
my_point = dom.select_one('#design_contents > div.point > font:nth-of-type(1)')
print(my_point.string)