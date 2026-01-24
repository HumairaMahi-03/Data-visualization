import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

scores = df[['math score', 'reading score', 'writing score']]

corr_matrix = scores.corr()


plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

plt.title('Correlation Heatmap of Math, Reading, and Writing Scores', fontsize=14)


plt.tight_layout()
plt.show()
