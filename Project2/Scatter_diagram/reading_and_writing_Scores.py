import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")


plt.scatter(df['reading score'], df['writing score'], color='blue', alpha=0.6)


plt.title('Scatter Plot: Reading Score vs Writing Score')
plt.xlabel('Reading Score')
plt.ylabel('Writing Score')


plt.tight_layout()
plt.show()
