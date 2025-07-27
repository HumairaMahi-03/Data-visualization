import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/macbookair/Desktop/Data_visualization/project/bollywood.csv')


df = df.dropna(subset=['BoxOfficeCollection', 'YoutubeLikes'])


plt.figure(figsize=(10, 6))
plt.scatter(df['YoutubeLikes'], df['BoxOfficeCollection'], color='blue', alpha=0.6)
plt.title("Box Office Collection vs. YouTube Likes")
plt.xlabel("YouTube Likes")
plt.ylabel("Box Office Collection")


plt.show()