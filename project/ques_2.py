# How many movies got released in each genre? Which genre had highest number of releases? Sort number of releases in each genre in descending order. 

import pandas as pd

df = pd.read_csv('/Users/macbookair/Desktop/Data_visualization/project/bollywood.csv')

genre_counts = df['Genre'].value_counts()

print("Number of movies released in each genre:\n")
print(genre_counts)

print(f"\nGenre with the highest number of releases: { genre_counts.idxmax()} ({genre_counts.max()} movies)")
