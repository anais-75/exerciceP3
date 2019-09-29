#!/usr/bin/python3
# coding: utf-8 
#1 - créez une boucle for qui affiche les numéros de 0 à 5

for i in range(0,6):
	print ("i a pour valeur", i)

#2 - créez une liste de 3 mots. Parcourez la liste a l'aide d'une boucle "for" et pour chaque mot afficher le nombre de caractère du mot et le mot en question

liste = ["maggie", "homer", "marge"] 	
for mots in liste:
    print 'longueur de la chaîne', mots, '=', len(mots)
    
    
#3 - Soit la variable x = "anticonstitutionnellement". A l'aide d'une boucle for, afficher les lettres présentes dans x.

x = "anticonstitutionnellement"
for lettre in x:
	print(lettre)

#4 - Soit la liste suivante : x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]].  parcourez l'ensemble pour afficher tous les nombres

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
i = 0

while i < len(x):
     j = 0
     while j < len(x[0]):
            print(x[i][j])
            j += 1
     i += 1

#avec la boucle for 

for line in x:
	for elem in line:
		print(elem)

#5 - Soit la liste suivante : x = [1,10,20,30,40,50]. Définissez a et b, 2 variables prenant chacune la sommu des nombres de la liste x. Les 2 sommes doivent être calculées différemment. Afficher a et b


x = [1,10,20,30,40,50]
a = sum(x)
print("la somme a vaut",a)



x = [1,10,20,30,40,50]
b = 0
for i in x:
	b += i
print("la somme b vaut", b) 



	
#6 - En utilisant la fonction range(), afficher tous les nombres de 0 à 5 en ordre décroissant


print(sorted(range(0,5), reverse=True))

	
#7 - Grâce à la fonction range(1, 10), afficher tous les nombres de 1 à 3. La boucle doit s'arrêter une fois que le chiffre 3 est affiché.

for i in range(0, 10):
     if i > 3:
         break
     print(i)



#8 - Refaire le même exercice que le précédent, mais cette fois variabiliser tous les nombres. ???????
a, b, c = 0, 10, 3
x = range(a, b)
for i in x:
	if i > c:
		break
	print(i) 
 
#9 - Grâce à la fonction range(1, 10), afficher tous les nombres de 1 à 9. La boucle ne doit pas afficher le nombre "3" mais doit obligatoirement continuer jusqu'au bout. Le faire de 2 manières différentes

for i in range(0, 10):
    if i < 10 and i!=3:
         print(i)

# 2 manière ????


#boucle while

#10 - Grâce à la liste suivante : ordi = ["apple", "asus", "dell", "samsung"], utilisez la boucle While pour afficher toutes les marques d'ordinateur

ordi = ["apple", "asus", "dell", "samsung"]
i = 0
while i < len(ordi):
    print(ordi[i])
    i += 1



#11 - Grâce à une boule while et a la fonction input(), demandez à l'utilisateur de saisir du texte, et quitter lorsqu'il écrit le mot "exit"


while True:
     x = input("je saisi du text au clavier:")
     if x == "exit":
             break



#12 - Grâce à une boucle while, afficher les nombres de 0 à 100 de 5 en 5

while i in range(0,100):
     print(i)
     i = i+5

