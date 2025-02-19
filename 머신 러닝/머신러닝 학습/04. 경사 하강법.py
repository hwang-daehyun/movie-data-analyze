## 경사 하강법

# 0인 지점까지 올 수 있는 보폭을 학습률이라고 한다

# 최적의 파라미터를 찾기 위해서 훈련 셋팅된 모든 데이터를 한번 씩 다 사용해보는 것이 에포크라함.

# -> 이걸 보완하기 위해서 나온데 확률적 경사 하강법
      #-> 네 단계마다 딱 하나의 데이터만 선택하여 기울기를 계산하는것

## 경사 하강법 실습
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import SGDRegressor  # 확률적 경사 하강법
dataset =pd.read_csv("C:\\Users\\dhwhang\\Desktop\\PythonMLWorkspace(LightWeight)\\ScikitLearn\\LinearRegressionData.csv")


X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values 

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0) 

reg = LinearRegression()
reg.fit(X_train, y_train)

# 경사 하강법 시작
# max_iter : 훈련 세트 반복 횟수 (Epoch 횟수)
# eta0 : 학숩률 (learning rate)

# 지수표기법
# 1e-3 : 0.001(10^-3)
# 1e-4 : 0.0001(10^-4)
# 1e+3 : 1000(10^3)
# 1e+4 : 10000(10^4)

#sr = SGDRegressor(max_iter=200, eta0=1e-4, random_state=0, verbose=1)
sr = SGDRegressor(max_iter=1000, eta0=1e-4, random_state=0, verbose=1)
sr.fit(X_train, y_train)


plt.scatter(X_train,y_train, color='b') # 산점도
plt.plot(X_train, sr.predict(X_train), color='g') # 선그래프
plt.title("Score by hours(train data,SGD)") # 제목
plt.xlabel('hours')
plt.ylabel('Score')
plt.show()

'''print(sr.coef_, "SGD")
print(reg.coef_)
print(sr.intercept_, "SGD")
print(reg.intercept_)'''

print(sr.score(X_test,y_test))
print(sr.score(X_train,y_train))