from user_agent import generate_user_agent, generate_navigator
user_agent = generate_user_agent()
user_agent
 
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import random
import time
from tqdm.notebook import tqdm

#pd.date_range('2018-01-01', '2023-08-31', freq='MS').strftime('%Y.%m.%d') => freq='MS' 각 월의 첫번째날 / freq='M' 각 월의 마지막날   

first_day = pd.date_range('2018-01-01', '2024-10-31', freq='MS').strftime('%Y.%m.%d')
last_day = pd.date_range('2018-01-01', '2024-10-31', freq='M').strftime('%Y.%m.%d')

# Zip을 통해서 리스트 안에 (first_day, last_day)가 들어가게 만들어 준다.
date_list = list(zip(first_day, last_day))


keyword = '부동산'

data = pd.DataFrame()
for dt in tqdm(date_list):
    dt1 = [dt[0].replace('.',''), dt[1].replace('.','')]

    for num in range(1, 101, 10):
        url = f'https://search.naver.com/search.naver?where=news&query={keyword}&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds={dt[0]}&de={dt[1]}&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Afrom{dt1[0]}to{dt1[1]}&is_sug_officeid=0&office_category=0&service_area=1&start={num}'
        
        user_agent = generate_user_agent()
        headers = {'user-Agent':user_agent}

        res = requests.get(url, headers=headers)
        time.sleep(random.random())
        soup = bs(res.text, 'html.parser')

        # 뉴스 타이틀
        title = [i.text for i in soup.find_all('a', class_='news_tit')]
        # 뉴스 링크
        link = [i['href'] for i in soup.find_all('a', class_='news_tit')]
        # 뉴스 언론사
        press = [i.text for i in soup.find_all('a', class_='info press')]

        temp = pd.DataFrame({'title':title, 'link':link, 'press':press, 'date_ym':dt1[0][:6]})
        data = pd.concat([data,temp])


data = pd.read_excel('C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part3) 파이썬 데이터 분석 실습\Data\\실습7_ 직접 크롤링하기 - 부동산 뉴스기사 키워드 추출을 통한 연도별 이슈 분석\\news_data.xlsx')
data


data.drop('Unnamed: 0',axis=1, inplace=True)

data['date_ym'] = data['date_ym'].astype(str)

data = data[['title', 'date_ym']]

data.info()
data.head()


from konlpy.tag import Mecab

mecab = Mecab()


# lambda x: [i[0] for i in mecab.pos(x) if i[i] in ('NNG')]  i의 두번째에NNG가 있는 데이터들의 첫번째 데이터를 가져오는 것

data['NNG'] = data['title'].apply(lambda x: [i[0] for i in mecab.pos(x) if i[i] in ('NNG')])

data['year'] = data['date_ym'].apply(lambda x: int(x[:4]))
data.head()


from collections import Counter 


# 각 연도에 해당하는 형태소를 각각 연도의 리스트에 모으는것

nng_2018 = [j for i in data.query('year == 2018')['NNG'] for j in i if j not in ['부동산','전망','시장','집값','투자'] and len(j) > 1]
nng_2019 = [j for i in data.query('year == 2019')['NNG'] for j in i if j not in ['부동산','전망','시장','집값','투자'] and len(j) > 1]
nng_2020 = [j for i in data.query('year == 2020')['NNG'] for j in i if j not in ['부동산','전망','시장','집값','투자'] and len(j) > 1]
nng_2021 = [j for i in data.query('year == 2021')['NNG'] for j in i if j not in ['부동산','전망','시장','집값','투자'] and len(j) > 1]
nng_2022 = [j for i in data.query('year == 2022')['NNG'] for j in i if j not in ['부동산','전망','시장','집값','투자'] and len(j) > 1]
nng_2023 = [j for i in data.query('year == 2023')['NNG'] for j in i if j not in ['부동산','전망','시장','집값','투자'] and len(j) > 1]
nng_2024 = [j for i in data.query('year == 2024')['NNG'] for j in i if j not in ['부동산','전망','시장','집값','투자'] and len(j) > 1]


# 각 연도에 해당하는 형태소를 각각 연도의 리스트에 모은 거를 카운트 해주며 most_common은 가장 많이 나온 단어를 추출 해주는것 현재 100이니 가장 많이 나온 단어 100개 저장
nng_2018_dict = dict(Counter(nng_2018).most_common(100))
nng_2019_dict = dict(Counter(nng_2019).most_common(100))
nng_2020_dict = dict(Counter(nng_2020).most_common(100))
nng_2021_dict = dict(Counter(nng_2021).most_common(100))
nng_2022_dict = dict(Counter(nng_2022).most_common(100))
nng_2023_dict = dict(Counter(nng_2023).most_common(100))
nng_2024_dict = dict(Counter(nng_2024).most_common(100))



import matplotlib.pyplot as plt
plt.rc('font', family='NanumGothic')

from wordcloud import WordCloud

path = '/user/share/fonts/truetype/nanum/NanumGothic.ttf'
wc = WordCloud(font_path = path,
               background_color='white',
               width=1000,
               height=1000,
               max_font_size=300)

dict_list = [nng_2018_dict, nng_2019_dict, nng_2020_dict, nng_2021_dict, nng_2022_dict, nng_2023_dict, nng_2024_dict]
title_list = [i for i in range(2018, 2025)]

fig = plt.figure(figsize=(25,20))
for i in range(len(dict_list)):
    wc.generate_from_frequencies(dict_list[i]) #워드클라우드 생성

    # fig.add_subplot(세로, 가로) 한번에 여러 표를 보이게 하기 위해서 하는것 
    ax = fig.add_subplot(2,3,i+1)
    ax.imshow(wc, interpolation='bilinear')
    ax.set_xlabel(f'{title_list[i]}') #그래프 제목 출력
    ax.set_xticks([]), ax.set_yticks([]) #x축, y축을 없앰
    plt.imshow(wc, interpolation='bilinear')
fig.suptitle('부동산 뉴스 제목 키워드')
fig.tight_layout()
plt.show()