import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('/Users/macbookair/Desktop/Data_visualization/project/bollywood.csv')


df['Release_Date'] = pd.to_datetime(df['Release Date'])


fig, ax = plt.subplots(1, 2, figsize=(16, 6))


ax[0].hist(df['Budget'], bins=20, color='skyblue', edgecolor='black')
ax[0].set_title('Histogram of Movie Budgets (in crores ₹)')
ax[0].set_xlabel('Budget (in crores ₹)')
ax[0].set_ylabel('Number of Movies')


df['Month'] = df['Release_Date'].dt.month_name()


monthly_avg = df.groupby('Month')['Budget'].mean().sort_values()


ax[1].plot(monthly_avg.index, monthly_avg.values, 
          color='orange', linewidth=2, marker='o')
ax[1].set_title('Average Budget by Release Month')
ax[1].set_xlabel('Month')
ax[1].set_ylabel('Average Budget (in crores ₹)')
ax[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()