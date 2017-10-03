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
		Key word argument project allows to set any project to save.
		By default project is set to None. That means the this method will save collection 
		of cakes for current project. 
		'''

		# Check if there is any given collection to save, if not this merthod will use default collection
		if project:
			self.source_project = project

		# Check if there are any cakes to save, otherwise saving is not possible
		if len(self.source_project.cakes) > 0:

			# Create main save folder if needen
			self.ensure_dir(SAVE_FOLDER)

			# Objects ready to serialize 
			objects_to_save = self.convert_collection(self.source_project.cakes)

			#------- Project Folder Creation --------#

			# Create path for current project
			#path = os.path.dirname(os.path.abspath(__file__))

			# Creating folder name for current project
			project_folder = (self.source_project.name)
			print('Project folder: ', str(project_folder))
			
			# Creating folder for current project
			folder_creation = True
			num = 1
			print()
			print('Project folder creation to save starts')
			while folder_creation:
				print('Control number', str(num))
				try:
					# Appending number sufix for new project with a name that already exists
					if num > 1:
						#path = (path+SAVE_FOLDER+project_folder+str(num)).replace(" ", "")
						path = os.path.join(os.path.dirname(os.path.abspath(__file__)), SAVE_FOLDER, project_folder.replace(" ", "")+str(num))
						print('Path form first case: ', path)
						print('Control number', str(num))
						print()
						#print('Test path form loader: ', str(os.path.join(os.path.dirname(os.path.abspath(__file__)), SAVE_FOLDER)))
					else:
						# Case when project name does not exist
						path = os.path.join(os.path.dirname(os.path.abspath(__file__)), SAVE_FOLDER, project_folder.replace(" ", ""))
						print('Path second case statment: ', str(path))
						print('Control number', str(num))
						print()
						#path = (os.path.join(path, SAVE_FOLDER, (project_folder).replace(" ", "")))
					
					# This folder can allready exist
					print('Control number', str(num))
					print('Creates folder')
					os.makedirs(path)
					folder_creation = False
				except:
					# When folder with project name already exists, we increase the counter
					num += 1
					# Reset path to avoid nested directories
					#path = os.path.dirname(os.path.abspath(__file__))

			# Let's use a folder name to create file name
			file_name = project_folder
			# In case when we create project with thissame name that already existing one, we add number to the filename
			if num > 1:
				file_name = project_folder+str(num)
			
			# Create temporary project object that will be saved
			tpts = TempProject(self.source_project.name, objects_to_save)
			
			# Saving temporary project object to a files		
			with open(os.path.join(path, file_name.replace(" ","")+".obj"), 'wb') as f:
				print('Dumping file to: ', str(os.path.join(path, project_folder.replace(" ","")+".obj")))
				pickle.dump(tpts, f)
		
		else:
			# Do nothing when there is no cakes to save
			pass
	

	def ensure_dir(self, directory):
		'''
		This method checks if there is a directory, if not, it creates it.
		'''

		try:
			# Setting up a path for directory
			path = os.path.join(os.path.dirname(os.path.abspath(__file__)),  SAVE_FOLDER)

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


class TempProject(object):
	'''
	Object of this class keeps temporary cakes with temporary ingredients.
	Instance is intendent to be serialized via pickle.
	'''

	def __init__(self, name, project_cakes):
		self.name = name
		self.project_cakes = project_cakes 
		print('TempProject saved, name: ', str(self.name), ' cakes: ', str(self.project_cakes))