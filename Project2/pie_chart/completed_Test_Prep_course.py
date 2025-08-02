import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

Prep_Count=df['test preparation course'].value_counts()


plt.pie(Prep_Count,labels=Prep_Count.index,autopct='%1.1f%%',colors=['purple','gold'])
plt.show()