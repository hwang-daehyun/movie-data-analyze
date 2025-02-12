import pandas as pd


time_df = pd.DataFrame({'시각' : ["2022-04-20 09:15:00",
                    "2022-02-15 12:30:00",
                    "2023-02-17 18:45:00"]})

time_df["시각"] = pd.to_datetime(time_df["시각"])

time_df["일"] = time_df["시각"].dt.day
time_df["시"] = time_df["시각"].dt.hour
time_df["분"] = time_df["시각"].dt.minute

# 해당 달의 일수를 알려줌
time_df["이달의 날짜 수"] = time_df["시각"].dt.days_in_month

# 시간을 제외한 날짜만 시리즈로 반환
time_df["날짜"] = time_df["시각"].dt.normalize()

# 날짜를 지정한 포맥의 문자열 시리즈로 반환
time_df["새 날짜 형식"] = time_df["시각"].dt.strftime("%Y.%m.%d.")

print(time_df)