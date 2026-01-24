import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_dic = {
    'A': [12, 15, 45, 71],
    'B': [18, 26, 50, 80],
    'C': [32, 48, 78, 93],
    'D': [29, 35, 63, 81]
}

df = pd.DataFrame(data_dic)
 
sns.heatmap(df, annot=True, cmap='inferno', fmt='d', linewidths=0.5)
plt.tight_layout()
plt.show()
