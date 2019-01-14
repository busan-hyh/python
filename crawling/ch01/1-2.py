import urllib.request as req
# 임포트 패키지.모듈 as 별칭으로 쓰기

URL = 'http://img.hani.co.kr/imgdb/resize/2018/0907/00502739_20180907.JPG'
req.urlretrieve(URL, './puppy1.jpg')

print('다운로드 완료')
