import pandas as pd

df = pd.read_csv('2Salary.csv')

description = df.describe()
quantiles = df['Salary'].quantile([0.25, 0.5, 0.75])

skewness = df['Salary'].skew()
kurtosis = df['Salary'].kurt()

value_counts = df['Salary'].value_counts()

print("Statistical Summary:\n", description)
print("\nQuantiles:\n", quantiles)
print("\nSkewness:", skewness)
print("\nKurtosis:", kurtosis)
print("\nValue Counts:\n", value_counts)
