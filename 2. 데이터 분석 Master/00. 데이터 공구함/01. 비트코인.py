import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\User\\Downloads\\BTC-USD.csv")
df['Date'] = pd.to_datetime(df['Date'])



plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Open'], label='Bitcoin Price', color='blue')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Bitcoin Price (2014-2023)')
plt.legend()
plt.grid(True)
plt.show()