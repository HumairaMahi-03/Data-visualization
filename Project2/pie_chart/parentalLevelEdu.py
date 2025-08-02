import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

Edu_level_counts=df['parental level of education'].value_counts()

colormap = cm.get_cmap('Set3', len(Edu_level_counts))
plt.pie(Edu_level_counts,labels=Edu_level_counts.index,autopct='%1.1f%%',startangle=90,colors=colormap.colors)



plt.show()