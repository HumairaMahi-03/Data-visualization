import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

gender_counts=df['gender'].value_counts()


plt.pie(gender_counts,labels=gender_counts.index,autopct='%1.1f%%',colors=['pink','purple'])



plt.show()