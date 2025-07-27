import pandas as pd

df = pd.read_csv('/Users/macbookair/Desktop/Data_visualization/project/bollywood.csv')


df['Release Date'] = pd.to_datetime(df['Release Date'], format='%d-%b-%y')

high_budget = df[df['Budget'] >= 25]
high_budget['Month'] = high_budget['Release Date'].dt.month_name()

month_counts = high_budget['Month'].value_counts()
print("High-budget movie releases by month:\n")
print(month_counts)

most_common_month = month_counts.idxmax()
print(f"\n Month with most high-budget releases: {most_common_month}")
