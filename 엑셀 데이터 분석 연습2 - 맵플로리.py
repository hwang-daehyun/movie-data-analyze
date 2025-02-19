# Matplotlib
#-> 다양한 형태의 그래프를 통해서 데이터 시각화를 할 수 있는 라이브러리
import matplotlib.pyplot as plt

# 1. 그래프 기본
'''x=[1, 2, 3]
y=[2, 4, 8]
plt.plot(x, y)'''


# Title 설정
'''plt.plot(x, y)
plt.title('Line Graph')
plt.show()'''



# 한글 폰트 설정
import matplotlib
import matplotlib.font_manager as fm




plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15 #글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False  #한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결
'''fm.fontManager.ttflist'''   #사용 가능한 폰트 목록 확인
'''print([f.name for f in fm.fontManager.ttflist])'''

'''plt.plot(x, y)
plt.title('꺾은선 그래프')
plt.show()


plt.plot([-1, 0, 1], [-5, -1, 2])
plt.show()'''


# 2. 축
'''x=[1, 2, 3]
y=[2, 4, 8]
plt.plot(x, y)
plt.title('꺾은선 그래프', fontdict={'family': 'HYGungSo-Bold', 'size':20} )   #개별 폰트 설정
plt.xlabel('X 축',color = 'red', fontdict={'family': 'HYGungSo-Bold'}, loc='right')  #X축 loc에 들어갈 수 있는 건 left, center, right
plt.ylabel('Y 축',color = '#00aa00', fontdict={'family': 'HYGungSo-Bold'}, loc='top') #Y축 loc에 들어갈 수 있는 건 top, center, bottom
plt.show()

plt.plot(x, y)
plt.xticks([1, 2, 3])
plt.yticks([3, 6, 9, 12])
plt.show()'''


# 3. 범례

'''x=[1, 2, 3]
y=[2, 4, 8]
plt.plot(x, y, label='무슨 데이터')'''
'''plt.legend()'''   #만약 범례의 위치를 변경하고 싶다면 legend( ) 괄호안에 loc를 통해 지정해 줄 수 있다.
'''plt.show()'''

'''plt.legend(loc='upper right')
plt.legend(loc='lower right')'''
'''plt.legend(loc=(0.7,0.8))'''  #세부적인 조정도 가능하다


# 4. 스타일
'''plt.plot(x, y, linewidth=5)'''  #linewidth 라인 두께 설정을 가능

# 마커(marker)
'''plt.plot(x, y, marker='o')'''  #선에 점을 찍어줌
'''plt.plot(x, y, marker='o', linestyle='None')'''  #점만 남고 선은 없어짐
'''plt.plot(x, y, marker='v', markersize=10)'''  #선에 삼각형을 찍어줌, 사이즈도 조절 가능
'''plt.plot(x, y, marker='X')'''  #선에 X을 찍어줌
'''plt.plot(x, y, marker='+', markersize=10, markeredgecolor='red')'''
'''plt.plot(x, y, marker='o', markersize=10, markeredgecolor='red', markerfacecolor='yellow')'''
#markeredgecolor는 마커 테두리의 색을 변경하는 것.
#markerfacecolor는 마커의 색을 변경하는 것.

# 선 스타일
'''plt.plot(x, y, linestyle=':')''' # 선 스타일이 점선
'''plt.plot(x, y, linestyle='--')''' #점선 보다는 좀더 촘촘한 스타일
'''plt.plot(x, y, linestyle='-.')''' #점선과 선이 같이 나오는 스타일

# 선 색깔
'''plt.plot(x, y, color='#ff0000') '''

# 포맷 (따로 정의하는게 아닌 한번에 정의 하는 것)
'''plt.plot(x, y, 'ro--')''' #r: color, o: marker, --:linestyle
'''plt.plot(x, y, 'go')''' #이럴경우 선 스타일이 없기 때문에 선은 안나옴

# 축약어
'''plt.plot(x, y, marker='o', mfc='red', ms=10, mec='blue', ls=':')'''
#mfc = markerfacecolor/ ms = markersize/ mec = markeredgecolor/ mew = markeredgewidth
#lw = linewidth/ ls = linestyle

# 선의 투명도
'''plt.plot(x, y , marker='o', ms=10, mfc='red', alpha=0.5)'''  #alpha : 투명도(0~1)

# 그래프의 크기
'''x=[1, 2, 3]
y=[2, 4, 8]
plt.figure(figsize=(10,5))
plt.plot(x, y)
plt.show()'''

'''x=[1, 2, 3]
y=[2, 4, 8]
plt.figure(figsize=(10,5), dpi=200)'''  #dpi : dots per inch : 확대
'''plt.plot(x, y)
plt.show()'''

'''x=[1, 2, 3]
y=[2, 4, 8]
plt.figure(facecolor='yellow')
plt.plot(x, y)
plt.show()'''
## TIP) 만약 원하는 컬러의 색의 RGB값을 알고 싶다면 color picker로 확인하면 됨.

# 5. 파일 저장
'''x=[1, 2, 3]
y=[2, 4, 8]
plt.plot(x, y)
plt.savefig('그래프.png')''' #만약 좀더 크게 저장하고 싶으면 dpi=를 쓰면 됨.( 예시) plt.savefig('그래프.png', dpi=100)

# 6. 텍스트
'''x=[1, 2, 3]
y=[2, 4, 8]
plt.plot(x, y, marker='o')
for idx, text in enumerate(y):
    plt.text(x[idx], y[idx] + 0.3, text, ha='center', color='blue')'''   #ha=수평을 뜯함.
'''plt.show()'''

# 7. 여러 데이터

#covid-19 백신 종류별 접종 인구

'''days = [1, 2, 3] #일
az = [2, 4, 8]  #[단위 : 만몀] 1일부터 3일까지 아스트라제네카 접종인구
pfizer = [5, 1, 3] #화이자
moderna = [1, 2, 5] #모더나'''

'''plt.plot(days, az, label='az')
plt.plot(days, pfizer, label='pfizer', marker='o', ls='--')
plt.plot(days, moderna, label='moderna', marker='s', ls='-.')
plt.legend(ncol=3)  '''       #ncol로 범례의 수를 지정할 수 있다/ 지정하면 옆으로 쭉 나열됨.
'''plt.show()'''

# 8. 막대 그래프(기본)

'''label = ['강백호', '서태웅', '정대만']
values = [190, 187, 184]
colors = ['r', 'g', 'b']
ticks = ['1번학생', '2번학생', '3번학생']
plt.bar(label, values, color=colors, alpha=0.5, width=0.5)'''   #bar 그래프에서는 두께를 그냥 width로 씀.
'''plt.ylim(175, 195)'''  #ylim은 Y축의 데이터값을 지정하는 것(175부터 195까지의 데이터만)
'''plt.xticks(rotation=45)'''      # X 축의 이름 데이터 각도를 45도로 설정하는 것.
'''plt.yticks(rotation=45)   
plt.show()'''

'''label = ['강백호', '서태웅', '정대만']
values = [190, 187, 184]
colors = ['r', 'g', 'b']
ticks = ['1번학생', '2번학생', '3번학생']
plt.bar(label, values, color=colors, alpha=0.5, width=0.5) 
plt.xticks(label, ticks)'''     #xticks(label, ticks)를 통해서 X 축의 다른 이름을 넣는 것도 가능
'''plt.show()'''

# 9. 막대 그래프(심화)
label = ['강백호', '서태웅', '정대만']
values = [190, 187, 184]
plt.barh(label, values)
plt.xlim(175, 195)
plt.show()

bar=plt.bar(label, values)
bar[0].set_hatch('/')  #///////
bar[1].set_hatch('x')    #xxxxxx
bar[2].set_hatch('..')  #......
plt.ylim(175, 200)
for idx, rect in enumerate(bar):
    plt.text(idx, rect.get_height() + 0.5, values[idx], ha='center', color='r')
plt.show()


# 10. DataFrame 활용
import pandas as pd


'''df = pd.read_excel('score.xlsx')
plt.plot(df['지원번호'], df['영어'])
plt.plot(df['지원번호'], df['수학'])
plt.grid(axis='y', color='purple', alpha=0.5, ls=':', lw=2)
plt.show()'''

# 11. 누적 막대 그래프
'''df = pd.read_excel('score.xlsx')'''
'''plt.bar(df['이름'], df['국어'], label='국어')
plt.bar(df['이름'], df['영어'], bottom=df['국어'] , label='수학')'''    #국어 점수위에 영어 점수를 쌓는 방법
'''plt.bar(df['이름'], df['수학'], bottom=df['국어'] + df['영어'], label='수학')
plt.xticks(rotation=60)
plt.legend()
plt.show()'''

# 12. 다중 막대 그래프
import numpy as np

'''df = pd.read_excel('score.xlsx')'''
'''N = df.shape[0]
index = np.arange(N)
plt.figure(figsize=(10,5))
plt.title('학생별 성적')

w = 0.25
plt.bar(index - w, df['국어'], width=0.25, label='국어')
plt.bar(index, df['영어'], width=0.25, label='영어')
plt.bar(index + w, df['수학'], width=0.25, label='수학')
plt.legend(ncol=3)
plt.xticks(index, df['이름'], rotation=45)
plt.show()'''

# 13. 원 그래프(기본)
'''values = [30, 25, 20, 13, 10, 2]
labels = ['Python', 'Java', 'Javascript', 'C#', 'C/C+', 'ETC']
explode = [0.05] * 6
plt.pie(values,labels=labels, explode=explode, autopct='%.1f%%', startangle=90, counterclock=False)'''   #startangle을 쓰면 90도 기준으로 데이터를 써넣기 시작/ counterclock을 넣으면 오른쪽 기준으로 시작함./ 퍼센트 넣는건:autopct='%.1f%%'
'''plt.legend(loc=(1.2, 0.3), title='언어별 선호도')
plt.show()'''

# 14. 원 그래프(심화)
'''values = [30, 25, 20, 13, 10, 2]
labels = ['Python', 'Java', 'Javascript', 'C#', 'C/C+', 'ETC']
colors=['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', '#a0c4ff']
explode = [0.05] * 6
dddd={'width':0.6, 'edgecolor':'w', 'lw':3}
def custom_autopct(pct):'''
'''    return ('%.1f%%' % pct) if pct >= 10 else '' ''' # 똑같은 방법으로 return '{:.1f}%'.format(pct) if pct >= 10 else '' / 만약 정수부분만 보여주고 싶다면 {:.0f}%으로 하면됨.
'''plt.pie(values,labels=labels, autopct=custom_autopct, startangle=90, counterclock=False, colors=colors, wedgeprops=dddd, pctdistance=0.7)''' #wedgeprops를 이용해서 원의 두께를 조절할 수 있다. dddd={'width':0.8} /pctdistance중심으로 부터 퍼센트의 거리

# DataFrame활용

'''df = pd.read_excel('score.xlsx')
grp=df.groupby('학교')
values = [grp.size()['북산고'], grp.size()['능남고']] #[5, 3]
label = ['북산고', '능남고']
plt.pie(values,labels=label)
plt.title('소속 학교')
plt.show()'''

# 15. 산점도 그래프
#-> 두 변수의 상관관계를 보여준다.
'''df = pd.read_excel('score.xlsx')

plt.figure(figsize=(7,7))
df['학력']=[3, 3, 2, 1, 1, 3, 2, 2]
sizes = df['학력']*100
plt.scatter(df['영어'], df['수학'], s=sizes, c=df['학력'], cmap= 'viridis', alpha=0.3)'''   #산점도의 점의 크기를 조절하기 위해서는 S를 써서 하면 된다./ 만약 학련별 색을 구분하고 싶다면C에 학력을 넣고 cmap을 이용해 색을 넣어야 한다.
'''plt.xlabel('영어 점수')
plt.ylabel('수학 점수')'''
'''plt.colorbar(ticks=[1,2,3], label='학년', shrink=0.5, orientation='horizontal')'''  #colorbar는 색깔의 의미를 알려주고, ticks를 통해서 colorbar안에 어떤 숫자를 넣을지 정할 수 있다./shrink은 컬러바의 길이/orientation은 컬러바의 위치다.
'''plt.show()'''

# 16. 여러 그래프
'''df = pd.read_excel('score.xlsx')

fig,axs = plt.subplots(2, 2, figsize=(15,10))  # 한번에 여러 그래프를 추가할 경우 추가(2 X 2에 해당하는 plot들을 생성)
fig.suptitle('여러그래프')
# 첫번째 그래프
axs[0,0].bar(df['이름'], df['국어'], label='국어 점수') #데이터 설정
axs[0,0].set_title('첫 번째 그래프') #제목
axs[0,0].legend() #범례
axs[0,0].set(xlabel='이름', ylabel='점수') #x, y측 label
axs[0,0].set_facecolor('lightyellow') #w전면색 설정
axs[0,0].grid(ls='--', lw=0.5)
# 두번째 그래프
axs[0,1].plot(df['이름'], df['수학'], label='수학 점수')
axs[0,1].plot(df['이름'], df['영어'], label='영어 점수')
axs[0,1].set_title('두 번째 그래프')
axs[0,1].legend() #범례
axs[0,1].set(xlabel='이름', ylabel='점수')
# 세번쨰 그래프
axs[1,0].barh(df['이름'], df['키'], label='키' )
# 네버째 그래프
axs[1,1].plot(df['이름'], df['사회'], label='사회 점수', color='g', alpha=0.3)
plt.show()
'''

# Matplotlib 퀴즈
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15 #글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False  #한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}
df = pd.DataFrame(data)


#1) 영화 데이터를 활용하여 X 축은 영화, Y축은 평정인 막대 그래프를 만드시오.
'''plt.bar(df['영화'], df['평점'])
plt.show()'''



#2) 앞에서 만든 막대 그래프에 제시된 세부 사항을 적용하시오.
  #제목: 국내 영화 Top8 영화 평점 정보
  #X축 label: 영화(90도 회전)
  #y축 label: 평점
'''plt.bar(df['영화'], df['평점'])
plt.xlabel('영화')
plt.ylabel('평점')
plt.xticks(rotation=90)
plt.title('국내 영화 Top8 영화 평점 정보')
plt.show()'''



#3) 개봉 연도별 평점 변화 추이를 꺾은선 그래프로 그리시오.
  #df_group = df.groupby('개봉연도').mean()
  #df_group
'''df_group = df.groupby('개봉 연도')['평점'].mean()
plt.plot(df_group.index, df_group['평점'])
plt.show()'''


#4) 앞에서 만든 그래프에 제시된 세부 사항을 적용하시오.
  #marker= 'o'
  #x축 눈금: 5년 단위(2005, 2010, 2015, 2020)
  #y축 범위: 최소7, 최대10
'''df_group = df.groupby('개봉 연도')['평점'].mean()
plt.plot(df_group.index, df_group['평점'], marker='o')
plt.xticks([2005, 2010, 2015, 2020])
plt.ylim(7, 10)
plt.show()'''


#5) 평점이 9점 이상인 영화의 비율을 확인할 수 있는 원 그래프를 제시된 세부 사항을 적용하여 그리시오.
  #label: 9점 이상 / 9점 미만
  #퍼센트: 소수점 첫째자리까지 표시
  #범례: 그래프 우측에 표시

df_9up=df['평점']>=9
values = [len(df[df_9up]), len(df[~df_9up])]
labels = ['9점 이상', '9점 미만'] 
plt.pie(values,labels=labels, autopct='%.1f%%')  
plt.legend(loc=(1.1, 0.7))
plt.show()


