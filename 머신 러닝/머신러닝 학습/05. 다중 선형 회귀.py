## 다중 선형 회귀


## 원-핫 인코딩
# -> 쉽게 표현하고 싶은 값만 1로 나머지는 모두 0으로
# -> 범주형(문자)를 찢어 변수로 만들고 그 문자에 해당하는 변수들만 1로 나머지는 0으로 하는 거다


## 다중 공선성
# -> 독립 변수들 간에 서로 강한 상관관계를 가지면서 회귀계수 추정의 오류가 나타나는 문제
# -> D1 + D2 + D3 = 1 항상 1이어야함
# -> D3 = 1 - (D1+D2) 즉, 변수가 n개면 n-1개만 사용 하는 것.
# -> 독립변수 간 높은 상관으로 독립변수 중 하나를 없애 상관관계를 낮추는것


## 실습(원-핫 인코딩).
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


dataset = pd.read_csv("C:\\Users\\dhwhang\\Desktop\\PythonMLWorkspace(LightWeight)\\ScikitLearn\\MultipleLinearRegressionData.csv")


## 만약 새로운 방법을 안쓰고 원-핫 인코딩 작업을 할거라면 아래와 같이 작업을 진행.

'''home = []
library = []
cafe = []'''

'''for index, row in dataset.iterrows():
    if row['place'] == 'Home':
        home.append(1)
    else:
        home.append(0)

    if row['place'] == 'Library':
        library.append(1)
    else:
        library.append(0)

    if row['place'] == 'Cafe':
        cafe.append(1)
    else:
        cafe.append(0)
'''

'''dataset['Home'] = home
dataset['Library'] = library
dataset['Cafe'] = cafe'''

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values



ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop='first'), [2])] , remainder='passthrough')
# remainder='passthrough' 해당 컬럼이 아닌 경우는 그냥 pass 하는 의미

# 1.0 = Home / 0.0 = Library (Home 기준으로)
X = ct.fit_transform(X)





## 실습(다중 선형 회귀) - 데이터 세트 분리
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

## 실습(다중 선형 회귀) - 학습 다중 선형 회귀
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train, y_train)

## 실습(다중 선형 회귀) - 예측값과 실제 값 비교 (테스트 세트)
y_pred = reg.predict(X_test)
'''print(y_pred)'''
# - 결과 [ 92.15457859  10.23753043 108.36245302  38.14675204]

'''print(y_test)'''
# - 결과 [ 90   8 100  38]

'''print(reg.coef_)'''
# - 결과 [-5.82712824 -1.04450647 10.40419528 -1.64200104]  순서대로 (집, 도서관, 카페는 0, 1시간당 상승 점수, 결석 1번당 -1.64점씩 부정적인 영향을 준다)

'''print(reg.intercept_)'''

## 실습(다중 선형 회귀) - 모델 평가
print(reg.score(X_train,y_train)) # 훈련 세트
print(reg.score(X_test,y_test)) # 테스트 세트