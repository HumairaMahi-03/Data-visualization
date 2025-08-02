import pandas as pd


df = pd.read_csv('/Users/macbookair/Desktop/Data_visualization/project/bollywood.csv')


df['Release_Date'] = pd.to_datetime(df['Release Date'], format='%d-%b-%y')

df['Month'] = df['Release_Date'].dt.month_name()
monthly_release_counts = df['Month'].value_counts()
print("Number of movie releases per month:\n")
print(monthly_release_counts)
max_month = monthly_release_counts.idxmax()
print(f"\nMonth with the highest number of movie releases: {max_month}")
