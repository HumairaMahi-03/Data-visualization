#Do the movies have higher ROI if they get released on festive seasons or long weekend? Calculate the  average ROI for different release times. 
import pandas as pd


df = pd.read_csv('/Users/macbookair/Desktop/Data_visualization/project/bollywood.csv')

df = df.dropna(subset=['Budget', 'BoxOfficeCollection'])

df = df[df['Budget'] > 0]

df['ROI'] = (df['BoxOfficeCollection'] - df['Budget']) / df['Budget']

avg_roi_by_time = df.groupby('ReleaseTime')['ROI'].mean().sort_values(ascending=False)

print(avg_roi_by_time)
