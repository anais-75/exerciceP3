#!/usr/bin/python3
# coding: utf-8 

#1 - Ecrire un programme qui demande deux nombres à l’utilisateur et l’informe ensuite si leur produit est nul, négatif ou positif.


a = int(input ("entrez le premier nombre : "))
b = int(input("entrez le deuxième nombre: "))

if a*b == 0 : 
	print ( "le produit est nul")
elif (a*b < 0): 
	print ( "le produit est negatif")
else: 
	print ("le produit est positif")

#2 - Ecrire un programme qui demande l'age de l'utilisateur, et qui lui dit s'il est majeur ou non

age_majeur = 18

age_utilisateur = int(input ("Entrez votre âge: "))
if  age_utilisateur >= age_majeur : 
	print ("Vous êtes majeur")
else: 
	print ("Vous n'êtes pas majeur")

#3 - Demandez un nombre à un utilisateur, créer une condition qui affichera si le nombre de l'utilisateur est comprit entre 5 et 10. 5 et 10 sont exclut (les nombres doivent donc etre 6, 7, 8 ou 9 pour que le programme afficher "vrai")

a= int(input("Veuillez entrer un nombre : "))
if 9 >= a >= 6 : 
	print ("True")

 
#4 - Même exercice qu'avant, mais cette fois écrire la condition d'une manière différente

a= int(input("Veuillez entrer un nombre : "))
if 10 > a > 5 : 
	print("True") 

