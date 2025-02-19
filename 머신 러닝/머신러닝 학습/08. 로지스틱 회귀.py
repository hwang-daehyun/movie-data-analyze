## 로지스틱 회귀 

# 분류를 위해 사용한다
# 선형 회귀 방식을 분류에 적용한 알고리즘, 데이터가 어떤 범주에 속할 확률을 0~1 사이의 값으로 예측, 더 높은 범주에 속하는 쪽으로 분류
# 이걸 위해 시그모이드 함수 (=로지스틱 함수)를 사용한다
# 시그모이드 함수 -> P = 1/1+e^-y 이건 결국 아무리 낮아도 0이고 아무리 높아도 1이기에 범위는 0 <= P(pass) <= 1이 된다.


## 로지스틱 회귀 - 실습

# 공부 시간에 따른 자격증 시험 합격 가능성
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset = pd.read_csv("C:\\Users\\dhwhang\\Desktop\\PythonMLWorkspace(LightWeight)\\ScikitLearn\\LogisticRegressionData.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)

# 학습 (로지스틱 회귀 모델)
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# 6시간 공부 했을 때 예측
'''print(classifier.predict([[6]]))'''
# 6시간 공부 했을 때 합격 확률 정보
'''print(classifier.predict_proba([[6]]))'''
# 결과 : [[0.141483 0.858517]]  0.14가 불합격 확률 / 0.85가 합격 확률


# 4시간 공부 했을 때 예측
'''print(classifier.predict([[4]]))'''
# 4시간 공부 했을 때 합격 확률 정보
'''print(classifier.predict_proba([[4]]))'''
# 결과 : [[0.62497682 0.37502318]]

# 분류 결과 예측(테스트 세트)
y_pred = classifier.predict(X_test)
'''print(y_pred, y_test, X_test)'''
print(classifier.score(X_test, y_test))

## 로지스틱 회귀 - 실습(데이터 시각화)

# 훈련 세트
X_range = np.arange(min(X), max(X), 0.1)
p = 1 / (1 + np.exp(-(classifier.coef_ * X_range + classifier.intercept_)))  # y = mx + b이기 때문에
p = p.reshape(-1) # 1차원 배열 형태로 변경

plt.scatter(X_train, y_train, color ='b')
plt.plot(X_range, p, color = 'g')
plt.plot(X_range, np.full(len(X_range), 0.5), color = 'r')   # X_range 개수만큼 0.5로 가득찬 배열 만들기
plt.title('Probability by hours')
plt.xlabel('hours')
plt.ylabel('Probability')


# 테스트 세트
X_range = np.arange(min(X), max(X), 0.1)
p = 1 / (1 + np.exp(-(classifier.coef_ * X_range + classifier.intercept_)))  # y = mx + b이기 때문에
p = p.reshape(-1) # 1차원 배열 형태로 변경

plt.scatter(X_test, y_test, color ='b')
plt.plot(X_range, p, color = 'g')
plt.plot(X_range, np.full(len(X_range), 0.5), color = 'r')   # X_range 개수만큼 0.5로 가득찬 배열 만들기
plt.title('Probability by hours (test)')
plt.xlabel('hours')
plt.ylabel('Probability')

'''print(classifier.predict_proba([[4.5]]))'''


## 혼동 행렬 (Confusion Matrix)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
# 결과 : [[1 1] [0 2]] 먼저 1은 불합격(예측) 불합격(실제) / 그 다음 1은 합격(예측) 불합격(실제) / 다음 0은 불합격(예측) 합격(실제) / 마지막 2는 합격(예측) 합격(실제)