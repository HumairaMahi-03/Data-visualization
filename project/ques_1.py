#1. How many records are present in the dataset? Print the metadata information of the dataset.
import pandas as pd

df = pd.read_csv('/Users/macbookair/Desktop/Data_visualization/project/bollywood.csv')
num_records = len(df)
print( f"{num_records} records are present")
print("\nMetadata information:")
df.info()
