import os
import pickle

from sprites import *


class Memory(object):
	'''
	class responsible for saving objects (cakes and ingredients)
	'''
	def __init__(self, program):
		self.program = program
		self.ingredients = []

	def save(self, obj=None, group=None):
		'''
		Method can take object or group of objects and save it to a file
		'''
		
		if obj:
			# temporary object
			to = self.create_temp_obj(obj)

			# Saving file via pickle
			with open('save.obj', 'wb') as f:
				pickle.dump(to, f)

	def create_temp_obj(self, obj):
		'''
		Creates temporary objects
		'''
		# Clearing ingredients list
		self.ingredients = []

		# Creates cake object
		tc = TempCake(obj.name)
		
		# Creates ingredient objects
		for ingr in obj.ingredients:
			ti = TempIngr(ingr.name,
						  ingr.rect.x,
						  ingr.rect.y,
						  ingr.how_much,
						  ingr.protein, 
						  ingr.carb, 
						  ingr.fat, 
						  ingr.kcal, 
						  ingr.package_size, 
						  ingr.price)
			self.ingredients.append(ti)
			
		# Creates temporary object, that combines cake with ingredients (temporary) 
		# Returns that object
		return TempAll(tc, self.ingredients)

	def load(self, filename):
		'''
		Loads temporary object from a file and returns it 
		'''

		with open(filename, 'rb') as f:
			cf_o = pickle.load(f) 

		return cf_o

	def recreate_obj(self, temp_obj):
		'''
		Recreates cake object from loaded file
		'''


 		# Creates cake object form loade file
		print(str(temp_obj))
 		
 		# Recreate cake object
		cake = Cake(self.program, temp_obj.cake.name)
		print('Cake object recreated: ', str(cake.name))

 		# Recreate ingredient object
		for ingr in temp_obj.ingredients:
 			i = Ingredient(self.program,
 						    ingr.name,
 						    ingr.x,
 						    ingr.y,
 						    ingr.how_much,
 						    ingr.protein,
 						    ingr.carb,
 						    ingr.fat,
 						    ingr.kcal,
 						    ingr.package_size,
 						    ingr.price,
 						   )
 			cake.ingredients.add(i)
		print(str(cake.ingredients))

 		# Combine

		#Cake(temp_obj.cake.name) 
 			 

		print('Cake object recreated')
		return cake


class TempCake(object):
	'''
	Creates temporary object of cake that will be serialized.
	Temp cake does not contain any non serializable elements
	'''

	def __init__(self, name):
		self.name = name


class TempIngr(object):
	'''
	Creates temporary object of ingredient that will be serialized.
	Temp ingredient does not contain any non serializable elements
	'''

	def __init__(self, name, x, y, how_much, protein, carb, fat, kcal, package_size, price):
		self.name = name
		self.x = x
		self.y = y
		self.how_much = how_much
		self.protein = protein
		self.carb = carb
		self.fat = fat
		self.kcal = kcal
		self.package_size = package_size
		self.price = price
		


class TempAll(object):
	'''
	Combines temporary cake object and ingredient object.
	This will be saved using pickle.
	'''
	
	def __init__(self, cake, ingredients):
		# First parameter is a cake obj, second is a list of ingredients
		self.cake = cake
		self.ingredients = ingredients




