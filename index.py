import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Date': ['2024-01-01','2024-02-01','2024-03-01','2024-04-01','2024-05-01','2024-06-01','2024-07-01','2024-08-01','2024-09-01','2024-10-01','2024-11-01','2024-12-01'],
    'sales': [1200, 1350, 1280, 1500, 1650, 1700, 1800, 1750, 1900, 2100, 2200, 2400]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
print("Original Time Series Data:")
print(df)
df['Moving_avg_3'] = df['sales'].rolling(window=3).mean()
print("\n Data with moving Average:")
print(df)
plt.figure(figsize=(10,5))
plt.plot(df.index, df['sales'], marker='o', label='Monthly Sales')
plt.plot(df.index, df['Moving_avg_3'], marker='s',label='3-Month Moving Average')
plt.title('Time Series Analysis of Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()