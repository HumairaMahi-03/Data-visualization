import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

df.groupby(['race/ethnicity','lunch']).size().unstack().plot(kind='bar')

plt.title('Lunch type by Race/Ethnicity Group')
plt.xlabel('Race/Ethnicity Group')
plt.ylabel('Lunch type')

plt.tight_layout()

plt.show()