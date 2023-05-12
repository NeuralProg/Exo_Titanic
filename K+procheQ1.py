import pandas
import matplotlib.pyplot as plt

# Traitement csv
iris = pandas.read_csv ("iris.csv")
x = iris.loc [:,"petal_length"]
y = iris.loc [:,"petal_width"]
lab = iris.loc [:,"species"]

# Graphique
plt.axis ('equal')
plt.scatter (x [lab == 0], y [lab == 0], color ='g', label = 'setosa')
plt.scatter (x [lab == 1], y [lab == 1], color ='r', label = 'versicolor')
plt.scatter (x [lab == 2], y [lab == 2], color ='b', label = 'virginica')
plt.scatter (2.0, 0.5, color = 'k')
plt.scatter (2.5, 0.75, color = 'k')
plt.legend ()
plt.show ()
