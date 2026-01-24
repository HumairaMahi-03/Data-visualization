import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

plt.figure(figsize=(8, 6))
sns.violinplot(x='gender', y='math score', data=df, palette='Set3')


plt.title('Violin Plot: Math Scores by Gender')
plt.xlabel('Gender')
plt.ylabel('Math Score')

plt.tight_layout()
plt.show()
