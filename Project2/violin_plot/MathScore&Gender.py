import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the dataset
df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

# Creating a violin plot to compare math scores for male and female students
plt.figure(figsize=(8, 6))
sns.violinplot(x='gender', y='math score', data=df, palette='Set3')

# Adding title and labels
plt.title('Violin Plot: Math Scores by Gender', fontsize=14)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Math Score', fontsize=12)

# Displaying the plot
plt.tight_layout()
plt.show()
