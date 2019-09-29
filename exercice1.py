#!/usr/bin/python3
# coding: utf-8 


#1 - définir une variable et lui attribuer un nombre. Afficher cette variable
n = 10
print (n)

#2 - définir 2 variables : 1 contenant un age en nombre et l'autre contenant votre prénom. Créez une troisième variable qui devra contenir la phrase suivante : "Je suis [NOM] et j'ai [AGE] ans." Enfin, afficher cette dernière variable

monAge = 20 
prenom  = "yasmian"

presentation = "je suis " +prenom+ " et j'ai " +monAge+ " "
print (presentation)



#3 - Refaire l'exercice précédent, mais cette fois déclarer les 2 premières variables sur une seule ligne

MonAge, prenom = 20, "yasmina"
print(MonAge, prenom)

#4 - Déclarer une variable et lui attribuer un nombre. Afficher le résultat de la multiplication de cette variable par 4

var = 4
print(var*4)

#5 - Déclarer une variable et lui attribuer un nombre. trouver ensuite 2 syntaxes différentes pour ajouter "1" à ce nombre. Afficher ce nombre à chaque fois que vous ajoutez "1".

m = 18
m1 = m+1
print(m1)
m2 = 10
m2 +=1
print(m2)

#6 - Même exercice qu'avant, mais cette fois en soustrayant "1"

m3 = m - 1
print(m3)
m4 = 5
m4 -=1
print(m4)

#7 - Même exercice qu'avant, mais en multipliant par 2

c = 2
c = c*2
print(c)

c *=c
print(c)

#8 - Même exercice qu'avant mais en divisant par 2

c2 = 3
c2= 3/2
print(c2)

c2 /=2
print(c2)

#9 - Déclarer 2 variables "a" et "b", leur affecter des valeurs. Puis permuter ces variables.

a = 4; b = 5
a, b = b, a

#10 - Déclarer 2 variables prenant la meme valeur de 3 manières différentes au moins.

x = y = 6
x, y = 7, 7
x = 8
Y = 8

#11 - Déclarer 1 variable "a" et lui affecter la valeur "10". Réaliser la suite dans l'ordre :
"""
    Afficher "a"
    Afficher le résultat de la division de a par 2
    Afficher le résultat entier de la division de a par 2
    Afficher le reste de la division de a par 2
    Afficher a puissance 3
"""
a = 10
a /= 2
print ("a=",a) 
a //=2
print ("a=",a) 
a %= 2
print ("a=",a)
a = pow(a,3)
print ("a=",a)

#12 - Ecrire un programme qui lit le prix HT d’un article, le nombre d’articles et qui définit une variable contenant le taux de TVA à 20%, et qui fournit le prix total TTC correspondant. Se servir de la fonction "input()" pour demander a l'utilisateur de renseigner les informations.

TVA = 0.2
pht = input("entrer le prix ht:")
nbr_darticle = input("entrer le nombre d'article:")
pttc = (pht*(1 + TVA))*nbr_darticle
print("pttc=",pttc)
 
#Q13 Ecrire une liste comportant les nombres "4" et "5" et l'afficher.
liste = [4, 5] 

print(liste)

#Q14 Ecrire une liste avec 2 chaines de caractère et 2 nombres.
"""
    Afficher la liste
    Afficher le premier élément de la liste
    Afficher le type du 3eme élément de la liste
""" 
liste = ["toto", "titi", 2, 3]
print(liste)
print(liste[0])
type (liste[2])

#Q15 Créer 2 listes "x" et "y", avec 2 nombres dans chacune d'elle. Créer une troisième liste qui sera la concaténation de x et y. Afficher cette troisième liste

x = [0, 1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print x

#Q16
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x[3]
x [3:5]
len(x)
min(x)
max(x)
sum(x)
print(sum(x))
del x[3:5]
print (x)

#Q17
x = ["ok", 4, 2, 78, "bonjour"]
print x[3]
x[1] = "toto"
print x

#x = {'key':'valeur','key2':'valeur2'}
18 
x = [0, 1, 2, 3, 4, 5]
#deuxième manière?
print(x)

#Q19 

x = {'key':'valeur','key2':'valeur2'}
print (x)
x.get("key")
x["titi"] = "toto"
x = {'key2': 'valeur2', 'titi': 'toto', 'key': 'valeur'}
x['titi'] = 'tata'
print (x)
{'key2': 'valeur2', 'titi': 'tata', 'key': 'valeur'}
del x['titi']
print (x)
{'key2': 'valeur2', 'key': 'valeur'}
x.pop("key2")    # renvoi la valeur supprimée
x = {'key2':'valeur2'}
y = {}
y = x.copy()
print (y)
{'key2':'valeur2'}









