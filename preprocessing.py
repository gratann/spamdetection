import pandas as pd

# Importing file

df = pd.read_csv("spam.csv", encoding = "ISO-8859-1")
df.head()

# Dropping unnecessary columns
df = df.drop(columns = ["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"])
print(df.head())
