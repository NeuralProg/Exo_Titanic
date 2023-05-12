import pandas
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Traitement csv
iris = pandas.read_csv ("iris.csv")
x = iris.loc [:,"petal_length"]
y = iris.loc [:,"petal_width"]
lab = iris.loc [:,"species"]

# Valeurs
longueur = 2.5
largeur = 0.75
k = 5

# Graphique
plt.axis ('equal')
plt.scatter (x [lab == 0], y [lab == 0], color ='g', label = 'setosa')
plt.scatter (x [lab == 1], y [lab == 1], color ='r', label = 'versicolor')
plt.scatter (x [lab == 2], y [lab == 2], color ='b', label = 'virginica')
plt.scatter (longueur, largeur, color ='k')
plt.legend ()

# Algo knn
d = list (zip (x, y))
model = KNeighborsClassifier (n_neighbors = k)
model.fit (d, lab)
prediction = model.predict ([[longueur, largeur]])

# Affichage résultats
txt = "Résultat : "
if prediction [0] == 0:
    txt = txt + "setosa"
if prediction [0] == 1:
    txt = txt + "versicolor"
if prediction [0] == 2:
    txt = txt + "virginica"

plt.text (3, 0.5, f"largeur : {largeur} cm longueur : {longueur} cm", fontsize = 12)
plt.text (3, 0.3, f"k : {k}", fontsize = 12)
plt.text (3, 0.1, txt, fontsize = 12)
plt.show ()
			
