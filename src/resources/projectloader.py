'''
Loading project
'''

import os
import pickle

from settings import *


class ProjectLoader(object):
	'''
	This class loads saved projects from file and converts it to proper cake and ingredients objects.
	'''

	def __init__(self, program):
		self.program = program
		self.all_projects = []
		print('ProjectLoader Created')



	def load_all_projects(self, path=None):
		'''
		This method loads all projects. The path to the folder with projects can be specified 
		by passing the path argument. If not, method will use default path.
		'''
		print('load_all_projects ivoked')
		if not path:
			path = os.path.join(os.path.dirname(os.path.abspath(__file__)), SAVE_FOLDER)
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
							self.all_projects.append(proj)
				except:
					print("Can't load save file")

		print('All loaded projects: ', str(self.all_projects))
		print()