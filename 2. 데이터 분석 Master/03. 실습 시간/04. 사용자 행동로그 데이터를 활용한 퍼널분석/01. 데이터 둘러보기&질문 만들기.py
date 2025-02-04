import pandas as pd
import plotly.express as px

data = pd.read_csv("C:\\Users\\dhwhang\\Desktop\\쉽게 배우는 파이썬 데이터 분석\\패스트 캠퍼스\\drive-download-20240910T020903Z-001\\Data\\실습4_ 사용자 행동 로그 데이터를 활용한 퍼널 분석\\ecommerce_behavior.csv")

'''print(data.head())'''
data.drop('Unnamed: 0', axis=1 ,inplace=True)
'''print(data.head())'''

print(data.info())

#- event_time: 이벤트가 발생한 시각
#- event_type: 이벤트 종류
#    - view: 상품을 조회
#    - cart: 상품을 카트에 추가
#    - remove_from_cart: 상품을 카트에서 제거
#    - purchase: 구매
#- product_id: 상품번호
#- category_id: 카테고리번호
#- category_code: 카테고리명
#- brand: 브랜드명
#- price: 상품 가격
#- user_id: 고객번호
#- user_session: 세션



#Index(['Unnamed: 0', 'event_time', 'event_type', 'product_id', 'category_id',
#       'category_code', 'brand', 'price', 'user_id', 'user_session'],

## **질문 만들기**
#- DAU(일간 활성 사용자수) 추이는?
#    - 어느 요일에 가장 많이 방문하는가?
#- 사이트 체류시간 평균은?
#    - 조회만 한 유저, 카트에 담은 유저, 구매까지 한 유저별로 체류시간이 어떻게 다른가?
#- 퍼널 분석
#    - 어느 단계에서 유저들이 가장 많이 이탈하는가?