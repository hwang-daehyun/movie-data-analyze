## 선형 회귀 실습

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
dataset =pd.read_csv("C:\\Users\\User\\Desktop\\ScikitLearn\\LinearRegressionData.csv")

# .values를 해야 차원형 가로 세로로 들어감
# .values는 pandas 객체에서 넘파이 배열로 데이터를 변환하는 데 사용되며, 이는 기계 학습 작업을 수행할 때 필요한 데이터 형태를 제공

X = dataset.iloc[:, :-1].values  # 처음부터 마지막 컬럼 직전까지의 데이터 (독립 변수 - 원인)
y = dataset.iloc[:, -1].values  # 마지막 컬럼 데이터 (종속 변수 - 결과)

reg = LinearRegression()  #객체 생성
reg.fit(X,y)  # .fit으로 훈련 시킨다는 거임
y_pred = reg.predict(X) # X에 대한 예측값

plt.scatter(X,y, color='b') # 산점도
plt.plot(X, y_pred, color='g') # 선그래프
plt.title("Score by hours") # 제목
plt.xlabel('hours')
plt.ylabel('Score')
# plt.show()


'''print('9시간 공부했을 때 예상 점수 : ', reg.predict([[9], [8], [7]]))'''  # 괄호를 두개 쓴 이유는 2차원이기 때문이다.

# 맞는지 확인해보기
print(reg.coef_) #기울기 (m)
print(reg.intercept_) # y절편 (b)    공식 y = mx + b
print(reg.coef_*9 + reg.intercept_)   # 9시간 공부시 93.77478776이 나온 것을 확인