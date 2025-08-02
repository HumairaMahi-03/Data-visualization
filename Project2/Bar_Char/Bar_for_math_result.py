import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

plt.figure(figsize=(10, 6))
df.groupby('race/ethnicity')['math score'].mean().plot(kind='bar', color='skyblue')

plt.title('Average Math Scores by Race/Ethnicity Group')
plt.xlabel('Race/Ethnicity Group')
plt.ylabel('Average Math Score')

plt.tight_layout()

plt.show()