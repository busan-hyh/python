import urllib.request as req

URL = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp'
# 전국날씨정보

data = req.urlopen(URL).read()
xml = data.decode('UTF-8')

print(xml)