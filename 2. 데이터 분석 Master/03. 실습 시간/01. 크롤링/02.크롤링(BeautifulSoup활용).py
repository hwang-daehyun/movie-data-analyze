# **BeautifulSoup 활용하기**

#- 크롤링의 과정
#    - 파이썬으로 웹서버에 정보 요청하고 HTML 데이터 가져오기
#    - 데이터 파싱
#    - 원하는 정보 저장

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


keyword = '제주도'
url = f'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={keyword}'
res = requests.get(url)
soup = bs(res.text, 'html.parser')

'''print(soup.find_all('a', class_='title_link'))'''

#요소에서 텍스트들만 다 가져오는 경우
# print([i.text for i in soup.find_all('a', class_='title_link')])
#print([i.text for i in soup.find_all('span', class_='sub')])
# print(i.text for i in soup.find_all('a', class_='dsc_link'))

date = []
for i in soup.find_all('span', class_='sub'):
    if i.text not in ["'\n제주도\n'관련광고", "도움말"]:
        date.append(i.text.strip())
del date[-1]
print(date)


#웹사이트의 html 구조가 달라질 수 있으므로, 직접 html 태그를 확인하여 값을 넣어주세요.
title = [i.text for i in soup.find_all('a', class_='title_link')]
date = []
for i in soup.find_all('span', class_='sub'):
    if i.text not in ["'\n제주도\n'관련광고", "도움말"]:
        date.append(i.text.strip())
del date[-1]
content = [i.text for i in soup.find_all('a', class_='dsc_link')]


# date = [i.text for i in soup.find_all('span', class_='sub') ]

# print(soup.find_all('span', class_='sub'))

# print(f"Length of titles: {len(title)}")
# print(f"Length of dates: {len(date)}")
# print(f"Length of contents: {len(content)}")

df = pd.DataFrame({'title':title, 'date':date, 'content':content})
print(df)