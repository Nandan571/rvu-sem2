import pandas as pd

def analyze_salary_data(file_path):
    """
    Calculates and displays central tendencies and dispersion measures for salary data.

    Args:
        file_path (str): The path to the CSV file containing salary data.
    """
    try:
        df = pd.read_csv(file_path)
        for col in df.columns:
            if 'salary' in col.lower():
                salary_column = col
                break

        if salary_column is None:
            print("Error: Salary column not found. Please ensure the CSV file contains a column with 'salary' in its name.")
            return

        salaries = df[salary_column]
        mean_salary = salaries.mean()
        median_salary = salaries.median()
        mode_salary = salaries.mode()
        range_salary = salaries.max() - salaries.min()
        variance_salary = salaries.var()
        std_salary = salaries.std()
        iqr_salary = salaries.quantile(0.75) - salaries.quantile(0.25)
        print("Central Tendencies:")
        print(f"  Mean: ${mean_salary:.2f}")
        print(f"  Median: ${median_salary:.2f}")
        print("  Mode:")
        for mode_value in mode_salary:
            print(f"    ${mode_value:.2f}")

        print("\nDispersion Measures:")
        print(f"  Range: ${range_salary:.2f}")
        print(f"  Variance: ${variance_salary:.2f}")
        print(f"  Standard Deviation: ${std_salary:.2f}")
        print(f"  Interquartile Range (IQR): ${iqr_salary:.2f}")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
file_path = "2salary.csv"  
analyze_salary_data(file_path)
