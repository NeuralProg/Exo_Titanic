import pandas
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

'''
Variable	Definition	                                    Key

survival	Survival	                                    0 = No, 1 = Yes
pclass	    Ticket class	                                1 = 1st, 2 = 2nd, 3 = 3rd
sex	        Sex	                                            0 = female, 1 = male
age	        Age in years	
sibsp	    # of siblings / spouses aboard the Titanic	
parch	    # of parents / children aboard the Titanic		
embarked	Port of Embarkation	                            0 = Southampton, 1 = Cherbourg, 2 = Queenstown
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


def calc_proba():
    global v_class
    global v_sex
    global v_age
    global v_sibsp
    global v_parch
    global v_emb
                                  
    potential_passenger_data = []
    potential_passenger_data.extend([v_class.get(), v_sex.get(), v_age.get(), v_sibsp.get(), v_parch.get(), v_emb.get()])

    if int(model.predict([potential_passenger_data])):
        messagebox.showinfo( "Resultat", "Le passager aurait surement survécu !")
    else:
        messagebox.showinfo( "Resultat", "Le passager n'aurait probablement pas survécu !")
        
       
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

# ! ! ! Interface graphique avec Tkinter ! ! !
# initialiser la fenêtre tkinter
root = Tk()
root.title("Survivants du Titanic")   # donner un nom àla fenêtre
root.geometry("500x450")    # définir une taille à la fenêtre
root.resizable(False, False) #Pas possible de mofidier la taille de la fenêtre
root.configure(background="#292020")
root.grid()

# print notre intro
intro_txt = StringVar()
intro_txt.set('Ce programme à une fiabilité de : ' + str((round(accuracy_score(y_test, y_pred), 2) * 100)) + "%, il permet de prédire selon des informations entrées par l'utilisateur, si un passager du titanic aurait survécu ou non.")
Label(root, textvariable = intro_txt, wraplength=475, bg="#292020", fg="white", font=('calibri 13 bold')).place(relx=0.5, rely=0.02, anchor=N)

# Input classe 
Label(root, text = "En quelle classe etait le passager ?", wraplength=300, bg="#292020", fg="CadetBlue1", font=('calibri', 10), justify="left").grid(column=0, row=0, pady=(90, 0), padx=10)
v_class = IntVar()
v_class.set(1)                                      
p_class = ["1", "2", "3"]
for val in range(len(p_class)):    
    Radiobutton(root, 
                bg="#292020",
                fg="grey",
                text=p_class[val],
                variable=v_class,
                value=int(p_class[val])).grid(column=val+1, row=0, pady=(90, 0))

# Input sexe
Label(root, text = "Quel etait le sexe du passager ?", wraplength=300, bg="#292020", fg="CadetBlue1", font=('calibri', 10), justify="left").grid(column=0, row=1, pady=(20, 0), padx=0)
v_sex = IntVar()
v_sex.set(0)
p_sex = [["Femme", 0], ["Homme", 1]]
for val in range(len(p_sex)):    
    if val == 0:
        Radiobutton(root, 
                    bg="#292020",
                    fg="grey",
                   text=p_sex[val][0],
                   variable=v_sex,
                   value=int(p_sex[val][1])).grid(column=val+1, row=1, pady=(20, 0))
    else:
        Radiobutton(root, 
                    bg="#292020",
                    fg="grey",
                   text=p_sex[val][0],
                   variable=v_sex,
                   value=int(p_sex[val][1])).grid(column=val+1, row=1, pady=(20, 0), columnspan=2)
    
# Input age
Label(root, text = "Quel etait l'age du passager ?", wraplength=300, bg="#292020", fg="CadetBlue1", font=('calibri', 10), justify="left").grid(column=0, row=2, pady=(20, 0), padx=0)
v_age = Scale(root, from_=1, to=100, orient=HORIZONTAL, length=200, bg="#292020", fg="grey", width=5, border=0)
v_age.set(30)
v_age.grid(column=1, row=2, pady=(20, 0), padx=0, columnspan=3)

# Input sibsp
Label(root, text = "Freres/soeurs ou mari/femme à bord ?", wraplength=300, bg="#292020", fg="CadetBlue1", font=('calibri', 10), justify="left").grid(column=0, row=3, pady=(20, 0), padx=(10, 0))
v_sibsp = Scale(root, from_=0, to=10, orient=HORIZONTAL, length=150, bg="#292020", fg="grey", width=5, border=0)
v_sibsp.set(0)
v_sibsp.grid(column=1, row=3, pady=(20, 0), padx=0, columnspan=3)

# Input parch
Label(root, text = "Enfants/parents à bord ?", wraplength=300, bg="#292020", fg="CadetBlue1", font=('calibri', 10), justify="left").grid(column=0, row=4, pady=(20, 0), padx=(10, 0))
v_parch = Scale(root, from_=0, to=10, orient=HORIZONTAL, length=150, bg="#292020", fg="grey", width=5, border=0)
v_parch.set(0)
v_parch.grid(column=1, row=4, pady=(20, 0), padx=0, columnspan=3)

# Input embark
Label(root, text = "D'où est entré le passager ?", wraplength=300, bg="#292020", fg="CadetBlue1", font=('calibri', 10), justify="left").grid(column=0, row=5, pady=(20, 0), padx=0)
v_emb = IntVar()
v_emb.set(0)
p_emb = [["S.", 0], ["C.", 1], ["Q.", 2]]
for val in range(len(p_emb)):    
    Radiobutton(root, 
                bg="#292020", 
                fg="grey",
                text=p_emb[val][0],
                variable=v_emb,
                value=int(p_emb[val][1])).grid(column=val+1, row=5, pady=(20, 0))

Button(root, text="Découvrir le résultat", command=calc_proba).grid(column=1, row=6, pady=(40, 0), columnspan=3, padx=10)

root.mainloop()
