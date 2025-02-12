import pandas as pd

df = pd.DataFrame({'Product' : ['A','B','A','B','A','A','B'], 
                   'Sales' : [100,150,120,80,200,180,90]})
'''print(df)'''

grouped_data = df.groupby('Product').sum().reset_index()
'''print(grouped_data)'''

grouped_object = df.groupby('Product')


for key, group in grouped_object:
    print(f"Group: {key}")
    print(group)

#df.groupby('그룹화 변수')['함수를 적용할 변수'].'함수'