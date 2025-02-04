import pandas as pd


#- 불러오기
# - `데이터변수 = pd.read_csv(파일경로)`
#- 저장하기
# - `데이터변수.to_csv(파일경로)`


# 엑셀 파일 저장하기
'''
file_path = "C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\titanic_train.csv"'''


# `index_col`: 인덱스로 사용할 컬럼
# `usecols`: 사용할 컬럼

# index_col : 인덱스로 사용할 컬럼
# usecols : 사용할 컬럼

'''
data = pd.read_csv(file_path, index_col = 0)
data2 = pd.read_csv(file_path, index_col = 'PassengerId', usecols= ['PassengerId', 'Survived', 'Pclass', 'Age' ])

print(data.head())
print(data2.head())

csv_file_path = "C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\csv_test.csv"
data2.to_csv(csv_file_path)'''

# 엑셀 파일 불러오기

#- 불러오기
# - `데이터변수 = pd.read_excel(파일경로, sheet_name=시트이름)`
#- 저장하기
# - `데이터변수.to_excel(파일경로, sheet_name=시트이름)`

'''
csv_file_path = "C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\titanic_train.xlsx"'''

# `header`: 컬럼 이름으로 사용할 행
# `index_col`: 인덱스로 사용할 컬럼
# `usecols`: 사용할 컬럼

'''
data = pd.read_excel(csv_file_path, sheet_name='시트1', header=1)
print(data.head())
'''
# 웹 html 파일 
# - `pd.read_html(html경로)`
# - `encoding`: 한글이 깨져서 나올 때 `utf-8/cp949`로 설정합니다. 

html_path = 'https://finance.naver.com/sise/sise_quant.naver'

'''quant_data_list = pd.read_html(html_path)'''

try:
    quant_data_list = pd.read_html(html_path, encoding='cp949')
except UnicodeDecodeError:
    try:
        quant_data_list = pd.read_html(html_path, encoding='cp949')
    except UnicodeDecodeError:
        quant_data_list = pd.read_html(html_path, encoding='cp949')

# Display the data
for table in quant_data_list:
    print(table)

'''quant_data_list = pd.read_html(html_path, encoding='utf-8')

print(quant_data_list)'''