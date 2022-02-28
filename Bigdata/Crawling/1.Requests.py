"""
날짜 : 2022/02/28
이름 : 김재현
내영 : 파이썬 HTML 페이지 요청 실습
"""

import requests as req

# 페이지 요청하기
html = req.get('https://naver.com').text
print(html)

print('-'*100)

test = req.get('http://chhak.or.kr/test.html').text
print(test)




