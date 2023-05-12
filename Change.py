import pandas as pd

"""
Infos :
    - Survived
    - PClass
    - Sex
    - Age
    - SibSP
    - Parch
    - Embarked
"""

df = pd.read_csv("titanic.csv", sep=";")

median_age = df["Age"].median()
df["Age"].fillna(median_age, inplace=True)

embark_points = ["S", "C", "Q"]
embark_point = [0, 0, 0]
for emb in range(len(df["Embarked"])):       # 0 = "S"  1 = "C"  2 = "Q"
    df["Embarked"][emb] = embark_points.index(df["Embarked"][emb])
    embark_point[emb] += 1
df["Embarked"].fillna(embark_point.index(max(embark_point)), inplace=True)

df.to_csv("titanic.csv", sep=";", index=False)
