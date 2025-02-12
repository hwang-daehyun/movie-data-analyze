# Geopy 주소와 위도, 경도로 표시하는 좌표간의 변환을 할 수 있는 도구
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="my_geocoder")
location = geolocator.geocode("인천광역시 부평구 십정동")

print("위도:", location.latitude, "경도:", location.longitude)


# Geopy
# 1. 지오코딩 Geocoding
location = geolocator.geocode("인천광역시 부평구 십정동")
# -> 주소를 위도와 경도로 변환
print("위도:", location.latitude, "경도:", location.longitude)
# 2. 역지오코딩 Reverse Geocoding
address = geolocator.reverse((location.latitude, location.longitude))
# -> 위도와 경도를 주소로 변환
print(address)

# 거리를 구하는 방법
location_school = (37.486, 127.069)
location_studycafe = (37.489, 127.069)
distance = geodesic(location_school, location_studycafe).kilometers
print(f"두 지점 간의 거리: {distance} 킬로미터")