# **folium 이해하기**

import folium


## **[1] 특정 장소의 지도 시각화하기**
#- 네이버 지도에서 원하는 위치를 검색하고 공유 버튼을 통해 URL을 복사하세요.
#- [링크](https://xn--yq5bk9r.com/blog/map-coordinates)에 복사한 url을 붙여넣고 위도와 경도를 확인하세요.
'''
f = folium.Figure(width=가로길이, height=세로길이)
m = folium.Map(location=[위도, 경도], zoom_start=줌할정도).add_to(f)
m.save('test.html') #지도 저장
m
'''

f = folium.Figure(width=700, height=500)
m = folium.Map(location=[37.510781008592716, 127.09607026177875], zoom_start=16).add_to(f)
m

m.save('test.html')

## **[2] 마커 추가하기**

'''
#장소 표시 마커
folium.Marker([위도, 경도]
                , tooltip=마우스 오버시 나타남
                , popup=클릭시 나타남
                , icon=folium.Icon(color=색, icon=모양)).add_to(지도)

#원 형태 마커
folium.CircleMarker([위도, 경도]
                , radius=범위
                , color=색).add_to(지도)
'''
folium.Marker([37.510781008592716, 127.09607026177875]
              , tooltip='롯데월드').add_to(m)
print(m)

folium.Marker([37.510781008592716, 127.09607026177875]
              , tooltip='롯데월드'
              , icon = folium.Icon(color='red', icon='star')).add_to(m)
print(m)

folium.Marker([37.510781008592716, 127.09607026177875]
               , tooltip='롯데월드'
              , icon = folium.Icon(color='red', icon='star')
              , popup = '<iframe src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Lotte_World_Theme_Park.jpg/440px-Lotte_World_Theme_Park.jpg"></iframe>').add_to(m)
print(m)

folium.CircleMarker([37.510781008592716, 127.09607026177875]
              , color = 'red'
              , radius = 50).add_to(m)
print(m)