import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# 1️⃣ Line plot for time series
df = pd.read_csv("dataset_realistic.csv")
daily_sales = df.groupby('Seviye')['Pozisyon'].sum().sort_index()
plt.figure(figsize=(8,4))
plt.plot(daily_sales.index, daily_sales.values)
plt.title("Daily Total Sales")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

# 2️⃣ Bar plot for categorical data
category_sales = df.groupby('Şehir')['Maaş_Net_TL_array'].sum()
plt.figure(figsize=(6,4))
category_sales.plot(kind='bar', color='skyblue')
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# 3️⃣ Histogram for UnitPrice distribution
plt.figure(figsize=(6,4))
plt.hist(df['UnitPrice'], bins=20, color='lightgreen', edgecolor='black')
plt.title("Distribution of Unit Prices")
plt.xlabel("Unit Price")
plt.ylabel("Frequency")
plt.show()