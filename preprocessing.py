import pandas as pd

# Importing file

df = pd.read_csv("spam.csv", encoding = "ISO-8859-1")
df.head()

# Getting Summary of DataFrame (Number of rows and columns)
df.info()
df.columns
