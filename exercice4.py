#!/usr/bin/python3
# coding: utf-8 

# définir une fonction qui prend un nombre en paramètre et return le produit par 5, print le résultat

def m(a):
     return a * 5

m(2)
print(m(5))

#2 Définir une fonction qui prend une liste de nombres en paramètre et qui retourne tous les nombres pairs

 
def fonct(x):
	maliste=[]
	for i in x:
		if (i%2) == 0:
			maliste.append(x[i])
			i+=1
		else:
			i+=1
			
	return maliste 

print fonct([0, 1, 2, 3, 4, 5, 6, 7, 8])


		

#3  Définir une fonction qui écrit la suite de fibonacci, et prend en paramètre un nombre. La fonction n'ira pas plus loin que ce nombre.

def fib2 (x):
	i=0
	maliste=[]
	maliste.append(0)
	maliste.append(1)

	while i < (x+1):
		if i<2:
			i+=1
		else:
			c= maliste[(i-1)] + maliste[(i-2)]			
			maliste.append(c)
			i+=1
	print ("Retourne la Suite de Fibonnaci:")
	return maliste
		
print fib2(9)


#4 - Définir une fonction qui compte le nombre de voyelle dans une chaine de caractère passé en argument avec une boucle for. Définir une deuxième fonction identique avec une boucle while. En faire une troisième avec une string dans le "in" de la condition

def nbreVoyelle (string):
	nbr_Voyelle = 0
	chaine=string.lower() #On convertit la chaine de caractère rentrée en paramètre de la focntion en miniscule
	liste_voyelle = ['a','e','i','o','u','y']
	for elt in chaine:
		for elt1 in liste_voyelle:
			if elt==elt1:
				nbr_Voyelle +=1
	print ("nbredevoyelle",nbr_Voyelle)
	return nbr_Voyelle
print nbreVoyelle ("bonjour le monde")

#5 - Définir une fonction qui retourne la factorielle d'un nombre passé en argument. Par rappel, la factorielle d'un nombre "n" et la multiplication de tous les nombres n par les nombres n-1 jusqu'à ce que n soit égal à 1.

def fact(n):
   
    x=1
    for i in xrange(2,n+1):
        x*=i
    return x
    
 #exemple d'exécution 
print fact(4)


#6 - Recommencer une fonction de factorielle de n avec une fonction récurrente
def fact(n):
   
    if n<2:
        return 1
    else:
        return n*fact(n-1)
 
#exemple d'exécution 
print fact(5)


#7 - Définir une fonction avec une nombre variable d'arguments. La fonction devra afficher le nombre d'arguments passer, et la somme des nombres (qui seront donc passés en arguments)

def somme(x, y, z):
	return x+y+z
	
print somme(4,5,6)

#8 - Soit la liste suivante : [1, 4 ,9 ,16 ,25 ,36 ,49 ,64 ,100 ,121]. Définir une fonction permettant de récupérer le premier chiffre d'un nombre. créer une deuxième fonction qui appelle la première pour afficher la fréquence d'apparition des premiers chiffres.

#résultat attendu : {1: 4, 2: 1, 3: 1, 4: 2, 5: 0, 6: 1, 7: 0, 8: 0, 9: 1}

def premier_chiffre () :
	liste=[1, 4 ,9 ,16 ,25 ,36 ,49 ,64 ,100 ,121]
	liste2 = []
	liste3 = []
	chiffre=0
	i=0
	for chiffre in range (0,10):
		elt=str (liste[chiffre])
		liste2.append(elt[0])
		
	for i in range(0,10):
		elt2= int (liste2 [i])
		liste3.append (elt2)

	return liste3
print ("cette fonction reccupere le 1er chiffre d'un nombre de la liste [1, 4 ,9 ,16 ,25 ,36 ,49 ,64 ,100 ,121]", premier_chiffre())



def frequence_chiffre():
	i=0
	liste=[]
	liste2=[]
	liste=premier_chiffre()

	for i in range (1,len(liste)):
		index=liste.count(i)
		liste2.append ("{0} {1} {2} {3} {4}".format ("{", i, ":" ,index,"}"))		
		i +=1

	#print "ma liste2",liste2
	return liste2
	
print frequence_chiffre()
 


