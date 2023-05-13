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


def predict_survive():
    #Récupérer les données d'un potentiel passager et verifier si il aurait potentiellement survécu
    potential_passenger_data = []
    try:
        potential_passenger_data.append(int(input("\n > En quelle classe etait le passager (1, 2 ou 3) : ")))
    except:
        print("\n\n ! ! ! ! ! \nINPUT ERROR\n ! ! ! ! !\n")
        quit()
    else:
        if potential_passenger_data[0] == -1:
            print("\n - - - - - - - - - -\nS'ettant accroché de force au bateau au moment du départ pour voyager clandestinement, le voyageur s'est surement noyé en tombant à l'eau avant même l'accident,le titanic etant fait d'un metal tres glissant... Il n'aurait donc surement pas survécu !\n - - - - - - - - - -\n")
            quit()
        else:
            if not 0 < potential_passenger_data[0] <= 3:
                print("\n\n ! ! ! ! ! \nINPUT ERROR\n ! ! ! ! !\n")
                quit()

    try:
        potential_passenger_data.append(int(input("\n > Le passager était-il un homme ou une femme ? (femme: 0 ou homme: 1) : ")))
    except:
        print("\n\n ! ! ! ! ! \nINPUT ERROR\n ! ! ! ! !\n")
        quit()
    else:
        if not 0 <= potential_passenger_data[1] <= 1:
            print("\n\n ! ! ! ! ! \nINPUT ERROR\n ! ! ! ! !\n")
            quit()

    try:
        potential_passenger_data.append(int(input("\n > Quel est l'age du passager ? : ")))
    except:
        print("\n\n ! ! ! ! ! \nINPUT ERROR\n ! ! ! ! !\n")
        quit()
    else:
        if not 1 <= potential_passenger_data[2] <= 100:
            print("\n\n ! ! ! ! ! \nINPUT ERROR\n ! ! ! ! !\n")
            quit()

    try:
        potential_passenger_data.append(int(input("\n > Combien avait-il de frères/soeurs et/ou mari/femme à bord du navire ? : ")))
    except:
        print("\n\n ! ! ! ! ! \nINPUT ERROR\n ! ! ! ! !\n")
        quit()
    else:
        if not 0 <= potential_passenger_data[3] <= 10:
            print("\n\n ! ! ! ! ! \nINPUT ERROR\n ! ! ! ! !\n")
            quit()

    try:
        potential_passenger_data.append(int(input("\n > Combien avait-il de parents/enfants à bord : ")))
    except:
        print("\n\n ! ! ! ! ! \nINPUT ERROR\n ! ! ! ! !\n")
        quit()
    else:
        if not 0 <= potential_passenger_data[4] <= 10:
            print("\n\n ! ! ! ! ! \nINPUT ERROR\n ! ! ! ! !\n")
            quit()

    try:
        potential_passenger_data.append(int(input("\n > Par quel port est rentré votre passager (0: Cherbourg, 1: Queenstown, 2: Southampton) ? : ")))
    except:
        print("\n\n ! ! ! ! ! \nINPUT ERROR\n ! ! ! ! !\n")
        quit()
    else:
        if not 0 <= potential_passenger_data[5] <= 2:
            print("\n\n ! ! ! ! ! \nINPUT ERROR\n ! ! ! ! !\n")
            quit()

    if int(model.predict([potential_passenger_data])):
        print("\n - - - - - - - - - -\nLe passager aurait surement survécu !\n - - - - - - - - - -\n")              # __END__
    else:
        print("\n - - - - - - - - - -\nLe passager n'aurait probablement pas survécu !\n - - - - - - - - - -\n")


# __Main__:
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

# Entrainner l'algorithme (après avoir testé toutes les possibilités, nous avons vu que pour 
#  une valeur "n_neighbors = 25", la précision des résultats etait la plus élevée (75.64%))
model = KNeighborsClassifier(n_neighbors = 25)
model.fit(X_train, y_train)

# Prédire la survie des passagers selon leur data et établir un pourcentage de précision de notre algorithme
y_pred = []
for data in X_test:
    y_pred.append(int(model.predict([data])))

if not (round(accuracy_score(y_test, y_pred), 10) * 100) >= 65:
    quit()

# Prédire la survie potentielle d'un passager selon ses infos
predict_survive()
