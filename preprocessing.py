import pandas as pd

# Importing file

df = pd.read_csv("spam.csv", encoding = "ISO-8859-1")
df.head()

# Getting Summary of DataFrame (Number of rows and columns)
df.info()
df.columns

# Value Counts
value_1 = df['v1'].value_counts()
print(value_1)

# Renaming the columns for clarity
df = df.rename(columns={"v1": "Label", "v2": "Message"})
df.head()

# Label Encoding 
le = LabelEncoder()
le.fit(df['Label'])
df['encoded_label'] = le.transform(df['Label'])
print(df)

# Visualization of the spam and ham data

sns.countplot(x="Label", data=df, palette ="viridis")
plt.title("Distribution of Spam and Ham Messages")
plt.xlabel("Label")
plt.ylabel("Count")
plt.show()
