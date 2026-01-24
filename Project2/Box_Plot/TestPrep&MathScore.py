import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

plt.figure(figsize=(8, 6))
sns.boxplot(x='test preparation course', y='math score', data=df, palette='Set3')


plt.title('Box Plot: Math Scores vs Test Preparation Course', fontsize=14)
plt.xlabel('Test Preparation Course', fontsize=12)
plt.ylabel('Math Score', fontsize=12)


plt.tight_layout()
plt.show()
