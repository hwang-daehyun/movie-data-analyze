import pandas as pd

file_path = "C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\titanic_train.csv"

df = pd.read_csv(file_path)

print(df.describe())


## **대푯값**
#|min()|최솟값|
#|max()|최댓값|
#|mean()|평균|
#|median()|중간값|
#|std()|표준편차|
#|var()|분산|
#|quantile()|분위수|

#print(df.min())  # 이렇게 할 경우 에러가 남 왜냐하면, 숫자인 데이터만 가능하지 때문에
# 그래서 아래처럼 숫자 데이터만 지정해서 해야됨.

print(df.min(numeric_only=True))

print(df.max(numeric_only=True))

print(df.mean(numeric_only=True))

print(df.median(numeric_only=True))

print(df.std(numeric_only=True))

print(df.var(numeric_only=True))

print(df.quantile(0.2, numeric_only=True))

print(df.quantile(0.9, numeric_only=True))

## **변수의 상관관계 확인하기**
#- 상관관계 분석은 두 변수의 관련성을 구하는 분석입니다.
#- 두 변수 간의 연관된 정도이지 인과관계를 설명하지 않습니다.
#- 상관계수 = 두 변수가 함께 변하는 정도 / 두 변수가 각각 변하는 정도
#- `.corr()`

print(df.corr(numeric_only=True))

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()