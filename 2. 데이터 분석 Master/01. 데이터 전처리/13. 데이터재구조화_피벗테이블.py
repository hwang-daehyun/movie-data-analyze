
import pandas as pd

file_path = "C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\titanic_train.csv"

df = pd.read_csv(file_path)

# **피벗테이블**
#- 엑셀의 피벗테이블처럼 인덱스별 컬럼별 값의 연산을 할 수 있습니다.
#- `pd.pivot_table(데이터명, index=, columns=, values=, aggfunc=)`

## **단일 인덱스, 단일 컬럼, 단일 값**

print(pd.pivot_table(df, index='Sex', columns='Pclass', values='Survived', aggfunc='mean'))

print(pd.pivot_table(df, index='Pclass', columns='Sex', values='Survived', aggfunc='mean'))

print(pd.pivot_table(df, index='Sex', columns='SibSp', values='Survived', aggfunc='mean'))

print(pd.pivot_table(df, index='Sex', columns='Survived', values='Age', aggfunc='mean'))

#- `margins` 옵션을 통해 행과 열 전체의 값도 구할 수 있습니다.

print(pd.pivot_table(df, index='Sex', columns='Survived', values='Age', aggfunc='mean', margins=True))

print(pd.pivot_table(df, index='Sex', columns='Survived', values='Age', aggfunc=['max','min','mean']))

## **다중 인덱스, 다중 컬럼, 다중 값**

print(pd.pivot_table(df, index=['Sex','Pclass'], columns='Survived', values='Age', aggfunc='mean'))

print(pd.pivot_table(df, index='Survived', columns=['Sex','Pclass'], values='Age', aggfunc='mean'))

print(pd.pivot_table(df, index=['Sex','Pclass'], columns=['Survived','Embarked'], values='Age', aggfunc='mean'))

print(pd.pivot_table(df, index=['Sex','Pclass'], columns=['Survived','Embarked'], values=['Age','Fare'], aggfunc='mean'))