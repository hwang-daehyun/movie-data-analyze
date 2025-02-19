## 데이터 세트 분리
# -> 이미 가지고 있는 데이터를 가지고 모델을 평가 하기 위해서 데이터 세트를 분리하는 작업을 함.
# -> 훈련 세트와 테스트 세트를 나눔 8~7:2~3으로

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split  #<- 얘를 쓰면 튜플 형태로 데이터가 4개가 나와진다

dataset =pd.read_csv("C:\\Users\\User\\Desktop\\ScikitLearn\\LinearRegressionData.csv")

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values 

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0) #test_size=0.2 이건 테스트 세트를 20퍼 쓰겠다는  말이다.
'''print(X, len(X))'''
'''print(X_train, len(X_train))'''  # 훈련 세트 X, 개수
'''print(X_test, len(X_test))'''    # 테스트 세트 X, 개수
'''print(y, len(y))'''
'''print(y_train, len(y_train))'''  # 훈련 세트 y, 개수
'''print(y_test, len(y_test))'''    # 테스트 세트 y, 개수

## 분리된 데이터를 통한 모델링
reg = LinearRegression()
reg.fit(X_train, y_train)  #훈련 세트로 학습

# 훈련 세트로 데이터 시각화
'''plt.scatter(X_train,y_train, color='b') # 산점도
plt.plot(X_train, reg.predict(X_train), color='g') # 선그래프
plt.title("Score by hours(train data)") # 제목
plt.xlabel('hours')
plt.ylabel('Score')
plt.show()'''

# 테스트 세트로 데이터 시각화
'''plt.scatter(X_test,y_test, color='b') # 산점도
plt.plot(X_train, reg.predict(X_train), color='g') # 선그래프
plt.title("Score by hours(test data)") # 제목
plt.xlabel('hours')
plt.ylabel('Score')
plt.show()'''

'''print(reg.coef_)
print(reg.intercept_)'''

# 모델 평가
print(reg.score(X_test,y_test))  # 테스트 세트를 통한 모델 평가
print(reg.score(X_train,y_train)) # 훈련 세트를 통한 모델 평가