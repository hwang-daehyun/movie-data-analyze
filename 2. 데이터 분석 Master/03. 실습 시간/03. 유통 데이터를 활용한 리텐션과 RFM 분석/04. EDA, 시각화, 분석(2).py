import pandas as pd
import plotly.express as px

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



#- 매출
amount_by_date = data.groupby('data_ymd')[['amount']].sum().reset_index()
fig = px.line(data_frame=amount_by_date, x='data_ymd', y='amount')
'''fig.show()'''

#- 주문고객수
customer_count_by_date = data.groupby('data_ymd')[['CustomerID']].nunique().reset_index().rename({'CustomerID' : 'customer_count'}, axis=1)
fig = px.line(data_frame=customer_count_by_date, x='data_ymd', y='customer_count')
'''fig.show()'''

#- 주문단가
invoice_count_by_date = data.groupby('data_ymd')[['InvoiceNo']].nunique().reset_index().rename({'InvoiceNo' : 'invoice_count'}, axis=1)
'''print(invoice_count_by_date.head())'''

invoice_amount = pd.merge(amount_by_date, invoice_count_by_date, on='data_ymd')
invoice_amount['amount_per_invoice'] = invoice_amount['amount'] / invoice_amount['invoice_count']


### [2] 리텐션 분석: 시간의 흐름에 따라 고객들은 얼마나 남고 얼마나 이탈했는가?

#- 연월 단위로 고객번호, 영수증번호 전처리
# drop_duplicates() -> 해당 컬럼들의 중복을 제거하고 유니크한 값만 남게 하는 것
# to_period('M') -> 연월데이터로 처리하는 것
retention_base = data[['CustomerID', 'InvoiceNo', 'data_ymd']].drop_duplicates()
retention_base['data_ym'] = retention_base['data_ymd'].dt.to_period('M')

#- 날짜 범위 수정
'''print(min(data['data_ymd'].unique()))
print(max(data['data_ymd'].unique()))'''

retention_base = retention_base.query('data_ymd <= "2011-11-30"') #12월 데이터를 포함하면 2011년 12월 데이터는 리텐션이 낮을 수 밖에 없으므로 12월 데이터 제외
'''print(min(retention_base['data_ymd'].unique()))
print(max(retention_base['data_ymd'].unique()))
'''

#- 리텐션 계산
date_ym_list = sorted(list(retention_base['data_ym'].unique()))

from tqdm import tqdm

retention = pd.DataFrame()
for s in tqdm(date_ym_list):
    for t in date_ym_list:
        period_start = s
        period_target = t

        if period_start <= period_target:
            period_start_users = set(retention_base.query('data_ym == @period_start')['CustomerID'])
            period_target_users = set(retention_base.query('data_ym == @period_target')['CustomerID'])

            retained_users = period_start_users.intersection(period_target_users)

            retention_rate = len(retained_users) / len(period_start_users)

            temp = pd.DataFrame({'cohort':[period_start], 'data_ym':[period_target], 'retention_rate':[retention_rate]})

            retention = pd.concat([retention, temp])

retention['cohort_size(month)'] = retention.apply(lambda x: (x['data_ym'] - x['cohort']).n, axis=1)
'''print(retention.head())'''

retention['cohort'] = retention['cohort'].astype(str)
retention['data_ym'] = retention['data_ym'].astype(str)
retention_final = pd.pivot_table(data=retention, index='cohort', columns='cohort_size(month)', values='retention_rate')
'''print(retention_final)'''
fig = px.imshow(retention_final, text_auto='.2%', color_continuous_scale='Burg')
'''fig.show()'''

#- 리텐션 커브
retention_curve = retention.groupby('cohort_size(month)')[['retention_rate']].mean().reset_index()
print(retention_curve)

fig = px.line(data_frame = retention_curve, x='cohort_size(month)', y='retention_rate', title='리텐션 커브')
fig.update_yaxes(tickformat='.2%')
fig.show()