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

import pandas as pd
from konlpy.tag import Mecab

mecab = Mecab()

news_data = pd.read_excel("C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part3) 파이썬 데이터 분석 실습\\Data\\실습8_ 직접 크롤링하기 - 뉴스기사 키워드 추출을 통한 주식 종목 이슈 분석\\news.xlsx")

news_data['Noun'] = news_data['title'].apply(lambda x: [i[0] for i in mecab.pos(x) if i[i] in ('NNG', 'NNP') and len(i[0]) > 1])

'''print(news_data.head())'''

news_data['data_ym'] = [str(i)[:6] for i in news_data['data_ymd']]
news_keyword = news_data.groupby(['keyword', 'data_ym'])[['Noun']].sum().reset_index()
'''print(news_keyword.head())'''

from collections import Counter

news_keyword['most_count'] = news_keyword['Noun'].apply(lambda x: dict(Counter(x).most_common()))
'''print(news_keyword.head())'''


def nng_clean(keyword,nng):
    if keyword == 'LG에너지솔루션':
        nng_clean == [i for i in nng if i not in ['너지', '솔루션']]
    elif keyword == 'SK하이닉스':
        nng_clean == [i for i in nng if i not in ['하이닉스']]
    else:
        nng_clean == [i for i in nng if i not in ['삼성전자', '삼성', '전자']]

    return nng_clean


news_keyword['noun_clean'] = news_keyword.apply(lambda x: nng_clean(x['keword'], x['Noun']), axis=1)
news_keyword['most_common'] = news_keyword['noun_clean'].apply(lambda x: dict(Counter(x).most_common()))
print(news_keyword.head())

## **분석**

import plotly.express as px

for y in ['삼성전자','LG에너지솔루션','SK하이닉스']:
    fig = px.line(data_frame = stock_close.reset_index(), x='Date', y=y)
    fig.show()



import matplotlib.pyplot as plt
plt.rc('font', family='NanumGothic')

from wordcloud import WordCloud

path = '/user/share/fonts/truetype/nanum/NanumGothic.ttf'
wc = WordCloud(font_path = path,
               background_color='white',
               width=1000,
               height=1000)

date_ym_list = sorted(news_keyword['date_ym'].unique())

for k in ['삼성전자','LG에너지솔루션','SK하이닉스']:
    fig = plt.figure(figsize=(25,20))
    for i in range(12):
        wc.generate_from_frequencies(news_keyword.query(f'keyword == "{k}" and date_ym == "{date_ym_list[i]}"')['most_common'].values[0])
        ax = fig.add_subplot(3,4,i+1)
        ax.imshow(wc, interpolation='bilinear')
        ax.set_xlabel(date_ym_list[i])
        ax.set_xticks([]), ax.set_yticks([])
    fig.suptitle(k)
    fig.tight_layout()
    plt.show()


stock_close['date_ym'] = [i[:6] for i in stock_close.index.strftime('%Y%m%d')]
print(stock_close.head())


news_keyword['TOP20'] = news_keyword['noun_clean'].apply(lambda x: str(dict(Counter(x).most_common(20))))

stock_close_keyword = stock_close.reset_index()\
.merge(news_keyword.query('keyword == "삼성전자"')[['date_ym','TOP20']], on='date_ym').rename({'TOP20':'삼성전자 월별 TOP20 키워드'}, axis=1)\
.merge(news_keyword.query('keyword == "LG에너지솔루션"')[['date_ym','TOP20']], on='date_ym').rename({'TOP20':'LG에너지솔루션 월별 TOP20 키워드'}, axis=1)\
.merge(news_keyword.query('keyword == "SK하이닉스"')[['date_ym','TOP20']], on='date_ym').rename({'TOP20':'SK하이닉스 월별 TOP20 키워드'}, axis=1)
print(stock_close_keyword)

for y in ['삼성전자','LG에너지솔루션','SK하이닉스']:
    fig = px.line(data_frame = stock_close_keyword, x='Date', y=y, hover_data=f'{y} 월별 TOP20 키워드')
    fig.show()