import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the dataset
df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

# Selecting the columns for math, reading, and writing scores
scores = df[['math score', 'reading score', 'writing score']]

# Calculating the correlation matrix
corr_matrix = scores.corr()

# Plotting the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Adding title and labels
plt.title('Correlation Heatmap of Math, Reading, and Writing Scores', fontsize=14)

# Displaying the plot
plt.tight_layout()
plt.show()
