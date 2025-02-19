# 2. 출생아 수 및 합계출산율
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15 #글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False 

df = pd.read_excel('C:\\Users\\dhwhang\\Downloads\\출산합계.xlsx', skiprows=2, nrows=2, index_col=0)  #nrows는 불러올 로우 수 /index_col=0을 한 이유는 공란이라 인덱스0으로 불러온것.

# TIP) 혹여나 데이터를 가져 왔을 때 인덱스 확인시 df.index.values를 사용해서 정확하게 보는게 좋다.

df.rename(index={'출생아\xa0수':'출생아 수', '합계\xa0출산율':'합계 출산율'}, inplace=True)

df = df.T  # df.T 가로 세로가 뒤집힌 데이터로 바뀐다


df['출생아 수'] = pd.to_numeric(df['출생아 수'], errors='coerce')
df['합계 출산율'] = pd.to_numeric(df['합계 출산율'], errors='coerce')



fig, ax1 = plt.subplots(figsize=(20,7))
fig.suptitle('출생아 수 및 합계출산율')
ax1.set_ylabel('출생아 수 (천 명))')
ax1.set_ylim(200,1200)
ax1.set_yticks([200, 300 ,400, 500, 600, 700, 800, 900, 1000 ])
ax1.bar(df.index, df['출생아 수'], color='#ff812d')
for idx, val in enumerate(df['출생아 수']):
    ax1.text(idx, val+12, val, ha='center')

ax2 = ax1.twinx()  # X축을 공유하는 쌍둥이 axis
ax2.set_ylabel('합계 출산율 (가임여성 1명당 명)')
ax2.set_ylim(0,4.5)
ax2.set_yticks([0, 1, 2, 3, 4])
ax2.plot(df.index, df['합계 출산율'], color='#ffd100', marker='o', ms=9, lw=5, mec='w', mew=2)
for idx, val in enumerate(df['합계 출산율']):
    ax2.text(idx, val+0.2, val, ha='center')



plt.show()

