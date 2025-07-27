#. How many movies in each genre got released in different release times like long weekend, festive season, etc. (Note: Do a cross tabulation between Genre and ReleaseTime.) 
import pandas as pd


df = pd.read_csv('/Users/macbookair/Desktop/Data_visualization/project/bollywood.csv')


genre_release_crosstab = pd.crosstab(df['Genre'], df['ReleaseTime'])
print("Cross-tabulation between Genre and Release Time:\n")
print(genre_release_crosstab)
