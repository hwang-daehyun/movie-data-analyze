import pandas as pd


data = pd.read_csv("C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part3) 파이썬 데이터 분석 실습\\Data\\실습3_ 유통 데이터를 활용한 리텐션과 RFM 분석\\ecommerce_data.csv")

# InvoiceNo: 영수증번호
# StockCode: 상품번호
# Description: 상품명
# Quantity: 판매수량
# InvoiceDate: 결제날짜
# UnitPrice: 개당 가격
# CustomerID: 고객번호
# Country: 나라


#고객 분석을 할 것이므로 CustomerID가 없는 행은 제거한다.
# 만약 subset을 사용하지 않으면 null값이 있는 모든 인자가 삭제됨.
# 하지만 subset을 추가하면 해당 컬럼을 기준으로 결측지 삭제 됨.

data.dropna(subset=['CustomerID'], inplace=True)
#data.dropna(inplace=True)
'''print(data.info())'''

# 데이터 타입 변경
# 시간에 따른 추이를 보기위해 형태 변환 필요
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], format='%m/%d/%Y %H:%M')
# 여기서 CustomerID를 먼저 int형으로 바꾼후 str로 변경한 이유는 소수점을 없애기 위해
data['CustomerID'] = data['CustomerID'].astype(int).astype(str)
'''print(data.info())
print(data.head(5))'''

# 날짜 컬럼 추가하기
data['data_ymd'] = data['InvoiceDate'].dt.date.astype('datetime64[ns]')
data['year'] = data['InvoiceDate'].dt.year
'''print(data.head())'''

# 매출컬럼 추가하기
data['amount'] = data['UnitPrice'] * data['Quantity']
'''print(data.head())'''

# 분석의 편의를 위하여 취소 주문 제외
data = data.query('Quantity > 0')
'''print(data.info())'''

# 여기서 의문 -> 취소가 9000개 정도 있는데 어느 날짜에 취소가 많은지도 보는 것도 한번 하는게 좋을 듯.

import plotly.express as px
