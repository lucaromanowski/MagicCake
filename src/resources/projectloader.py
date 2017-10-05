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
		self.all_loaded_projects = None



	def load_all_projects(self, path=None):
		'''
		This method loads all projects. The path to the folder with projects can be specified 
		by passing the path argument. If not, method will use default path.
		'''
	
		# Check if there is any given path, if not use default path
		if not path:
			path = os.path.join(os.path.dirname(os.path.abspath(__file__)), SAVE_FOLDER)

		# Reset all projects list
		self.reset()
		
		

		# Get project folders
		
		
		# We are looking for any project files in save catalogue
		for walk_path, dirs, files in os.walk(path):
			if files:
				# Opening the file
				try:
					for file in files:
						with open(os.path.join(walk_path, file), 'rb') as f:
							# Load file with pickle
							proj = pickle.load(f) 
							# test append
							self.all_temp_loaded_projects.append(proj)
				except:
					#print("Can't load save file")
					pass

		# Converting collection into proper project objects
		self.all_loaded_projects =  self.convert_collection(self.all_temp_loaded_projects)


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

		# List of final projects 
		projects_list = []
		# Recreating projects from temporary projects 
		for project in collection:
			# Creating new project
			p = NewProject(project.name)
			for TempAll in project.project_cakes:
				# Create cake object
				c = Cake(self.program, TempAll.cake.name)
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
					# Adding ingredient to cake
					c.ingredients.add(i)
				# Appending Cake to project
				p.cakes.append(c)
			#Appending project to projects list
			projects_list.append(p)
		return projects_list









		