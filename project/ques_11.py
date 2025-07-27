import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/macbookair/Desktop/Data_visualization/project/bollywood.csv')


df = df.dropna(subset=['YoutubeLikes'])

genres = df['Genre'].unique()
plt.figure(figsize=(12, 6))


box_data = []
for genre in genres:
    box_data.append(df[df['Genre'] == genre]['YoutubeLikes'])

plt.boxplot(box_data, labels=genres)
plt.title('YouTube Likes Distribution by Genre')
plt.ylabel('Number of YouTube Likes')
plt.xlabel('Movie Genre')
plt.xticks(rotation=45)  

plt.tight_layout()
plt.show()

