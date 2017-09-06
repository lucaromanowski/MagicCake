'''
Saving project
'''

import os
import pickle

from settings import *


class ProjectSaver(object):
	'''
	This class saves project to a file
	'''

	def __init__(self, program):
		self.program = program
		self.source_project = self.program.current_project

		
	def save(self, project=None):
		'''
		This method saves project objects to the files.
		Key word argument objects allows to set any project to save.
		By default objects is set to None. That means the this method will save collection 
		of cakes for current project. 
		'''

		# Check if there is any given collection to save, if not this merthod will use default collection
		if project:
			self.source_project = objects

		# Create main save folder if needen
		self.ensure_dir(SAVE_FOLDER)

		# Objects ready to serialize
		objects_to_save = self.convert_collection(self.source_project.cakes)

		#------- Project Folder Creation --------#

		# Create path for current project
		path = os.path.dirname(os.path.abspath(__file__))

		# Creating folder name for current project
		project_folder = '\\'+str(self.source_project.name)
		
		# Creating folder for current project
		folder_creation = True
		num = 1
		while folder_creation:
			try:
				# Appending numberf sufix for new project with a name that already exists
				if num > 1:
					path = (path+SAVE_FOLDER+project_folder+str(num)).replace(" ", "")
					print(path)
				else:
					# Case when project name does not exist
					path = (path+SAVE_FOLDER+project_folder).replace(" ", "")
				
				# This folder can allready exist
				os.makedirs(path)
				folder_creation = False
			except:
				# When folder with project name already exists, we increase the counter
				num += 1
				# Reset path to avoid nested directories
				path = os.path.dirname(os.path.abspath(__file__))

		# Saving cakes to a files
		for cake in objects_to_save:

			with open((path+project_folder+cake.cake.name+".obj").replace(" ",""), 'wb') as f:
				print(path+cake.cake.name+".obj")
				pickle.dump(cake, f)
	

	def ensure_dir(self, directory):
		'''
		This method checks if there is a directory, if not, it creates it.
		'''

		try:
			# Setting up a path for directory
			path = os.path.dirname(os.path.abspath(__file__))
			path = path + SAVE_FOLDER

			# Making directory
			os.makedirs(path)
		except:
			print('directory already exists')


	def convert_collection(self, collection):
		'''
		This method converts collection of cakes into a list of temporary objects ready to serialize
		'''
		# TempAll objects list
		temp_all_list = []

		# Converting cake objects into temporary objects that are possilbe to serialize via pickle
		for cake in collection:
			print(cake.name)
			
			# Creates cake object
			tc = TempCake(cake.name)
			
			# List of ingredients
			ingredients = []

			# For each ingredient in a cake create temporary ingredient object
			for ingr in cake.ingredients:	
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
				ingredients.append(ti)
				
			# Create final temporary cake object that will be saved to a file
			ta = TempAll(tc, ingredients)
			
			# Adding Temp All object to the list of all TempAll objects
			temp_all_list.append(ta)
		
		return temp_all_list


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
	This object is a combination of temporary cake object and temporary ingredient objects.
	This will be saved using pickle.
	'''
	
	def __init__(self, cake, ingredients):
		# First parameter is a cake obj, second is a list of ingredients
		self.cake = cake
		self.ingredients = ingredients