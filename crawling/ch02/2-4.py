from selenium import webdriver

# 크롬 드라이버 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 네이버 이동
browser.get('http://naver.com')

# 네이버 로그인버튼 클릭
login_btn = browser.find_element_by_css_selector('#account > div > a')
login_btn.click()

# 로그인정보 입력
input_id = browser.find_element_by_id('id')
input_pw = browser.find_element_by_id('pw')

input_id.send_keys('dsforme')
input_pw.send_keys('ckdwh77')

input_btn = browser.find_element_by_css_selector('#frmNIDLogin > fieldset > input')
input_btn.click()

# 리캡챠가 뜬다!!