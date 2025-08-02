import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

Groups=df['race/ethnicity'].value_counts()
colormap = cm.get_cmap('Set3', len('Groups'))
plt.pie(Groups,labels=Groups.index,autopct='%1.1f%%',startangle=90,colors=colormap.colors)

plt.show()