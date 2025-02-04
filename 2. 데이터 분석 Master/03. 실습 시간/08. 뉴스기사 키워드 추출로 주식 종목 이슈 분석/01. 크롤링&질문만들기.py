# **주식 데이터 - 뉴스기사 키워드 추출을 통한 주식 종목 이슈 분석**
import matplotlib.pyplot as plt
import FinanceDataReader as fdr
import pandas as pd
import FinanceDataReader as fdr

## **데이터 수집**

#- 주식 데이터 수집

plt.rc('font', family='NanumGothic')

kospi = fdr.StockListing('KOSPI')
'''print(kospi.head())'''


top3 = kospi.head(3)[['Code', 'Name']]
'''print(top3)'''

stock_close = pd.DataFrame()
for i in top3.index:
    temp = fdr.DataReader(top3.loc[i, 'Code'], start='2022-01-01', end='2024-10-31')[['Close']].rename({'Close': top3.loc[i,'Name']}, axis=1)
    stock_close = pd.concat([stock_close, temp], axis=1)

'''print(stock_close)'''

#- 일자별 각 종목 뉴스 제목 수집
from user_agent import generate_user_agent, generate_navigator
user_agent = generate_user_agent()
'''print(user_agent)'''

import requests
from bs4 import BeautifulSoup as bs
import random
import time
from tqdm.notebook import tqdm

date_list = list(stock_close.index.strftime('%Y.%m.%d'))
'''print(date_list)'''

def new_crawling(keyword):
    data = pd.DataFrame()
    for dt in tqdm(date_list):
        dt1 = dt.replace('.','')

        url = f'https://search.naver.com/search.naver?where=news&query={keyword}&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds={dt}&de={dt}&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Afrom{dt1}to{dt1}&is_sug_officeid=0&office_category=0&service_area=1'

        user_agent = generate_user_agent()
        headers = {'User-Aqent':user_agent}

        res = requests.get(url, headers=headers)
        time.sleep(random.random())
        soup = bs(res.text, 'html.parser')

        title = [i.text for i in soup.find_all('a', class_='news_tit')]

        if len(title) < 1: #크롤링이 아무것도 되지 않았으면 루프를 종료, 시간 텀을 가진 뒤 다시 크롤링
            break

        temp = pd.DataFrame({'keyword':keyword, 'title':title, 'date_ymd':dt1})
        data = pd.concat([data, temp])

    return data

keyword_list = ['삼성전자', 'SK하이닉스', 'LG에너지솔루션']

news_data = pd.DataFrame()
for k in keyword_list:
    news = new_crawling(k)
    news_data = pd.concat([news_data, news])

news_data.to_excel('C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part3) 파이썬 데이터 분석 실습\\Data\\실습8_ 직접 크롤링하기 - 뉴스기사 키워드 추출을 통한 주식 종목 이슈 분석\\new_data.xlsx')