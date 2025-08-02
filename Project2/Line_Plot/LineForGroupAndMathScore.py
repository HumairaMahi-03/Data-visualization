import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset
df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

# Grouping by 'race/ethnicity' and calculating the mean math score for each group
grouped = df.groupby('race/ethnicity')['math score'].mean()

# Plotting the line plot for each race/ethnicity group
plt.figure(figsize=(10, 6))
grouped.plot(kind='line', marker='o')

# Adding title and labels
plt.title('Average Math Scores by Race/Ethnicity Group', fontsize=14)
plt.xlabel('Race/Ethnicity Group', fontsize=12)
plt.ylabel('Average Math Score', fontsize=12)

# Adjusting layout for better readability
plt.tight_layout()

# Displaying the plot
plt.show()
