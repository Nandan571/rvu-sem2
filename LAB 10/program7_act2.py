import pandas as pd

# Loading a CSV file into a DataFrame
df = pd.read_csv('6Mcd_null_values.csv')

# Displaying the first 5 rows of the DataFrame
print("Original DataFrame:")
df

# Identifying missing values
print("\nMissing values in the DataFrame:")
print(df.isnull().sum())

# Filling all missing values with appropriate values
df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nDataFrame after filling all missing values:")
print(df.head())

# Dropping duplicate rows
df.drop_duplicates(inplace=True)

print("\nDataFrame after dropping duplicate rows:")
print(df.head())
