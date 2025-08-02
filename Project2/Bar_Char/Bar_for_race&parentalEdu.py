import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")
plt.figure(figsize=(12, 8))


df.groupby(['race/ethnicity', 'parental level of education']).size().unstack().plot(kind='bar')


plt.title('Count of Students by Race/Ethnicity and Parental Level of Education')
plt.xlabel('Race/Ethnicity Group')
plt.ylabel('Count of Students')

plt.tight_layout()


plt.show()
