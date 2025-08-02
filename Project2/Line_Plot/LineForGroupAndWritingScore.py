import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")


grouped = df.groupby('race/ethnicity')['writing score'].mean()

grouped.plot(kind='line', marker='o',color='purple')


plt.title('Average writing Scores by Race/Ethnicity Group')
plt.xlabel('Race/Ethnicity Group')
plt.ylabel('Average writing Score')


plt.tight_layout()


plt.show()
