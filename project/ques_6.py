import pandas as pd

# Load the dataset
df = pd.read_csv('/Users/macbookair/Desktop/Data_visualization/project/bollywood.csv')

df = df.dropna(subset=['BoxOfficeCollection', 'Budget'])

df = df[df['Budget'] > 0]

df['ROI'] = (df['BoxOfficeCollection'] - df['Budget']) / df['Budget']


top_10_roi = df.sort_values(by='ROI', ascending=False).head(10)


print(top_10_roi[['MovieName', 'BoxOfficeCollection', 'Budget', 'ROI']])
