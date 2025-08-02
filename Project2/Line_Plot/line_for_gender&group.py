import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

grouped = df.groupby(['race/ethnicity', 'gender']).size().unstack()

grouped.plot(kind='line', marker='o', figsize=(12, 8))

plt.title('Count of Students by Race/Ethnicity and gender')
plt.xlabel('Race/Ethnicity Group')
plt.ylabel('Count of Students')

plt.tight_layout()

plt.show()
