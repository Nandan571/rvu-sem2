import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

df = pd.read_csv("4laptops_Updated_Price.csv")

ohe = OneHotEncoder(drop='first', sparse_output=False)
encoded_os = ohe.fit_transform(df[['Operating_System']])
os_columns = ohe.get_feature_names_out(['Operating_System'])
encoded_os_df = pd.DataFrame(encoded_os, columns=os_columns)

le = LabelEncoder()
df['Stage'] = le.fit_transform(df['Category'])

df_final = df.join(encoded_os_df)

print(df_final.head())
print("Label classes:", le.classes_)

df
