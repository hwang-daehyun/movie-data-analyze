import pandas as pd
from konlpy.tag import Mecab

#- 형태소 분석
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