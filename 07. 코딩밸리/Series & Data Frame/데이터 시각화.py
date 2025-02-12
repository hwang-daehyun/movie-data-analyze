# Matplotlib

# 1. Figure : 도면
# 2. Axes : 축
# 3. Plot Elements : 그래프

import matplotlib.pyplot as plt

# Window 기본 제공 한글 폰트
plt.rc('font', family='Malgun Gothic')

# Mac 기본 제공 한글 폰트
#plt.rc('font', family='AppleGothic')

x = [1, 2, 3, 4, 5]
y = [5, 8, 19, 21, 28]
'''plt.plot(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('간단한 선 그래프')'''
'''plt.show()'''

'''df.plot(x = 'X축 열의 이름',
           y = 'Y축 열의 이름',
           kind = '그래프의 종류' -> line, bar, hist
           title = '그래프의 제목',
           xlabel = 'X축의 레이블,
           ylabel = 'Y축의 레이블)'''

import pandas as pd

# 선 그래프
data = {'A' : [1, 2, 3, 4, 5],
        'B' : [5, 8, 19, 21, 28]} 
df = pd.DataFrame(data)

'''df.plot(x='A', y='B', kind='line', title='Pandas로 그린 그래프', xlabel = 'A 축의 레이블', ylabel = 'B축의 레이블')'''
'''plt.show()'''


# 산점도 -> 이상치 분석이나 군집분석등에 사용됨.
'''x = [1, 2, 3, 4, 5]
y = [5, 8, 19, 21, 28]
plt.scatter(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('간단한 스캐터 플롯')'''
'''plt.show()'''


# 스터디카페들의 평균 별점 분포와 스터디카페 당 학생 수
rating_average = [2, 3, 5, 4, 5]
student_numbers = [1100, 900, 500, 300, 200]

plt.figure(figsize=(4,5))
plt.scatter(rating_average, student_numbers)

school_name = ['A고', 'B고', 'C고', 'D고', 'E고']

#  enumerate 리스트에서 아이템의 값과 인텍스를 같이 사용하게 해주는 것
for i, name in enumerate(school_name):
    plt.annotate(name, # 받아오는 아이템의 값
                 (rating_average[i],
                  student_numbers[i]), # 어떤 X,Y 데이터를 받아오는 지 적고
                  textcoords="offset points",
                  xytext=(0,7), # 글자 위치 선택 방식을 선택하는 것
                  ha='center', # 글자의 좌우를 정렬하는 것
                  fontsize=16) # 글자 사이즈를 정하는 것

# 이렇게 정하는 이유는 데이터의 최댓값을 범위로 하면 그래프 끝에 걸칠 수 있어서 범위를 늘려주는 것
plt.xlim(0,5.5) # -> X축의 범위
plt.ylim(0,1300) # -> Y축의 범위

# X,Y축의 눈금 글씨 크기 설정
plt.xticks(fontsize=12) 
plt.yticks(fontsize=12)

plt.title('스터티카페 입지 선정 참고 자료', fontsize=18)
plt.xlabel('근방 스터디카페 평균 별점', fontsize=16)
plt.ylabel('스터디카페 당 학생 수', fontsize=16)

# 각 점이 얼마를 나타내는지 정확하게 알기 위한 것
plt.grid(True)
plt.show()