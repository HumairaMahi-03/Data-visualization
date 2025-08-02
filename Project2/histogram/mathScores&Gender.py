import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("/Users/macbookair/Desktop/Data_visualization/Project2/StudentsPerformance.csv")

fig,axes=plt.subplots(1,2,figsize=(14,6))
df_male=df[df['gender']=='male']
df_female=df[df['gender']=='female']

axes[0].hist(df_male['math score'],bins=10,color='blue')
axes[0].set_title('Math Score Distribution - Male Students')
axes[0].set_xlabel('Math Score')
axes[0].set_ylabel('Frequency')

axes[1].hist(df_female['math score'],bins=10,color='pink')
axes[1].set_title('Math Score Distribution - Female Students')
axes[1].set_xlabel('Math Score')
axes[1].set_ylabel('Frequency')


plt.tight_layout()
plt.show()
