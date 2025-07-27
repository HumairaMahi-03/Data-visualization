import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/macbookair/Desktop/Data_visualization/project/bollywood.csv')
df['ROI'] = (df['BoxOfficeCollection'] - df['Budget']) / df['Budget']


avg_roi = df[df['Genre'].isin(['Comedy', 'Drama'])].groupby('Genre')['ROI'].mean()


plt.figure(figsize=(8, 6))
plt.pie(avg_roi, labels=avg_roi.index, autopct='%1.1f%%', 
        colors=['skyblue','purple'], startangle=90)
plt.title('Average ROI Comparison: Comedy vs Drama')
plt.show()