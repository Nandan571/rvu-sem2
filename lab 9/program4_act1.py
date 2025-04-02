import pandas as pd
csv_file_path = 'your_file.csv'
df = pd.read_csv(csv_file_path)
print("Last 3 rows of the DataFrame:")
print(df.tail(3))
print("\nDescription of the DataFrame:")
print(df.describe())
print("\nInformation about the DataFrame:")
print(df.info())
print("\nColumn names of the DataFrame:")
print(df.columns)
