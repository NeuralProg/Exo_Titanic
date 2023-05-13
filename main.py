import pandas
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

'''
Variable	Definition	                                    Key

survival	Survival	                                    0 = No, 1 = Yes
pclass	    Ticket class	                                1 = 1st, 2 = 2nd, 3 = 3rd
sex	        Sex	                                            0 = female, 1 = male
age	        Age in years	
sibsp	    # of siblings / spouses aboard the Titanic	
parch	    # of parents / children aboard the Titanic		
embarked	Port of Embarkation	                            0 = Cherbourg, 1 = Queenstown, 2 = Southampton
'''

#Remplissage des cases vides du csv
def fill_blanks(fichier):
    df = pandas.read_csv(fichier + ".csv", sep=";")

    # Convertir l'age en int et remplir les cases vides avec l'age median de tous les passagers
    median_age = df["Age"].median()
    df["Age"].fillna(median_age, inplace=True)
    df["Age"] = [int(ag) for ag in df["Age"]]

    # Convertir le point d'embarquement en int et remplir avec des probabilités les cases vides 
    embark_points = ["S", "C", "Q"]
    embark_point = [0, 0, 0]
    for emb in range(len(df["Embarked"])):      
        try:
            embark_point[embark_points.index(df["Embarked"][emb])] += 1
            df["Embarked"][emb] = embark_points.index(df["Embarked"][emb])
        except:
            pass
    df["Embarked"].fillna(embark_point.index(max(embark_point)), inplace=True)

    # Convertir le sexe en donnée int
    for sx in range(len(df["Sex"])):
        try:
            df["Sex"][sx] = int(df["Sex"][sx])
        except:
            if df["Sex"][sx] == "male":
                df["Sex"][sx] = 1
            else:
                df["Sex"][sx] = 0
        else:
            pass
    
    df.to_csv(fichier + ".csv", sep=";", index=False)


# Main:
# Préparer les listes
fill_blanks("train")
fill_blanks("test")

train = pandas.read_csv ("train.csv", sep=";")
test = pandas.read_csv ("test.csv", sep=";")

# Définir les listes de données 
X_train = list(zip(train["Pclass"],train["Sex"], train["Age"], train["SibSp"], train["Parch"], train["Embarked"]))
y_train = train["Survived"]
X_test = list(zip(test["Pclass"],test["Sex"], test["Age"], test["SibSp"], test["Parch"], test["Embarked"]))
y_test = test["Survived"]

  
# Entrainner l'algorithme
model = KNeighborsClassifier(n_neighbors = 25)
model.fit(X_train, y_train)

# Prédire la survie des passagers selon leur data
y_pred = []
for data in X_test:
    y_pred.append(int(model.predict([data])))

print(str(round(accuracy_score(y_test, y_pred), 10) * 100) + "%")


"""
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, random_state=0)

print(model.score(X_train, y_train))
print(model.score(X_test, y_test))
"""






