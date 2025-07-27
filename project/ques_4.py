import pandas as pd

# Load the dataset
df = pd.read_csv('/Users/macbookair/Desktop/Data_visualization/project/bollywood.csv')

# Step 1: Convert 'Release Date' column to datetime
df['Release Date'] = pd.to_datetime(df['Release Date'], format='%d-%b-%y')

# Step 2: Extract month name and store in a new column called 'Month'
df['Month'] = df['Release Date'].dt.month_name()

# Step 3: Count movie releases per month
monthly_release_counts = df['Month'].value_counts()

# Step 4: Display the result
print("Number of movie releases per month:\n")
print(monthly_release_counts)

# Step 5: Show the month with the maximum releases
max_month = monthly_release_counts.idxmax()
print(f"\nMonth with the highest number of movie releases: {max_month}")
