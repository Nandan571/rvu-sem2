import pandas as pd

# Load the CSV file
df = pd.read_csv("2Salary.csv")

# Calculating central tendency measures
mean_value = df.mean(numeric_only=True)
median_value = df.median(numeric_only=True)
mode_value = df.mode().iloc[0]  # Taking the first mode value in case of multiple modes

# Calculating dispersion measures
min_value = df.min(numeric_only=True)
max_value = df.max(numeric_only=True)
variance_value = df.var(numeric_only=True)
std_dev_value = df.std(numeric_only=True)

# Displaying the results
print("Central Tendency Measures:")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")

print("\nDispersion Measures:")
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {std_dev_value}")
