## 비지도 학습
# 정답이 없는 데이터에서 규칙성을 찾는 것 

## 군집화
# 유사한 특징을 가지는 데이터들을 그룹화하는 것

# K-means
# 데이터를 K 개의 클러스터(그룹)로 군집화하는 알고리즘,
# 각 데이터로부터 이들이 속한 클러스터의 중심점까지의 평균 거리를 계산 

# K-means 순서
# 1. K 값 설정
# 2. 지정된 K 개 만큼의 랜덤 좌표 설정 
# 3. 모든 데이터로부터 가장 가까운 중심점 선택
# 4. 데이터들의 평균 중심으로 중심점 이동
# 5. 중심점이 더 이상 이동되지 않을 때까지 반복

# K-means의 문제
# -> Random Initialization Trap
# 이것을 해결하기 위해 K-Means ++가 등장

# K-Means ++
# 1. 데이터 중에서 랜덤으로 1개를 중심점으로 선택
# 2. 나머지 데이터로부터 중심점까지의 거릴 계산
# 3. 중심점과 가장 먼 ㅈ지점의 데이터를 다음 중심점으로 선택
# 4. 중심점이 K개가 될 때까지 반복
# 5. K-means 전통적인 방식으로 진행


## Tip) 비지도 학습은 종속변수가 따로 없다. 결과를 가지고 유사성에 따라 분리하기 때문에

## K - 평균 실습
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.environ['OMP_NUM_THREADS'] = '1'
dataset = pd.read_csv("C:\\Users\\User\\Desktop\\ScikitLearn\\KMeansData.csv")

# X = dataset.values 
# 공식 홈페이지 권장 방식 X = dataset.to_numpy[]
X = dataset.iloc[:,:].values

# 데이터 시각화 [전체 데이터 분포]
'''plt.scatter(X[:,0], X[:,1]) # X축은 공부시간 Y축은 점수
plt.title('Score by hours')
plt.xlabel('hours')
plt.ylabel('score')
plt.show()'''

# 데이터 시각화 [축 범위 통일]
'''plt.scatter(X[:,0], X[:,1]) # X축은 공부시간 Y축은 점수
plt.title('Score by hours')
plt.xlabel('hours')
plt.xlim(0, 100)
plt.ylabel('score')
plt.ylim(0, 100)
plt.show()'''

# 피처 스케일링
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
'''print(X[0:5])'''

# 데이터 시각화 (피처 스케일링한 데이터)
'''plt.figure(figsize=(5,5))
plt.scatter(X[:,0], X[:,1])
plt.title('Score by hours')
plt.xlabel('hours')
plt.ylabel('score')
plt.show()'''

## K - 평균 실습 2

# 최적의 K 값 찾기 (엘보우 방식)
from sklearn.cluster import KMeans
inertia_list = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
    kmeans.fit(X)
    inertia_list.append(kmeans.inertia_) # 각 지점으로부터 클러스터와 중심까지의 거리의 제곱의 합

'''plt.plot(range(1,11), inertia_list)
plt.title('Elbow Mathod')
plt.xlabel('n_clusters')
plt.ylabel('inertia')
plt.show()'''

n_clusters = 4 #최적의 K 값

## K - 평균 실습 3

K = 4
# 최적의 K(4) 값으로 KMeans 학습
kmeans = KMeans(n_clusters=K, random_state=0)
y_kmeans = kmeans.fit_predict(X)
centers = kmeans.cluster_centers_ # 클러스트의 중심점 좌표
# 데이터 시각화 (최적의 K)
'''for cluster in range(K):
    plt.scatter(X[y_kmeans==cluster, 0], X[y_kmeans == cluster, 1], s=100, edgecolors = 'black') # 각 데이터 출력
    plt.scatter(centers[cluster, 0], centers[cluster, 1], s=300, edgecolors ='black', color = 'yellow', marker='s') # 중심점 네모
    plt.text(centers[cluster, 0], centers[cluster, 1], cluster, va = 'center', ha = 'center') # 클러스터 텍스트 출력'''
'''plt.title('Score by hours')
plt.xlabel('hours')
plt.ylabel('score')
plt.show()'''


## K - 평균 실습 4

# 데이터 시각화 [스케일링 원복]
X_org = sc.inverse_transform(X)    # Feature Scailing 된 데이터를 다시 원복
centers_org = sc.inverse_transform(centers)

for cluster in range(K):
    plt.scatter(X_org[y_kmeans==cluster, 0], X_org[y_kmeans == cluster, 1], s=100, edgecolors = 'black') # 각 데이터 출력
    plt.scatter(centers_org[cluster, 0], centers_org[cluster, 1], s=300, edgecolors ='black', color = 'yellow', marker='s') # 중심점 네모
    plt.text(centers_org[cluster, 0], centers_org[cluster, 1], cluster, va = 'center', ha = 'center') # 클러스터 텍스트 출력
plt.title('Score by hours')
plt.xlabel('hours')
plt.ylabel('score')
plt.show()