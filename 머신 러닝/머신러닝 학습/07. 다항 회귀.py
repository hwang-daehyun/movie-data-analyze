## 다항 회귀
# -> 일차방정식으로 표현하기 힘든 경우 
# -> 독립 변수의 확장
# -> 과소 적합 : 어느정도 데이터를 표현할 수 있지만, 개선이 필요한 것
# -> 과대 적합 : 훈련 데이터에만 너무 맞춰져 실제 데이터에 대해서는 예측을 잘 못하는 경우

## 다항 회귀 실습
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



dataset = pd.read_csv("C:\\Users\\dhwhang\\Desktop\\PythonMLWorkspace(LightWeight)\\ScikitLearn\\PolynomialRegressionData.csv")

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

# 단순 선형 회귀
from sklearn.linear_model import LinearRegression

reg = LinearRegression()  
reg.fit(X,y)

# 데이터 시각화 (전체)

plt.scatter(X,y, color='b')
plt.plot(X,reg.predict(X), color='g')
plt.title("Score by hours (genius)")
plt.xlabel('hours')
plt.ylabel('score')
# plt.show()

print(reg.score(X,y)) # 전체 데이터를 통한 모델 평가

# 다항 회귀
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4) # degree=2라 하면 2차 다항식으로 되는거임
X_poly = poly_reg.fit_transform(X)
# fit_transform를 따로 할 수 있지만, 위에처럼 한번에 쓸수 있음
# poly_reg.fit()
# poly_reg.transform()
'''print(X_poly[:5])'''  # -> [X] -> [X^0, X^1, X^2] 예) X=3이라면 [1, 3, 9]로 변환
'''[[1.   0.2  0.04]  순서대로 X의0승 X의1승 X의2승 
 [1.   0.5  0.25]
 [1.   0.8  0.64]
 [1.   0.9  0.81]
 [1.   1.2  1.44]]'''
lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)  # 변환된 X와 y를 가지고 모델 생성(학습)

# 데이터 시각화(변환된 X와 y)
'''plt.scatter(X,y, color='b')
plt.plot(X,lin_reg.predict(poly_reg.fit_transform(X)), color='g')
plt.title("Score by hours (genius)")
plt.xlabel('hours')
plt.ylabel('score')'''
X_range = np.arange(min(X), max(X), 0.1)  # X의 최소값에서 최대값까지의 범위를 0.1 단위로 잘라서 데이터를 생성
X_range = X_range.reshape(-1,1)  # row 개수는 자동으로 계산, column 개수는 1개
'''print(X_range)'''
plt.scatter(X,y, color='b')
plt.plot(X_range,lin_reg.predict(poly_reg.fit_transform(X_range)), color='g')
plt.title("Score by hours (genius)")
plt.xlabel('hours')
plt.ylabel('score')
# plt.show()

# 공부 시간에 따른 시험 성적 예측
print(reg.predict([[2]]))  # 2시간을 공부했을 때 선형 회귀 모델의 예측
print(lin_reg.predict(poly_reg.fit_transform([[2]]))) # 2시간을 공부했을 때 다항 회귀 모델의 예측

print(lin_reg.score(X_poly,y))



