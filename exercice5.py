#!/usr/bin/python3
# coding: utf-8 


class Carre(object):
	count = 0
	 
	def __init__(self, cote):
		self.__class__.count += 1
		self.cote = cote 
		perimeter = self.perimeter()
		area = self.area()
		
	def perimeter(self): 
		return self.cote*4
	
	def area(self):
		return self.cote ** 2
	
	def factor (self,x):
		return self.cote*x
		
	def __repr__(self):
		return "Le carré à un côté d'une longueur de {} cm, une aire de {} cm2 et un périmètre de {} cm."\
			.format(self.cote, self.area(), self.perimeter())

	def __add__(self, c):
		nouveau_carre = self.cote + c.cote
		return Carre(nouveau_carre)

	def __sub__(self, c):
		nouveau_carre2 = self.cote - c.cote
		return Carre(nouveau_carre2)
	
	def __lt__(self, c):
		if self.cote < c.cote :
			return True
		else: 
			return False 
			

	def __le__(self, c):
		if self.cote <= c.cote :
			return True
		else: 
			return False 
			
	def __ge__(self, c):
		if self.cote >= c.cote :
			return True
		else: 
			return False 		
	
	def __eq__(self, c):
		if self.cote == c.cote :
			return True
		else: 
			return False 
	
	def __ne__(self, c):
		if self.cote != c.cote :
			return True
		else: 
			return False 
			
			
c1 = Carre(2)
c2 = Carre(3)
c3 = c1 + c2
c4 = c1 - c2
c5 = c1 != c2 # je test les différents opérateurs dans le c5
#print(c5)

a = Carre(1)
print(a.count)
b = Carre(1)
print(b.count)
         


#if _name_ == "__main__":



