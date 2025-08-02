import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")


for group in df['race/ethnicity'].unique():
    plt.hist(df[df['race/ethnicity'] == group]['math score'], 
             bins=10, alpha=0.5, label=group)


plt.title('Math Score Distribution Across Different Race/Ethnicity Groups')
plt.xlabel('Math Score')
plt.ylabel('Frequency')


plt.legend(title='Race/Ethnicity')


plt.tight_layout()


plt.show()



