## 회귀 모델 평가

## MAE (Mean Absolute Error)
# : 실제 값과 예측 값 차이의 절대값들의 평균

# 예) 
'''y    y2     |y - y2|
  15    25        10   
  55    42        13
  50    59         9
  95    76        19
  80    93        13'''

# (10 + 13 + 9 + 19 + 13) / 5 = 12.8


## MSE (Mean Squared Error)
# : 실제 값과 예측 값 차이의 제곱한 값들의 평균

# 예) 
'''y    y2     (y - y2)2
  15    25        100   
  55    42        169
  50    59         81
  95    76        361
  80    93        169'''

# (100 + 169 + 81 + 361 + 169) / 5 = 176


## RMSE (Root Mean Squared Error)
# : MSE 에 루트를 적용 

# 예) 
'''y    y2     (y - y2)2
  15    25        100   
  55    42        169
  50    59         81
  95    76        361
  80    93        169'''

# (100 + 169 + 81 + 361 + 169) / 5 = 루트 176 = 13.27


## R2 (R Square)
# : 결정계수 (데이터의 분산을 기반으로 한 평가 지표) -> 1에 가까울수록 좋은 거 0에 가까울수록 나쁜거
# -> 1 - (실제값 - 예측값)2 의 합 / (실제 값 - 평균 값)2 의 합

# 예) 
'''y    y2     (y - y2)2   (y - y평균)
  15    25        100         1936
  55    42        169         16  
  50    59         81         81    
  95    76        361         1296
  80    93        169         441     '''


# y의 평균 값은 59
# SSE의 값은 100 + 169 + 81 + 361 + 169 = 880
# SST의 값은 1936 + 16 + 81 + 1296 + 441 = 3770
# SSE / SST -> 1 - (880 / 3770)  -> 1 - 0.233 = 0.767 


## 외귀 모델 평가 실습
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error

dataset = pd.read_csv("C:\\Users\\dhwhang\\Desktop\\PythonMLWorkspace(LightWeight)\\ScikitLearn\\MultipleLinearRegressionData.csv")

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop='first'), [2])] , remainder='passthrough')

X = ct.fit_transform(X)


from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)


# MAE (Mean Absolute Error)
from sklearn.metrics import mean_absolute_error
print("MAE")
print(mean_absolute_error(y_test, y_pred))  # 실제 값(y_test), 예측 값(y_pred) 


# MSE (Mean Squared Error)
from sklearn.metrics import mean_squared_error
print("MSE")
print(mean_squared_error(y_test, y_pred))  # 실제 값(y_test), 예측 값(y_pred) 

# RMSE (Root Mean Squared Error)
from sklearn.metrics import mean_squared_error
print("RMSE")  # -> squared=False 넣은 이유는 root가 들어가기 때문
print(mean_squared_error(y_test, y_pred, squared=False))  # 실제 값(y_test), 예측 값(y_pred) 

# R2 (R Square)
from sklearn.metrics import r2_score
print("R2")
print(r2_score(y_test, y_pred))

