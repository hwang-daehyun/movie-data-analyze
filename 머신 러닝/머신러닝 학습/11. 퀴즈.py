## Quiz
# 어느 결혼식장에서 피로연의 식수 인원을 올바르게 예측하지 못하여 버려지는 음식으로 고민이 많다.
# 현재까지 진행된 결혼식에 대한 결혼식 참석 인원과 그 중에서 식사를 하는 인원의 데이터가 제공될 때, 아래 각 문항에 대한 코드를 작성
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. QuizData에서 파일로부터 데이터를 읽어와서 결혼식 참석 인원(total), 식수인원(reception)을 각각의 변수로 저장
dataset = pd.read_csv("C:\\Users\\User\\Desktop\\ScikitLearn\\QuizData.csv")

X = dataset.iloc[:,:-1].values  # 결혼식 참석 인원
y = dataset.iloc[:,-1].values  # 식수 참석 인원

# 2. 전체 데이터를 훈련 세트와 테스트 세트로 분리 이 때 비율은 75:25로 진행

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=0) #test_size=0.25 이건 테스트 세트를 20퍼 쓰겠다는  말이다
print(X, len(X))
print(X_train, len(X_train))  # 훈련 세트 X, 개수
print(X_test, len(X_test))    # 테스트 세트 X, 개수
print(y, len(y))
print(y_train, len(y_train))  # 훈련 세트 y, 개수
print(y_test, len(y_test))   # 테스트 세트 y, 개수


# 3. 훈련 세트를 이용하여 단순 선형회귀 모델을 생성
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train, y_train)  #훈련 세트로 학습

# 4. 데이터 시각화 (훈련세트) 코드를 작성하시오.
plt.scatter(X_train,y_train, color = 'b',edgecolors='black')
plt.plot(X_train, reg.predict(X_train), color = 'g')
plt.title('total by reception (Train)')
plt.xlabel('total')
plt.ylabel('reception')
'''plt.show()'''

# 5. 데이터 시각화 (테스트 세트) 코드를 작성하시오.
plt.scatter(X_test,y_test, color = 'y', edgecolors='black')
plt.plot(X_test, reg.predict(X_test), color = 'r')
plt.title('total by reception (Test)')
plt.xlabel('total')
plt.ylabel('reception')
plt.show()


# 6. 훈련 세트, 테스트 세트에 대한 각각 모델 평가 점수를 구하시오.
print(reg.score(X_test,y_test))  # 테스트 세트를 통한 모델 평가
print(reg.score(X_train,y_train)) # 훈련 세트를 통한 모델 평가


# 7. 결혼식 참석 인원이 300명일 때 예상되는 식수 인원을 구하시오.
print('결혼식 참석 인원이 300명일 때 예상되는 식수 인원 : ', reg.predict([[300]]))

# 만약 좀 깥끔하게 나오고 싶다면
y_pred = reg.predict([[300]])

print(f'결혼식 참석 인원이 300명일 때 예상되는 식수 인원은 {np.around(y_pred[0]).astype(int)}명 입니다.')
