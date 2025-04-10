import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

df = pd.read_csv("4laptops_Updated_Price.csv")

# One-Hot Encode the Operating_System column
ohe = OneHotEncoder(drop='first', sparse_output=False)
encoded_os = ohe.fit_transform(df[['Operating_System']])
os_columns = ohe.get_feature_names_out(['Operating_System'])
encoded_os_df = pd.DataFrame(encoded_os, columns=os_columns)

# Label Encode the Category column (used here as "Stage")
le = LabelEncoder()
df['Stage'] = le.fit_transform(df['Category'])

# Combine the DataFrames
df_final = df.join(encoded_os_df)

print(df_final.head())
print("Label classes:", le.classes_)

df
