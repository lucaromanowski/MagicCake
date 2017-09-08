'''
Loading project
'''

import os
import pickle

from .project import NewProject
from settings import *
from sprites import Cake, Ingredient


class ProjectLoader(object):
	'''
	This class loads saved projects from file and converts it to proper cake and ingredients objects.
	'''

	def __init__(self, program):
		self.program = program
		self.all_temp_loaded_projects = []
		print('ProjectLoader Created')



	def load_all_projects(self, path=None):
		'''
		This method loads all projects. The path to the folder with projects can be specified 
		by passing the path argument. If not, method will use default path.
		'''
		print('load_all_projects ivoked')
		# Check if there is any given path, if not use default path
		if not path:
			path = os.path.join(os.path.dirname(os.path.abspath(__file__)), SAVE_FOLDER)

		# Reset all projects list
		self.reset()
		
		print('path with pos path join: ', str(path))

		# Get project folders
		print()
		print('Walk starts')
		
		# We are looking for any project files in save catalogue
		for walk_path, dirs, files in os.walk(path):
			print()
			print(walk_path)
			print(dirs)
			print(files)
			if files:
				print('Files found: ', str(files))
				# Opening the file
				try:
					for file in files:
						print('File to open: ', str(file))
						with open(os.path.join(walk_path, file), 'rb') as f:
							print('File opened')
							# Load file with pickle
							proj = pickle.load(f) 
							# test append
							self.all_temp_loaded_projects.append(proj)
				except:
					print("Can't load save file")

		print('All loaded projects: ', str(self.all_temp_loaded_projects))
		print()

		# Converting collection into proper project objects
		self.convert_collection(self.all_temp_loaded_projects)


	def reset(self):
		'''
		This method makes list of loaded projects empty.
		'''
		self.all_temp_loaded_projects = []


	def convert_collection(self, collection):
		'''
		This method converts temp projects collection into projects. It converts temp cakes
		into cakes and temp ingredients into ingredients.
		'''
		print()
		print('Converting collection form temp to regular project')
		print('Given collection: ', str(collection))

		print('Goingt through the collection')

		# List of final projects 
		projects_list = []
		# Recreating projects from temporary projects 
		for project in collection:
			print('Project: ', str(project))
			print('Project name: ', str(project.name))
			# Creating new project
			p = NewProject(project.name)
			print('Project created: ', str(p.name))
			print()
			print('Going through tempAll in  temp project')
			for TempAll in project.project_cakes:
				print(str(TempAll))
				print('Temp cake: ', str(TempAll.cake.name), ', ingredients: ' ,str(TempAll.ingredients))
				print('Creating cake')
				# Create cake object
				c = Cake(self.program, TempAll.cake.name)
				print('Cake created: ', str(c.name))
				print()
				print('Creating ingredients')
				# Create ingredient object
				for ingredient in TempAll.ingredients:
					i = Ingredient(self.program, 
								   ingredient.name,
								   ingredient.x,
								   ingredient.y,
								   ingredient.how_much,
								   ingredient.protein,
								   ingredient.carb,
								   ingredient.fat,
								   ingredient.kcal,
								   ingredient.package_size,
								   ingredient.price)
					print('Ingredient created: ', str(i.name))
					# Adding ingredient to cake
					c.ingredients.add(i)
					print('Ingredient added')
				# Appending Cake to project
				p.cakes.append(c)
				print('Cake appended to project')
			#Appending project to projects list
			projects_list.append(p)
			print('Project appended to projects list')
			print('Projects list: ', str(projects_list))
			print('End convert collection')
			print()
		return projects_list









		