import pandas as pd

# Importing file

df = pd.read_csv("spam.csv", encoding = "ISO-8859-1")
df.head()
