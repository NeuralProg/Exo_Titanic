import pandas as pd

"""
Infos :
    - Survived  ( peut etre utilisé en bool (comme le sexe) )
    - PClass
    - Sex       ( 0 = "male"  1 = "female" ) ( False = "male"  True = "female )
    - Age
    - SibSP
    - Parch
    - Embarked  ( 0 = "S"  1 = "C"  2 = "Q" )
"""

df = pd.read_csv("titanic.csv", sep=";")

median_age = df["Age"].median()
df["Age"].fillna(median_age, inplace=True)

embark_points = ["S", "C", "Q"]
embark_point = [0, 0, 0]
for emb in range(len(df["Embarked"])):      
    try:
        embark_point[embark_points.index(df["Embarked"][emb])] += 1
        df["Embarked"][emb] = embark_points.index(df["Embarked"][emb])
    except:
        pass
df["Embarked"].fillna(embark_point.index(max(embark_point)), inplace=True)

print(df["Embarked"])
df.to_csv("titanic.csv", sep=";", index=False)
