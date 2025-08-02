import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

plt.figure(figsize=(10, 6))
df.groupby('race/ethnicity')['writing score'].mean().plot(kind='bar', color='blue')

plt.title('Average Writing Scores by Race/Ethnicity Group')
plt.xlabel('Race/Ethnicity Group')
plt.ylabel('Average Writing Score')

plt.tight_layout()

plt.show()