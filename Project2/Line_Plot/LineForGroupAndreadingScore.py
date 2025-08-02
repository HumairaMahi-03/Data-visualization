import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")


grouped = df.groupby('race/ethnicity')['reading score'].mean()

grouped.plot(kind='line', marker='o',color='pink')


plt.title('Average reading Scores by Race/Ethnicity Group')
plt.xlabel('Race/Ethnicity Group')
plt.ylabel('Average reading Score')


plt.tight_layout()


plt.show()
