import pandas as pd

df = pd.read_csv("titanic.csv", sep=";")
median_age = df["Age"].median()
df["Age"].fillna(median_age, inplace=True)
df.to_csv("titanic.csv", sep=";", index=False)
