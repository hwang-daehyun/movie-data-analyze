import pandas as pd
import matplotlib.pyplot as plt

## Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리

# 1. Series
# -> 1차원 데이터(정수, 실수, 문자열 등)

#Series 객체 생성
'''temp = pd.Series([-20, -10, 10, 20])'''
'''print(temp[0])''' # 1월 온도

#Series 객체 생성 (Index 지정)
'''temp = pd.Series([-20, -10, 10, 20], index= ['Jan', 'Fed', 'Mar', 'Apr'])'''
'''print(temp['Jan'])''' #Index Jan에 해당하는 데이터 출력

# 2. DataFrame
# -> 2차원 데이터(Series 들의 모음)

# Data 준비
'''data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}
'''

# DataFrame 객체 생성
'''df=pd.DataFrame(data)'''

# 데이터 접근
'''print(df[['이름','키']])''' #만약 여러 컬럼의 데이터를 불러오고 싶다면 [[]]로 해야한다.

# DataFrame 객체 생성(Column 지정)
'''df2 = pd.DataFrame(data=data, columns=['이름','키','학교'] )
print(df2)'''


# 3. INDEX
# -> 데이터에 접근할 수 있는 주소 값

'''df=pd.DataFrame(data=data, index=['1번', '2번','3번','4번','5번','6번','7번','8번'])'''


# INDEX 이름 설정
'''df.index.name = '지원번호'''


# INDEX 초기화
'''print(df.reset_index())'''  #-> 이럴경우 인덱스에 들어간 정보(1번, 2번 ......8번)가 새로운 데이터에 들어와짐.
'''print(df.reset_index(drop=True))''' #-> 이럴경우 기존 인덱스에 있는 정보는 데이터가 되는데 아닌 삭제된다.
'''print(df.reset_index(drop=True, inplace=True))''' #-> 이럴경우 인덱스가 삭제된 정보로 저장된다.

# INDEX 설정(원하는 변수로 설정)
'''df.set_index('이름', inplace=True)'''

# INDEX 정렬 (index 를 기준으로 오름차순, 내림차순 정렬)

'''print(df.sort_index())''' #인덱스 기준 오름차순으로 정렬


'''print(df.sort_index(ascending=False))''' #인덱스 기준 내림차순으로 정렬



# 데이터 확인
data=pd.read_excel('score.xlsx',index_col='지원번호')

# 데이터프레임 확인

'''print(data.describe())
print(data.info())'''

'''print(data.head())'''  # 처음 5개의 row 데이터만 가져옴.

'''print(data.tail())'''  # 마지막 5개의 row 데이터만 가져옴.

'''print(data.values)
print(data.index)
print(data.columns)'''

'''print(data['키'].describe())
print(data['키'].min())
print(data['키'].max())
print(data['키'].nlargest(3)) # 키 변수에서 가장 큰 3명만 만 약 숫자 안 넣고 돌이면 기본 5명만 나옴 헤드와 비슷
print(data['키'].mean())
print(data['키'].sum())
print(data['SW특기'].count())  # 존재하는 데이터에서 카운트 값으로
print(data['학교'].unique())  # 중복을 제거한 val들을 제시해 준다
print(data['학교'].nunique())   #중복은 제거한 val들의 카운드 값을 제시'''


# 6. 데이터 선택(기본)

# Column선택 (label)
'''print(data[['이름', '키']])'''

# Column선택 (정수index)
'''print(data.columns) 
print(data.columns[0]) 
print(data.columns[2]) '''
'''print(data[data.columns[0]])''' #해당 컬럼의 데이터를 가져올때 만약 컬럼명을 모르면 이와 같이 하면 됨. -> data['이름']과 동일하게 동작함

# 슬라이싱
'''print(data['영어'][0:5])'''   #영어 컬럼에서 0~4번째 인덱스에 해당하는 데이터값만 가져옴
'''print(data[['영어','키']][:5])''' #영어와 키 컬럼에서 0~4번째 인덱스에 해당하는 데이터값만 가져옴
'''print(data[3:])'''

# 7. 데이터 선택(loc)
# -> 이름을 이용해서 원하는 row에서 원하는 데이터를 선택 
'''print(data.loc['1번'])''' #index 5번에 해당하는 전체 데이터를 가져옴
'''print(data.loc['1번','국어'])''' #index 1번의 국어 점수를 불러옴
'''print(data.loc[['1번','2번'],'영어'])''' #index 1번과 2번의 국어 점수를 불러옴
'''print(data.loc[['1번','2번'],['영어','수학']])''' #index 1번과 2번의 영어,수학 점수를 불러옴
'''print(data.loc['1번':'5번','국어':'사회'])'''

##iloc와 loc의 차이점 iloc같은 경우에는 정수를 통해 위치를 찾고, loc같은 경우에는 변수 혹은 인덱스 번호를 통해 위치를 찾음

# 8. 데이터 선택(iloc)
# -> 위치를 이용해서 원하는 row에서 원하는 col선택
'''print(data.iloc[0])''' #0번째 위치 데이터
'''print(data.iloc[0:5])''' #0~4번째 위치의 데이터
'''print(data.iloc[0,1])''' #0번째 위치의 1번째(학교) 데이터
'''print(data.iloc[4,2])''' #5번 학생의 키 데이터
'''print(data.iloc[[0,1],2])''' #0,1번째 위치의 학생의 2번째(키) 데이터
'''print(data.iloc[[0,1],[3,4]] )''' #0, 1번째 위치의 학생의 3, 4번째 데이터(국어,영어)
'''print(data.iloc[:5,3:8])''' #0 ~ 4번째 위치의 학생 중에서, 3 ~ 7번째 데이터(국어:사회)

# 9. 데이터 선택(조건)
# -> 조건에 해당하는 데이터를 선택

'''print(data['키']>=185)''' # 학생들의 키가 185 이상인지 여부를 True/False (블리언) 형태로 알려줌

'''filt=(data['키']>=185)'''
'''print(data[filt])'''
'''print(data[~filt])''' #filter를 역으로 적용
'''print(data[data['키']>=185])'''  #=print(data[filt]) 랑 같은거다
'''print(data.loc[data['키']>=185,'수학'])'''  #키가 185이상인 학생들의 수학 데이터
'''print(data.loc[data['키']>=185,['이름','국어','수학']])'''

# 다양한 조건
# & 조건(그리고)
'''print(data.loc[(data['키']>=185) & (data['학교']=='북산고')])''' #키가 185이상인 북산고 학생 데이터

# | 조건(또는)
'''print(data.loc[(data['키']<170) | (data['키']>200)])''' #키가 170보다 작거나, 200보다 큰 학생 데이터

# str 함수
'''filt=data['이름'].str.startswith('송')'''  # 송씨 성을 가진 사람
'''print(data[filt])'''

'''filt=data['이름'].str.contains('태')'''  # 이름에 태가 있는 사람
'''print(data[~filt])'''

'''langs=['Python', 'Java']'''
'''filt=data['SW특기'].isin(langs)'''  #SW 특기가 Python이거나 Java인 사람을 뽑는것(langs 변수에 리스트로 넣은 후) isin을 통해 들어가 있는 걸 찾는다.
'''print(data[filt])'''  #-> 이럴경우 대문자 PYTHON은 추출이 안된다

# 다른 방법  #->lower을 추가하여 모든 SW특기의 문자를 소문자로 바꾸어 진행하면 전체 출력 가능
'''langs=['python','java']
flit=data['SW특기'].str.lower().isin(langs)
print(data[flit])'''

'''filt=data['SW특기'].str.contains('Java',na=False)'''     #->contains로 할 경우 Nan인 데이터 때문에 오류가 남. 
'''print(data[filt])'''                                     #-> 그래서 contains안에 java다음 na를 어떻게 처리할지 정희할 수 있음
                                                            #-> 이럴 경우 na은 다 False로 감.

#만약 바로 적용시키고 싶다면 inplace=True로 쓰면 됨.

# 10. 결측지
# 데이터 채우기 fillna
'''print(data.fillna(''))''' #-> Nan 데이터를 빈 칸으로 채움
'''print(data.fillna('없음'))'''

import numpy as np

'''data['학교'] = np.nan ''' #-> 학교 데이터 전체를 Nan로 채움

'''print(data.fillna('모름'))'''

# 일부 데이터만 채우기
'''data['SW특기'].fillna('확인중', inplace=True) '''#->SW특기 데이터 중에서 Nan에 대해서만 채움
'''print(data)'''

# 데이터 제외하기 Dropna
'''print(data.dropna())''' #->전체 데이터 중에서 Nan을 포함한 데이터를 삭제

# - axis의 속성은 : index or columns
# index로 할 경우 인덱스 기준으로 nan를 삭제, columns은 nan데이터가 있는 컬럼을 기준으로 삭제
# - how의 속성은 : any or all
# any는 데이터 중 하나라도 그 선정한 데이터가 있는 경우 all은 전체가 선정한 데이터일때 삭제하는 거임
print(data.dropna(axis='index', how='any'))
print(data.dropna(axis='columns', how='any')) #->이경우 SW특기가 다 삭제됨.

data['학교'] = np.nan
print(data.dropna(axis='columns', how='all')) # 이럴 경우 학교가 전체 nan기때문에 삭제되고, SW특기는 살아있음.


# 11. 데이터 정렬
'''print(data.sort_values('키',ascending=False))''' # 키 기준으로 오름차순 but, ascending=False로 할경우 내림차순으로 됨.(기본이 오름차순)
'''print(data.sort_values(['수학','영어'],ascending=False))''' # 수학, 영어 점수 기준으로 내림차순

'''print(data.sort_values(['수학','영어'],ascending=[True,False]))''' #만약 수학 점수는 오름차순으로 하고 영어 점수는 내림차순으로 하고 싶을 경우(이럼, 수학 오름차순 안에서 영어 내림차순이 됨)
'''print(data['키'].sort_values())
print(data['키'].sort_values(ascending=False))'''
'''print(data.sort_index())'''

# 12. 데이터 수정

#Column 수정
'''data['학교'].replace({'북산고':'상북고'},inplace=True)
print(data)'''

'''data['SW특기'] = data['SW특기'].str.lower()'''   # SW특기에 있는 문자들을 모두 소문자로 바꾼걸 SW특기에 다시 넣는 것
'''print(data)'''

'''data['SW특기'] = data['SW특기'].str.upper()'''   # SW특기에 있는 문자들을 모두 대문자로 바꾼걸 SW특기에 다시 넣는 것
'''print(data)'''

'''data['학교']=data['학교'] + '등학교' '''  # 학교 데이터에 등학교를 추가하는 것
'''print(data)'''

#Column 추가
'''data['총합'] = data['국어'] + data['영어'] + data['수학'] + data['과학'] + data['사회']'''
'''data['결과'] = 'Fail'  '''#결과 Column을 추가하고 전체 데이터는 Fail로 초기화
'''data.loc[data['총합'] > 400, '결과'] = 'Pass' '''#총합이 400보다 큰 데이터에 대해서 결과를 Pass로 업데이트

#Column 삭제
'''print(data.drop(columns=['총합']))'''  #총합 Column을 삭제
'''print(data.drop(columns=['국어','영어','수학']))'''  #국어,영어,수학 Column을 삭제

#Row 삭제
'''print(data.drop(index='4번'))''' # 4번 학생 row데이터 삭제.
'''filt=data['수학'] < 80'''   #수학 점수가 80점 미만 필터링
'''print(data[filt].index) '''
'''print(data.drop(index=data[filt].index))''' #수학 점수가 80점 미만인 인덱스를 삭제함.

#Row 추가
'''data.loc['9번'] = ['이정환', '해남고등학교', 184, 90 , 90, 90, 90, 90, 'Kotlin', 450, 'Pass']'''

#Cell 수정
'''data.loc['4번', 'SW특기'] = 'Python' ''' #4번 학생의 SW특기 데이터를 Pythin으로 변경
'''data.loc['5번', ['학교','SW특기']] = ['능남고등학교','C']'''  #5번 학생의 SW특기 데이터와 학교 데이터를 수정


#column 순서 변경
'''cols = list(data.columns)'''
'''data=data[[cols[-1]]+cols[0:-1]]'''  #맨 뒤에 있는 결과 col을 앞으로 가져오고, 나머지 col들과 합쳐서 순서 변경

#Column 이름 변경
'''data.rename(columns={'결과': 'Result', '이름' : 'name', '학교' :'School'}, inplace=True)
print(data)'''


# 13. 함수 적용
# 데이터에 함수 적용(apply)
'''def add_cm(height):
    return str(height) + 'cm' '''

'''data['키'] = data['키'].apply(add_cm)''' # 키 데이터에 대해서 add_cm 함수를 호출한 결과 데이터를 반영


'''def capitalize(lang):
    if pd.notnull(lang):           #Nan이 아닌지를 확인하는 것
        return lang.capitalize()   #첫 글자는 대문자로, 나머지는 소문자로
    return lang'''

'''data['SW특기'] = data['SW특기'].apply(capitalize) '''

'''data['SW특기'].str.capitalize()'''   #얘도 똑같은 결과값 제공함.

# 14. 그룹화
#->동일한 값을 가진 것들끼리 합쳐서 통계 또는 평균 등의 값을 계산하기 위해 사용

data.groupby('학교')
'''print(data.groupby('학교').get_group('북산고'))
print(data.groupby('학교').get_group('능남고'))
print(data.groupby('학교')[['수학', '영어']].mean())'''  #계산 하고 싶은 데이터들의 평균값
'''print(data.groupby('학교').size())'''                     #각 그룹의 크기
'''print(data.groupby('학교').size()['능남고']) '''            #학교로 그룹화를 한 뒤에 능남고에 해당하는 데이터의 수


data['학년'] = [3,3,2,1,1,3,2,2]   #학년 컬럼 추가

'''print(data.groupby(['학교', '학년'])[['키','국어','영어','수학','사회','과학']].mean()) 
print(data.groupby('학년')[['키','국어','영어','수학','사회','과학']].mean()) 
print(data.groupby('학년')[['키','국어','영어','수학','사회','과학']].mean().sort_values('키',ascending= False)) '''
'''print(data.groupby(['학교','학년'])[['키','국어','영어','수학','사회','과학']].sum()) '''
'''print(data.groupby(['학교'])[['이름','SW특기']].count()) '''

'''school=data.groupby('학교')'''
'''print(school['학년'].value_counts()) '''   #학교를 그룹화를 한 뒤에 학년별 학생 수를 가져옴
'''print(school['학년'].value_counts().loc['북산고'])''' #학교로 그룹화를 한 뒤에 북산고에 대해서 학년별 학생 수를 가져옴
'''print(school['학년'].value_counts(normalize=True).loc['북산고'])'''  #학생들의 수 데이터를 퍼센트로 비교하여 가져옴
'''print(school['학년'].value_counts().loc['능남고'])''' #학교로 그룹화를 한 뒤에 능남고에 대해서 학년별 학생 수를 가져옴
'''print(school['학년'].value_counts(normalize=True).loc['능남고'])'''


# 15. Pandas 퀴즈

data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}
df = pd.DataFrame(data)



# 1) 전체 데이터 중에서 '영화'정보만 출력하시오.
print(df['영화'])
print(df[df.columns[0]])
cols = list(df.columns)
data=df[cols[0]]
print(data)

# 2) 전체 데이터 중에서 '영화', '평점' 정보만 출력하시오.
print(df[['영화','평점']])

# 3) 2015년 이후에 개봉한 영화 데이터 중에서 '영화', '개봉 연도' 정보를 출력하시오.
print(df.loc[df['개봉 연도']>=2015,['영화','개봉 연도']])


# 4) 주어진 계산식을 참고하여 '추천 점수' Column 을 추가하시오
# 추천 점수 = (관객수 * 평점) // 100
#예) 첫 번째 영화인 '명량'의 경우
#추천 점수 = (관객수 1761 * 평점 8.88) // 100 = 156
df['추천 점수'] = (df['관객 수'] * df['평점']) //100
print(df)

# 5) 전체 데이터를 '개봉 연도' 기준 내림차순으로 출력하시오.
print(df.sort_values('개봉 연도', ascending= False))