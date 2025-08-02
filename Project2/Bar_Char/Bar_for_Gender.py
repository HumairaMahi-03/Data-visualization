import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

df.groupby(['race/ethnicity','gender']).size().unstack().plot(kind='bar',color=('pink','blue'))

plt.title('Gender type by Race/Ethnicity Group')
plt.xlabel('Race/Ethnicity Group')
plt.ylabel('Gender type')

plt.tight_layout()

plt.show()