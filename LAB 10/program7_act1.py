import pandas as pd

data = [
    {"Product Name": "Laptop", "Category": "Electronics", "Price": 50000},
    {"Product Name": "Chair", "Category": "Furniture", "Price": 3000},
    {"Product Name": "Notebook", "Category": "Stationery", "Price": 100},
    {"Product Name": "Smartphone", "Category": "Electronics", "Price": 20000},
]

df = pd.DataFrame(data)

df["Discount Price"] = df["Price"] * 0.9

print(df)
