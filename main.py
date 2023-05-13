import pandas
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#Remplissage des cases vides
def fill_blanks(fichier):
    df = pandas.read_csv(fichier + ".csv", sep=";")

    median_age = df["Age"].median()
    df["Age"].fillna(median_age, inplace=True)
    df["Age"] = [int(ag) for ag in df["Age"]]

    embark_points = ["S", "C", "Q"]
    embark_point = [0, 0, 0]
    for emb in range(len(df["Embarked"])):      
        try:
            embark_point[embark_points.index(df["Embarked"][emb])] += 1
            df["Embarked"][emb] = embark_points.index(df["Embarked"][emb])
        except:
            pass
    df["Embarked"].fillna(embark_point.index(max(embark_point)), inplace=True)

    df["Sex"] = (df["Sex"]== "male").astype("int")
    
    df.to_csv(fichier + ".csv", sep=";", index=False)
    

# __Main()__:
fill_blanks("train")
fill_blanks("test")
train = pandas.read_csv ("train.csv")
test = pandas.read_csv ("test.csv")


#train.info()


'''
Variable	Definition	                                    Key

survival	Survival	                                    0 = No, 1 = Yes
pclass	    Ticket class	                                1 = 1st, 2 = 2nd, 3 = 3rd
sex	        Sex	                                            0 = female, 1 = male
Age	        Age in years	
sibsp	    # of siblings / spouses aboard the Titanic	
parch	    # of parents / children aboard the Titanic		
embarked	Port of Embarkation	                            0 = Cherbourg, 1 = Queenstown, 2 = Southampton
'''



